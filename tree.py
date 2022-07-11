from dataclasses import dataclass, field

from parser import Call


@dataclass
class Node:
    pid: int
    exe: str
    children: list = field(default_factory=list)


def _if_root(sample: Call, calls_list: list[Call]) -> bool:
    for call in calls_list:
        if sample.parent_pid == call.pid and sample.parent_exe == call.exe:
            return False
    return True


def search_roots(calls_list: list[Call]) -> list[Node]:
    """В списке вызовов (типа Call) ищет процессы, являющиеися корневыми,
    и возвращает новый их список."""
    root_list = []
    for call in calls_list:
        if _if_root(call, calls_list):
            node = Node(pid=call.parent_pid, exe=call.parent_exe)
            if node not in root_list:
                root_list.append(node)
    return root_list


def _get_children(node: Node, calls_list: list[Call]) -> list[Node]:
    children_list = []
    for call in calls_list:
        if call.parent_pid == node.pid and call.parent_exe == node.exe:
            children_list.append(Node(pid=call[0], exe=call[1]))
    return children_list


def _get_children_tree(
        node: Node,
        calls_list: list[Call],
        search_pid: int,
        found: bool = False) -> tuple[list[Node], bool]:

    if node.pid == search_pid:
        found = True

    node_children = _get_children(node, calls_list)
    for child in node_children:
        children_list, found = _get_children_tree(child, calls_list, search_pid, found)
        child.children = children_list

    return node_children, found


def build_node_list(
        roots_list: list[Node],
        calls_list: list[Call],
        search_pid: int) -> list[Node]:
    """Возвращает список объектов типа Node, в дочерних процессах которых найден
    процесс с PID, совпадающий с заданным"""

    result_list = []
    for root in roots_list:
        children, found = _get_children_tree(root, calls_list, search_pid)
        if found:
            root.children = children
            result_list.append(root)

    return result_list
