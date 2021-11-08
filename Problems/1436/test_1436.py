import io
from ans_1436 import *


def test_666_1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("3\n"))
    solve()
    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out == "2666\n"


def test_666_2(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("7\n"))
    solve()
    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out == "6660\n"


def test_666_3(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("187\n"))
    solve()
    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out == "66666\n"
