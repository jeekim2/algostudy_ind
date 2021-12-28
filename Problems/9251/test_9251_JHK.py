import io
from ans_9251_JHK import solve


def test_LCS_1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("ACAYKP\n" + "CAPCAK\n"))
    solve()
    capture = capsys.readouterr()
    assert capture.out == "4\n"


def test_LCS_2(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("ABCCBEASEWAD\n" + "ABWADEASED\n"))
    solve()
    capture = capsys.readouterr()
    assert capture.out == "7\n"
