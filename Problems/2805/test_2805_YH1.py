#https://www.acmicpc.net/problem/2805
from ans_2805_YH1 import *
import io

def test_solve1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("5 20\n4 42 40 26 46\n"))
    solve()
    cap = capsys.readouterr()
    assert cap.out == "36\n"
    
def test_solve2(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("4 7\n20 15 10 17\n"))
    solve()
    cap = capsys.readouterr()
    assert cap.out == "15\n"
    
def test_solve3(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("5 27\n37 27 46 52 16\n"))
    solve()
    cap = capsys.readouterr()
    assert cap.out == "36\n"
    
def test_solve4(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("5 13\n1 1 1 1 60\n"))
    solve()
    cap = capsys.readouterr()
    assert cap.out == "47\n"

def test_solve5(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("3 3\n10 10 10\n"))
    solve()
    cap = capsys.readouterr()
    assert cap.out == "9\n"

def test_solve6(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("3 5\n2 3 7\n"))
    solve()
    cap = capsys.readouterr()
    assert cap.out == "2\n"