from ans_1546 import *
import io


def test_average1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("3\n10 20 30\n"))
    solve()
    captured = capsys.readouterr()
    assert captured.out == "66.66666666666667\n"


def test_average2(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("2\n20 40\n"))
    solve()
    captured = capsys.readouterr()
    assert captured.out == "75.0\n"
