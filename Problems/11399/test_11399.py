import io
from ans_11399 import solve


def test_ATM1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("5\n3 1 4 3 2\n"))
    solve()
    outst = capsys.readouterr()
    assert outst.out == "32\n"
