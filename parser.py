from typing import NamedTuple


class Call(NamedTuple):
    pid: int
    exe: str
    parent_pid: int
    parent_exe: str


def parse_csv(file_path: str) -> list[Call]:
    """Парсит csv, возвращает список объектов типа Call."""
    with open(file_path, 'r', encoding='utf-8') as file:
        result_list = []
        for line in file.readlines()[1:]:
            line_list = line.strip().replace('"', '').split(';')[1:]
            result_list.append(Call(
                pid=int(line_list[0]),
                exe=''.join(line_list[1:3]),
                parent_pid=int(line_list[3]),
                parent_exe=''.join(line_list[4:6])
            ))
    return result_list
