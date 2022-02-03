from __future__ import annotations

import pytest

from greeting import hello


def test_hello(capsys):
    hello('github')
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
    hello(given_name)
    stdout, stderr = capsys.readouterr()
    assert stdout == expected_greeting
