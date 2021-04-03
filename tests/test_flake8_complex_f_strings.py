import ast
from typing import Set

from flake8_complex_f_strings import Plugin


def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col} {msg}' for line, col, msg, _ in plugin.run()}


def test_incorrect_f_strings(complex_f_string):
    assert _results(complex_f_string) == {'1:0 FCS100 too complex f-string'}


def test_another_incorrect_f_strings(another_complex_f_string):
    assert (
        _results(another_complex_f_string) ==
        {'1:0 FCS100 too complex f-string'}
    )

def test_another_one_incorrect_f_strings(another_one_complex_f_string):
    assert (
        _results(another_one_complex_f_string) ==
        {'1:0 FCS100 too complex f-string'}
    )


def test_allowed_f_strings(allowed_f_string):
    assert _results(allowed_f_string) == set()
