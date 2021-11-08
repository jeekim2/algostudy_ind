from ans_1065 import *
import io


def test_hansu1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("100\n"))
    solve()
    captured = capsys.readouterr()
    assert captured.out == "99\n"


def test_hansu2(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("500\n"))
    solve()
    captured = capsys.readouterr()
    assert captured.out == "119\n"


def test_hansu3(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("1000\n"))
    solve()
    captured = capsys.readouterr()
    assert captured.out == "144\n"


def test_hansu4(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("210\n"))
    solve()
    captured = capsys.readouterr()
    assert captured.out == "105\n"
