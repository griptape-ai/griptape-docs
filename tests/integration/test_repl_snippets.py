import doctest
import pathlib
import pytest

# Note the use of `str`, makes for pretty output
@pytest.mark.parametrize('fpath', pathlib.Path("docs").glob("**/*.md"), ids=str)
def test_code_snippets(fpath):
    doctest.testfile('../../' + str(fpath), optionflags=doctest.ELLIPSIS)
