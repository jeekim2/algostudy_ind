# from _pytest.monkeypatch import monkeypatch
# from _pytest.capture import capsys
from ans_1018 import *
import io


def test_chessboard1(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.stdin",
        io.StringIO(
            "8 8\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBBBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\n"
        ),
    )
    solve()
    gg = capsys.readouterr()
    assert gg.out == "1\n"


def test_chessboard2(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.stdin",
        io.StringIO(
            "10 13\nBBBBBBBBWBWBW\nBBBBBBBBBWBWB\nBBBBBBBBWBWBW\nBBBBBBBBBWBWB\nBBBBBBBBWBWBW\nBBBBBBBBBWBWB\nBBBBBBBBWBWBW\nBBBBBBBBBWBWB\nWWWWWWWWWWBWB\nWWWWWWWWWWBWB\n"
        ),
    )
    solve()
    gg = capsys.readouterr()
    assert gg.out == "12\n"
