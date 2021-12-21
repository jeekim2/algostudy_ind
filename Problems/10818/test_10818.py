import io
from ans_10818 import *


def test_OpInsert_1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("5\n20 10 35 30 7\n"))
    find_min_max()
    capture = capsys.readouterr()
    assert (
        capture.out
        == "7 35\n"
    )


def test_OpInsert_2(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("9\n-200 140 3500 -30 700 100 -999 1999 6666\n"))
    find_min_max()
    capture = capsys.readouterr()
    assert (
        capture.out
        == "-999 6666\n"
    )
