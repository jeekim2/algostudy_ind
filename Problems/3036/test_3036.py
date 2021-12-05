import io
from ans_3036 import solve


def test_circles1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("3\n8 4 2\n"))
    solve()
    cap = capsys.readouterr()
    assert cap.out == "2/1\n4/1\n"


def test_circles2(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("3\n11 4 2\n"))
    solve()
    cap = capsys.readouterr()
    assert cap.out == "11/4\n11/2\n"
