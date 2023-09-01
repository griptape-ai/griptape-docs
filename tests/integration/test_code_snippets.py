import io
import pathlib
import pytest

from mktestdocs import check_md_file

# Note the use of `str`, makes for pretty output
@pytest.mark.parametrize('fpath', pathlib.Path("docs").glob("**/*.md"), ids=str)
def test_files_good(fpath, monkeypatch):
    # Send some stdin for tests that use the Chat util
    monkeypatch.setattr('sys.stdin', io.StringIO('Hi\nexit\n'))
    
    # This example requres creating a directory outside of code
    if str(fpath) == 'docs/griptape-tools/custom-tools/index.md':
        with pytest.raises(ModuleNotFoundError):
            check_md_file(fpath=fpath)
    # This example requres docker running 
    # elif str(fpath) == 'docs/griptape-tools/official-tools/computer.md':
    #     with pytest.raises(ValueError):
    #         check_md_file(fpath=fpath)
        
    else:
        check_md_file(fpath=fpath)
