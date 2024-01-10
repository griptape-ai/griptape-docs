import io
import pathlib
import pytest
import textwrap


def check_py_string(source):
    """Exec the python source given in a new module namespace

    Does not return anything, but exceptions raised by the source
    will propagate out unmodified
    """
    try:
        exec(source, {"__MODULE__": "__main__"})
    except Exception:
        print(source)
        raise


def check_codeblock(block, lang="python"):
    """
    Cleans the found codeblock and checks if the proglang is correct.

    Returns an empty string if the codeblock is deemed invalid.

    Arguments:
        block: the code block to analyse
        lang: if not None, the language that is assigned to the codeblock
    """
    first_line = block.split("\n")[0]
    if lang:
        if first_line[3:] != lang:
            return ""
    return "\n".join(block.split("\n")[1:])


def grab_code_blocks(docstring, lang="python"):
    """
    Given a docstring, grab all the markdown codeblocks found in docstring.

    Arguments:
        docstring: the docstring to analyse
        lang: if not None, the language that is assigned to the codeblock
    """
    docstring = textwrap.dedent(docstring)
    in_block = False
    block = ""
    codeblocks = []
    for idx, line in enumerate(docstring.split("\n")):
        if line.startswith("```"):
            if in_block:
                codeblocks.append(check_codeblock(block, lang=lang))
                block = ""
            in_block = not in_block
        if in_block:
            block += line + "\n"
    return [c for c in codeblocks if c != ""]


def get_all_code_blocks():
    return [
        {"id": f"{str(fpath)}-{snippet_num}", "code": snippet}
        for fpath in pathlib.Path("docs").glob("**/*.md")
        for snippet_num, snippet in enumerate(grab_code_blocks(fpath.read_text()))
    ]


all_code_blocks = get_all_code_blocks()


@pytest.mark.parametrize(
    "snippet", all_code_blocks, ids=[f["id"] for f in all_code_blocks]
)
def test_code_snippet(snippet, monkeypatch):
    # Send some stdin for tests that use the Chat util
    monkeypatch.setattr("sys.stdin", io.StringIO("Hi\nexit\n"))

    check_py_string(snippet["code"])
