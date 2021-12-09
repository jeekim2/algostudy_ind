from ans_1002_JHP import *
import io


def test_case1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("1\n0 0 13 40 0 37\n"))
    solve()
    captured = capsys.readouterr()
    assert captured.out == "2\n"

def test_case2(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("1\n0 0 3 0 7 4\n"))
    solve()
    captured = capsys.readouterr()
    assert captured.out == "1\n"

def test_case3(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("1\n1 1 1 1 1 5\n"))
    solve()
    captured = capsys.readouterr()
    assert captured.out == "0\n"

def test_case4(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("1\n2 2 2 2 2 2\n"))
    solve()
    captured = capsys.readouterr()
    assert captured.out == "-1\n"
