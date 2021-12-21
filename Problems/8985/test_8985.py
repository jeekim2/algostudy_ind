import io
from ans_8985 import *


def test_OpInsert_1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("5\nOOXXOXXOOO\nOOXXOOXXOO\nOXOXOXOXOXOXOX\nOOOOOOOOOO\nOOOOXOOOOXOOOOX\n"))
    score_result()
    capture = capsys.readouterr()
    assert (
        capture.out
        == "10\n9\n7\n55\n30\n"
    )


def test_OpInsert_2(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("7\nOOOOOOOOOX\nXOOOOOOOOO\nOXOOOOOOOO\nOOOOOOOOXO\nXXXXXXXXXX\nXXXXXXXXXO\nXOXOXOXOXO\n"))
    score_result()
    capture = capsys.readouterr()
    assert (
        capture.out
        == "45\n45\n37\n37\n30\n0\n1\n5\n"
    )
