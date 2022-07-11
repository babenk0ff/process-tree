from tree import Node


def print_node_tree(node: Node, search_pid: int, level: int = 0) -> None:
    """Выводит на экран древо вызовов, выделяя процесс с заданным PID"""
    if node.pid == search_pid:
        print('{}{}{} (PID: {}){}'
              .format('\033[92m', '\t' * level, node.exe, node.pid, '\033[0m'))
    else:
        print('{}{} (PID: {})'.format('\t' * level, node.exe, node.pid))

    for child in node.children:
        print_node_tree(child, search_pid, level + 1)
