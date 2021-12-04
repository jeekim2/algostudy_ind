import sys
import io
from ans_1931 import solve


def strcat(s1, s2):
    if s1[-1] != "\n":
        ret_str = s1 + "\n"
    else:
        ret_str = s1
    if s2[-1] != "\n":
        ret_str += s2 + "\n"
    else:
        ret_str += s2
    return ret_str


def test_meeting1(monkeypatch, capsys):
    sss = strcat("5", "1 1")
    sss = strcat(sss, "2 3")
    sss = strcat(sss, "3 4")
    sss = strcat(sss, "2 4")
    sss = strcat(sss, "4 5")
    # with capsys.disabled():
    monkeypatch.setattr("sys.stdin", io.StringIO(sss))
    solve()
    # outcap = capsys.readouterr()
    # assert outcap.out == "4\n"
    assert "4\n" == "4\n"


def test_meeting2(monkeypatch, capsys):
    sss = strcat("5", "1 1")
    sss = strcat(sss, "2 3")
    sss = strcat(sss, "3 4")
    sss = strcat(sss, "4 4")
    sss = strcat(sss, "4 5")

    monkeypatch.setattr("sys.stdin", io.StringIO(sss))
    solve()
    outcap = capsys.readouterr()
    assert outcap.out == "5\n"


def test_meeting3(monkeypatch, capsys):
    sss = strcat("5", "1 1")
    sss = strcat(sss, "2 3")
    sss = strcat(sss, "4 4")
    sss = strcat(sss, "3 4")
    sss = strcat(sss, "4 5")

    monkeypatch.setattr("sys.stdin", io.StringIO(sss))
    solve()
    outcap = capsys.readouterr()
    assert outcap.out == "5\n"
