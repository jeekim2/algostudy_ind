import io
from ans_1780 import solve


def strcat(sorg, s2):
    if sorg[-1:] != "\n":
        sorg += "\n"
    if s2[-1:] != "\n":
        s2 += "\n"
    sorg += s2
    return sorg


def test_paper1(monkeypatch, capsys):
    sss = strcat("3", "1 1 1")
    sss = strcat(sss, "1 1 1")
    sss = strcat(sss, "1 1 1")

    monkeypatch.setattr("sys.stdin", io.StringIO(sss))
    solve()
    tOut = capsys.readouterr()
    assert tOut.out == "0\n0\n1\n"


def test_paper2(monkeypatch, capsys):
    sss = strcat("9", "1 1 1 0 0 0 -1 -1 -1")
    sss = strcat(sss, "1 1 1 0 0 0 -1 -1 -1")
    sss = strcat(sss, "1 1 1 0 0 0 -1 -1 -1")

    sss = strcat(sss, "1 1 1 0 0 0 -1 -1 -1")
    sss = strcat(sss, "1 1 1 0 1 0 -1 -1 -1")
    sss = strcat(sss, "1 1 -1 0 0 0 -1 -1 -1")

    sss = strcat(sss, "1 1 1 0 0 0 -1 -1 -1")
    sss = strcat(sss, "1 1 1 0 0 0 -1 -1 -1")
    sss = strcat(sss, "1 1 1 0 0 0 -1 -1 0")

    monkeypatch.setattr("sys.stdin", io.StringIO(sss))
    solve()
    tOut = capsys.readouterr()
    assert tOut.out == "11\n11\n11\n"
