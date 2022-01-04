import io
from ans_13305 import solve


def test_oilcost1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("4\n2 3 1\n5 2 4 1\n"))
    solve()
    outst = capsys.readouterr()
    assert outst.out == "18\n"


def test_oilcost2(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("4\n3 3 4\n1 1 1 1\n"))
    solve()
    outst = capsys.readouterr()
    assert outst.out == "10\n"
