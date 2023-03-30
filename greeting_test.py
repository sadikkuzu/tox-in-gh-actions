from __future__ import annotations

import sys
from unittest.mock import patch

import pytest

import greeting


def test_hello(capsys):
    greeting.hello('github')
    stdout, stderr = capsys.readouterr()
    assert stdout == 'hello github\n'


@pytest.mark.parametrize(
    "given_name, expected_greeting",
    [
        ("pytest", "hello pytest\n"),
        ("tox", "hello tox\n"),
    ],
)
def test_hello_with_parameters(capsys, given_name, expected_greeting):
    greeting.hello(given_name)
    stdout, stderr = capsys.readouterr()
    assert stdout == expected_greeting


def test_parse_args(capsys):
    testargs = ["python", "greeting.py", "John"]
    with patch.object(sys, 'argv', testargs):
        return_main = greeting.main()
        stdout, stderr = capsys.readouterr()
        assert stdout == 'hello John\n'
        assert return_main == 0
