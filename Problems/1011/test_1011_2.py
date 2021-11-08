from ans_1011_2 import *
import io


def test_length1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("3\n1 3\n2 6\n1 8\n"))
    solve()
    captured = capsys.readouterr()
    assert captured.out == "2\n3\n5\n"
