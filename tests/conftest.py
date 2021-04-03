import pytest


@pytest.fixture()
def complex_f_string():
    return "f'there is {calculate_square_root(16)}'"


@pytest.fixture()
def another_complex_f_string():  # FIXME: make through parametrize
    return "f'there is {calculate_square_root(your_number)}'"


@pytest.fixture()
def another_one_complex_f_string():  # FIXME: make through parametrize
    return "f'there is {calculate_square_root(calculate_square_root(your_number))}'"


@pytest.fixture()
def allowed_f_string():
    return "f'there is {number}'"


