from binarytree import Node

LBRACE = "⟨"
RBRACE = "⟩"
SEP = ","

OUTPUT_LEAF_REPRESENTATION = LBRACE + RBRACE


class MalformedSyntaxError(RuntimeError):
    pass


def _get_groups(tree_syntax: str):
    level = 0
    groups = [[1]]
    i = None
    for i, char in enumerate(tree_syntax):
        if char == LBRACE:
            level += 1
        elif char == RBRACE:
            level -= 1
        if level == 1 and char == SEP:
            groups[-1].append(i)
            groups.append([i + 1])
    if i is None:
        raise MalformedSyntaxError(
            "Parser reached a point where a subtree or element was empty."
        )
    groups[-1].append(i)

    if level:
        raise MalformedSyntaxError(
            "Following syntax group failed to match outer angle brackets"
            + f" '{tree_syntax}'."
        )
    if len(groups) != 3:
        raise MalformedSyntaxError(
            f"Following syntax group did not have did not have three elements but instead {len(groups)}"
            + f" '{tree_syntax}'."
        )
    return [tree_syntax[start:end].strip() for start, end in groups]


def _is_leaf(tree_syntax: str) -> bool:
    return "".join(tree_syntax.split()) == LBRACE + RBRACE


def parse_graph(tree_syntax: str):
    if _is_leaf(tree_syntax):
        return Node(OUTPUT_LEAF_REPRESENTATION)
    left_syntax, value, right_syntax = _get_groups(tree_syntax)
    node = Node(value)
    node.left = parse_graph(left_syntax)
    node.right = parse_graph(right_syntax)
    return node
