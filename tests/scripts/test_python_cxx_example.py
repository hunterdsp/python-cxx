
def test_script():
    """Test successful execution."""

    from subprocess import check_call

    assert check_call([
        'bash', '-c', 'uv run', '--no-editable', 'python-cxx-example',])