from ans_7568 import *
import io


def test_bigman1(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.stdin", io.StringIO("5\n55 185\n58 183\n88 186\n60 175\n46 155\n")
    )
    solve()
    captured = capsys.readouterr()
    assert captured.out == "2 2 1 2 5"


def test_bigman2(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.stdin", io.StringIO("5\n30 200\n40 300\n60 600\n30 200\n40 100\n")
    )
    solve()
    captured = capsys.readouterr()
    assert captured.out == "3 2 1 3 2"
