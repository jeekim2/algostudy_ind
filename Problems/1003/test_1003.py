import io
from ans_1003 import solve


def test_fibo1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("3\n1\n2\n3\n"))
    solve()
    outst = capsys.readouterr()
    assert outst.out == "0 1\n1 1\n1 2\n"


def test_fibo2(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("1\n4"))
    solve()
    outst = capsys.readouterr()
    assert outst.out == "2 3\n"


def test_fibo3(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("1\n5"))
    solve()
    outst = capsys.readouterr()
    assert outst.out == "3 5\n"
