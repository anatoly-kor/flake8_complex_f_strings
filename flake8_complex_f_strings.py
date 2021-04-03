import ast
import sys
from typing import Generator, Tuple, Type, Any, List

if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.issues: List[Tuple[int, int]] = []

    def visit_FormattedValue(self, node: ast.FormattedValue) -> None:
        if (
            isinstance(node.value, ast.Call) and
            (
                all(isinstance(arg, ast.Constant) for arg in node.value.args)
                or
                all(isinstance(arg, ast.Name) for arg in node.value.args)
                or
                all(isinstance(arg, ast.Call) for arg in node.value.args)
            )
        ):
            self.issues.append((node.lineno, node.col_offset))
        self.generic_visit(node)


class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)
        for line, col in visitor.issues:
            yield line, col, 'FCS100 too complex f-string', type(self)
