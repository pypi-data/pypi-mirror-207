"""Procedures for parsing, target elt identification, and graph construction at the document level"""


from itertools import chain

import lxml.html as lxml_html
from lxml.etree import Element, ElementTree
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

from statichl.elementutil import TreeNode, nx, WebElement
from statichl.constants import CODE_XPATH_SELECTOR, HTML_DOCUMENT_FMT_STR, CSS_HREF_FMT_STR


def etree_from_str(html_str: str) -> ElementTree:
    """parse content and return an ElementTree for ``html_str``"""
    return ElementTree(lxml_html.document_fromstring(html_str))


def _webelements_from_xpath(driver: WebDriver, xpath: str, limit: int = None) -> list[WebElement]:
    """get the selenium webelement at ``xpath``

    fail if no matches are found, or if ``limit`` is specified and exceeded
    """
    matches = driver.find_elements(By.XPATH, xpath)
    if not matches:
        raise RuntimeError(f'no webelement matches for {xpath}')
    if limit is not None and len(matches) > limit:
        raise RuntimeError(f'exceeded {limit} webelement matches for {xpath}')
    return list(matches)


def collect_target_elements(sl_webdriver: WebDriver, lx_tree: ElementTree) -> list[Element]:
    """collect html `code` elements to concretize. each element serves as the root of a digraph for that block

    code elements must:
        1. be detected by lxml
        2. be detected by selenium
        3. not be hidden
    """
    elt_xpath_map = {lx_element: lx_tree.getpath(lx_element) for lx_element in lx_tree.xpath(CODE_XPATH_SELECTOR)}
    visible_elements = []
    for elt, abs_xpath in elt_xpath_map.items():
        try:
            matches = _webelements_from_xpath(sl_webdriver, abs_xpath, limit=1)
        except RuntimeError:
            continue
        else:
            if matches[0].is_displayed():
                visible_elements.append(elt)

    return visible_elements


def _build_node(graph: nx.DiGraph, driver: WebDriver, lxml_tree: ElementTree, lxml_elt: Element) -> TreeNode:
    """recursive dfs traversal that builds a graph of `TreeNode` elements composing a code block"""
    node_xpath = str(lxml_tree.getpath(lxml_elt))
    node_webelt = _webelements_from_xpath(driver, node_xpath, limit=1)[0]

    node = TreeNode(graph, node_xpath, node_webelt)
    graph.add_node(node)

    children = [_build_node(graph, driver, lxml_tree, child_elt) for child_elt in lxml_elt]
    for c in children:
        graph.add_edge(node, c)

    return node


def build_codelt_graph(driver: WebDriver, lxml_tree: ElementTree, lxml_elt: Element) -> nx.DiGraph:
    """kick off construction of a digraph representing the code block at ``lxml_elt``"""
    etree_dag = nx.DiGraph()
    _ = _build_node(etree_dag, driver, lxml_tree, lxml_elt)
    return etree_dag


def build_document(element_graphs: list[nx.DiGraph], css_path: str) -> tuple[str, str]:
    """ingest graphs and return complete, static source for the document and stylesheet"""
    all_graph_nodes = list(chain.from_iterable(graph.nodes for graph in element_graphs))
    css_str = '\n'.join(TreeNode.build_aggregate_rulesets(all_graph_nodes))
    css_href_str = CSS_HREF_FMT_STR.format(css_path)

    graph_roots = tuple(next(n for n, d in graph.in_degree if d == 0) for graph in element_graphs)
    body_str = '\n'.join(root_node.html for root_node in graph_roots)

    html_str = HTML_DOCUMENT_FMT_STR.format(css_href_str, body_str)
    return html_str, css_str
