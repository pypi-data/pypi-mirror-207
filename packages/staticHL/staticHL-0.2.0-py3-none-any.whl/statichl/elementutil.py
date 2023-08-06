"""Class + utilities for parsing, construction, and style concretization at the element level"""


import random
import string
import networkx as nx
from collections import defaultdict

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from statichl.constants import (RAND_ID_CHARSPACE, RAND_ID_LEN, HTML_ELEMENT_FMT_STR, INNER_HTML_SELECTOR,
                                OUTER_HTML_SELECTOR, CSS_DECLARATION_FMT_STR, CSS_RULESET_FMT_STR, TARGET_CSS_PROPS,
                                PARENT_REL_XPATH_SELECTOR, DEFAULT_NOINHERIT_PROP_MAP)


def _gen_rand_str() -> str:
    """generate a random `RAND_ID_LEN` string"""
    return ''.join(random.choices(RAND_ID_CHARSPACE, k=RAND_ID_LEN))


class TreeNode:
    """Graph node for some html code block element or element within a code block.

    Each `code` element is represented by a graph composed of `TreeNode` nodes.
    The final document content is constructed from one or more graphs.

    Attributes:
        _webelt: selenium web element located at ``xpath``
        _xpath: xpath string describing location in the DOM. planned usage for data viz
        _digraph: directed graph of `TreeNode`s representing the parent `code` element
        _rand_id: unique identifier linking concretized html and css ruleset
            used as the `id` attr and `id` selector, respectively
        _tag: html tag for the element this node represents
    """

    # prevent node identifier collisions
    _visited_ids = set()

    def __init__(self, digraph: nx.DiGraph, xpath: str, webelt: WebElement):
        self._webelt = webelt
        self._xpath = xpath
        self._digraph = digraph
        self._tag = self._webelt.tag_name

        # generate a unique identifier
        rand_str = _gen_rand_str()
        while rand_str[0] in string.digits or rand_str in self._visited_ids:
            # id attrs must begin with an alpha char
            rand_str = _gen_rand_str()
        self._visited_ids.add(rand_str)
        self._rand_id = rand_str

    @property
    def _inner_content(self) -> str:
        """return the content contained within this element's tags"""
        return self._webelt.get_attribute(INNER_HTML_SELECTOR)

    @property
    def _outer_content(self) -> str:
        """return this element's entire string representation: tags + inner content"""
        return self._webelt.get_attribute(OUTER_HTML_SELECTOR)

    @property
    def _style_declaration(self) -> str:
        """compute the `TARGET_CSS_PROPS` style properties at this node, return a declaration block string"""
        style_props = self._style_from_webelt()
        declaration = '\n'.join(CSS_DECLARATION_FMT_STR.format(prop_name, prop_val) for
                                prop_name, prop_val in style_props.items())
        return declaration

    @property
    def _children(self) -> list['TreeNode']:
        return list(self._digraph.successors(self))

    @property
    def html(self) -> str:
        """return concretized, sanitized html for this element and it's contents

        See features/anti-features in readme. We keep actual page content but drop all existing tag attributes
        """
        if not self._children:
            return HTML_ELEMENT_FMT_STR.format(self._tag, self._rand_id, self._inner_content, self._tag)

        processed_contents = str(self._inner_content)
        for c in self._children:
            start, end = processed_contents.split(c._outer_content, maxsplit=1)
            processed_contents = f'{start}{c.html}{end}'

        return HTML_ELEMENT_FMT_STR.format(self._tag, self._rand_id, processed_contents, self._tag)

    @staticmethod
    def build_aggregate_rulesets(document_treenodes: list['TreeNode']) -> list[str]:
        """build stylesheet contents using ``TreeNode``s representing document elements

        Collapse selectors into a single ruleset where possible to eliminate redundant code
        """
        aggregate_rulesets = []

        declaration_id_mapping = defaultdict(list)
        id_declaration_mapping = {node._rand_id: node._style_declaration for node in document_treenodes}
        for node_id, node_decl_block in id_declaration_mapping.items():
            declaration_id_mapping[node_decl_block].append(f'#{node_id}')

        for declaration, id_list in declaration_id_mapping.items():
            selector_str = ',\n'.join(id_list)
            aggregate_rulesets.append(CSS_RULESET_FMT_STR.format(selector_str, declaration))

        return aggregate_rulesets

    def _style_from_webelt(self) -> dict[str, str]:
        """build a dictionary of style attributes computed at this node

        collect values for `TARGET_CSS_PROPS` properties to construct the ruleset
        if this is the root node, traverse the chain of ancestor nodes to identify values for missing,
            non-inheritable styles
        """
        props = {prop: self._webelt.value_of_css_property(prop) for prop in TARGET_CSS_PROPS}

        # default to normal behavior if this isn't the codeblock root node
        if list(self._digraph.predecessors(self)):
            return props

        dom_root = self._webelt.parent.find_element(By.XPATH, '/html')
        parent_elt = self._webelt

        # continue iterating up the ancestor chain until all values are satisfied, or we encounter the document root
        # satisfied means having some value other than the default computed (unset) value
        satisfied_props = {}
        while len(satisfied_props) != len(DEFAULT_NOINHERIT_PROP_MAP) and parent_elt != dom_root:
            candidate_props = {parent_prop: parent_elt.value_of_css_property(parent_prop) for parent_prop in
                               DEFAULT_NOINHERIT_PROP_MAP if parent_prop not in satisfied_props}
            non_default_props = {candidate_prop: candidate_val for candidate_prop, candidate_val in
                                 candidate_props.items() if candidate_val != DEFAULT_NOINHERIT_PROP_MAP[candidate_prop]}
            satisfied_props.update(non_default_props)
            parent_elt = parent_elt.find_element(By.XPATH, PARENT_REL_XPATH_SELECTOR)

        props.update(satisfied_props)
        return props
