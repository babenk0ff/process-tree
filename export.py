from __future__ import annotations
from typing import Protocol, TypedDict
from pathlib import Path
import json

from tree import Node


class Exporter(Protocol):
    def export(self, node_list: list[Node]) -> None:
        raise NotImplementedError


class JSONData(TypedDict):
    pid: int
    exe: str
    children: list[JSONData]


class JSONExporter:
    """Экспорт дерева в JSON файл"""

    def __init__(self, file: Path):
        self.file = file

    def _convert_to_dict(self, node: Node) -> JSONData:
        return {
            'pid': node.pid,
            'exe': node.exe,
            'children': [self._convert_to_dict(child) for child in node.children]
        }

    def _write(self, export_list: list[JSONData]) -> None:
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(export_list, fp=f, indent=4)

    def export(self, node_list: list[Node]) -> None:
        export_list = [self._convert_to_dict(node) for node in node_list]
        self._write(export_list)


def export(node_list: list[Node], exporter: Exporter) -> None:
    exporter.export(node_list)
