import io
from ans_10809 import *


def test_OpInsert_1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("baekjoon\n"))
    solve()
    capture = capsys.readouterr()
    assert (
        capture.out
        == "[1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1]\n"
    )


def test_OpInsert_1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("jaehyun\n"))
    solve()
    capture = capsys.readouterr()
    assert (
        capture.out
        == "[1, -1, -1, -1, 2, -1, -1, 3, -1, 0, -1, -1, -1, 6, -1, -1, -1, -1, -1, -1, 5, -1, -1, -1, 4, -1]\n"
    )
