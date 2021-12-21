import io
from ans_1920 import solve


def test_bs1(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.stdin", io.StringIO("6\n1 3 5 7 9 11\n11\n1 2 3 4 5 6 7 8 9 10 11")
    )
    solve()
    capture = capsys.readouterr()
    assert capture.out == "1\n0\n1\n0\n1\n0\n1\n0\n1\n0\n1\n"


def test_bs2(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("6\n1 3 5 7 9 11\n2\n0 12"))
    solve()
    capture = capsys.readouterr()
    assert capture.out == "0\n0\n"


def test_bs3(monkeypatch, capsys):

    monkeypatch.setattr(
        "sys.stdin",
        io.StringIO("7\n1 3 5 7 9 11 13\n13\n1 2 3 4 5 6 7 8 9 10 11 12 13"),
    )
    solve()
    capture = capsys.readouterr()
    assert capture.out == "1\n0\n1\n0\n1\n0\n1\n0\n1\n0\n1\n0\n1\n"


def test_bs4(monkeypatch, capsys):

    monkeypatch.setattr(
        "sys.stdin",
        io.StringIO("8\n1 3 5 7 9 11 13 15\n15\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15"),
    )
    solve()
    capture = capsys.readouterr()
    assert capture.out == "1\n0\n1\n0\n1\n0\n1\n0\n1\n0\n1\n0\n1\n0\n1\n"
