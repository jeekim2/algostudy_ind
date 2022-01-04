import io
from ans_1316 import solve


def test_groupword_1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("1\n" "z\n"))
    solve()
    capture = capsys.readouterr()
    assert capture.out == "1\n"


def test_groupword_2(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.stdin",
        io.StringIO("3\n" "happy\n" "new\n" "year\n"),
    )
    solve()
    capture = capsys.readouterr()
    assert capture.out == "3\n"


def test_groupword_3(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.stdin",
        io.StringIO("1\n" "aaaaa\n"),
    )
    solve()
    capture = capsys.readouterr()
    assert capture.out == "1\n"
