import pytest
from packaging.version import parse

import locnus


@pytest.mark.skipif(parse(locnus.__version__) < parse("0.1"), reason="This test requires locnus.__version__ >= 0.1")
def test_some_function_only_available_in_later_versions():
    print(parse(locnus.__version__))
    assert False
