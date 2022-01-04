import io
from ans_11047 import solve


def test_coins1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("5 108\n1\n5\n10\n20\n30\n"))
    solve()
    outcap = capsys.readouterr()
    assert outcap.out == "8\n"


def test_coins2(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("1 100000000\n1\n"))
    solve()
    outcap = capsys.readouterr()
    assert outcap.out == "100000000\n"
