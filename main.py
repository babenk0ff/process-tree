from pathlib import Path

from parser import parse_csv
from printer import print_node_tree
from tree import build_node_list, search_roots
from export import JSONExporter, export


def main():
    file = 'Task_data.csv'
    pid = 11012

    calls_list = parse_csv(file)
    roots_list = search_roots(calls_list)
    node_list = build_node_list(roots_list, calls_list, pid)
    for node in node_list:
        print_node_tree(node, pid)
    export(node_list, JSONExporter(Path.cwd() / 'tree.json'))


if __name__ == '__main__':
    main()
