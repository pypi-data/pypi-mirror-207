import sys
import random
import argparse
import time
from pathlib import Path

from selenium.webdriver import Firefox
from selenium.common.exceptions import SessionNotCreatedException
from progress.bar import Bar

from statichl.pageutil import collect_target_elements, build_codelt_graph, build_document, etree_from_str


def _get_source(source_string: str) -> str:
    """return a url or absolute path for ingest by a selenium webdriver"""
    if source_string.startswith('http://') or source_string.startswith('https://'):
        return source_string

    local_path = Path(source_string)
    if not local_path.exists():
        raise RuntimeError('input file does not exist')

    return f'file://{local_path.resolve()}'


def _validate_output_dir(outdir: str, can_overwrite: bool) -> tuple[Path, Path]:
    """check that static html + css files either don't exist or can be overwritten"""
    outdir_path = Path(outdir)
    html_outpath = Path(outdir_path, 'static.html')
    css_outpath = Path(outdir_path, 'static.css')

    if not outdir_path.exists():
        raise RuntimeError(f'output directory {str(outdir_path)} does not exist')

    if not any((html_outpath.exists(), css_outpath.exists())):
        return html_outpath, css_outpath

    if can_overwrite:
        return html_outpath, css_outpath

    raise RuntimeError('files already exist: {}'.format(
        tuple(str(path_) for path_ in (html_outpath, css_outpath) if path_.exists())))


def _get_parsed_args(parser):
    parser.add_argument('target', type=str, help='url or filesystem path containing target content'),
    parser.add_argument('-o', '--output-dir', dest='output_dir', type=Path, required=False,
                        help='write concretized html+css to directory OUTPUT_DIR, '
                             'defaults to the current directory if unspecified'),
    parser.add_argument('-f', '--force', dest='force', action='store_true', required=False,
                        help='force overwrite; overwrite existing html+css files')
    parser.add_argument('-d', '--delay', dest='delay', type=float, required=False,
                        help='wait DELAY seconds before parsing to allow resources to load, '
                             'rationals and sub-second values allowed')
    return parser.parse_args(sys.argv[1:])


def main():
    random.seed()
    static_parser = argparse.ArgumentParser()
    parsed_args = _get_parsed_args(static_parser)
    try:
        html_source = _get_source(parsed_args.target)
        output_dir = parsed_args.output_dir or '.'
        html_outpath, css_outpath = _validate_output_dir(output_dir, parsed_args.force)
    except RuntimeError as e:
        print(f'ERROR: {e}\n\n')
        static_parser.print_help()
        sys.exit(1)
    else:
        # visit the page and get source contents
        try:
            firefox_webdriver = Firefox()
        except SessionNotCreatedException:
            print("please install firefox")
            sys.exit(1)
        else:
            firefox_webdriver.get(html_source)

        if parsed_args.delay:
            time.sleep(parsed_args.delay)

        # parse the page and build a digraph for each code tag
        lxml_doctree = etree_from_str(firefox_webdriver.page_source)
        target_elements = collect_target_elements(firefox_webdriver, lxml_doctree)

        target_graphs = []
        with Bar('constructing graphs', max=len(target_elements)) as prog_bar:
            for elt in target_elements:
                target_graphs.append(build_codelt_graph(firefox_webdriver, lxml_doctree, elt))
                prog_bar.next()

        # build concretized source content and write it to the destination dir
        print(f'computing source from graphs')
        html_content, css_content = build_document(target_graphs, css_outpath.name)
        firefox_webdriver.close()

        html_outpath.write_text(html_content)
        css_outpath.write_text(css_content)
        print(f'source written to {html_outpath}, {css_outpath}')
