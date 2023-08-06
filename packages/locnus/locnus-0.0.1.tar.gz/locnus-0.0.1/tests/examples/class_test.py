import pytest

from .misc import add_numbers


class TestFirst:
    @staticmethod
    def assert_equal(actual, expected, message=None):
        __tracebackhide__ = True
        if actual != expected:
            pytest.fail(message or f"Expected {expected}, but got {actual}")

    def test_add_numbers(self):
        x, y = 3, 4
        result = add_numbers(x, y)
        self.assert_equal(result, 7, "add_numbers failed")

    # def test_concat_strings(self):
    #     a, b = "hello ", "cruel world"
    #     result = concat_strings(a, b)
    #     self.assert_equal(result, "hello world", "concat_strings failed")
