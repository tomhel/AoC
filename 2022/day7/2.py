from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Command:
    cmd: str
    arg: str = None
    output: list = field(default_factory=list)


@dataclass
class FSNode:
    type: str
    name: str
    size: int = 0
    parent: "FSNode" = None
    children: Dict[str, "FSNode"] = field(default_factory=dict)


def load():
    with open("input") as f:
        cmd = None
        for line in map(lambda x: x.strip().split(), f):
            if line[0] == "$":  # command
                if cmd:
                    yield cmd
                cmd = Command(*line[1:])
            else:  # directory or file
                cmd.output.append(line)
        yield cmd


def build_structure(commands, i, node):
    if i < len(commands):
        if commands[i].cmd == "ls":
            for attr, name in commands[i].output:
                if attr == "dir":
                    node.children[name] = FSNode(type="d", name=name, parent=node)
                else:  # file
                    node.children[name] = FSNode(type="f", name=name, size=int(attr), parent=node)
            build_structure(commands, i+1, node)
        elif commands[i].cmd == "cd" and commands[i].arg == "..":
            build_structure(commands, i+1, node.parent)
        else:  # cd <some dir>
            build_structure(commands, i+1, node.children[commands[i].arg])
    return node


def get_dir_size(node, result):
    size = sum(n.size if n.type == "f" else get_dir_size(n, result) for n in node.children.values())
    if node.type == "d":
        result.append(size)
    return size


def find_smallest_delete_candidate():
    commands, dir_sizes = list(load()), []
    root = build_structure(commands, 1, FSNode(type="d", name="/"))
    used_size = get_dir_size(root, dir_sizes)
    return min(filter(lambda x: 70000000 - used_size + x >= 30000000, dir_sizes))


print(find_smallest_delete_candidate())
