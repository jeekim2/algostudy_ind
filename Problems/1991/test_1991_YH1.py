import io
from ans_1991_YH1 import *


def test_1991_1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("7\nA B C\nB D .\nC E F\nE . .\nF . G\nD . .\nG . ."))
    solve()
    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out == "ABDCEFG\nDBAECFG\nDBEGFCA\n"