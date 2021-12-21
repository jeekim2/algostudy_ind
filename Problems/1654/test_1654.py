import io
from ans_1654 import solve


def test_lancut1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("4 11\n802\n743\n457\n539\n"))
    solve()
    capture = capsys.readouterr()
    assert capture.out == "200\n"


def test_lancut2(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("1 11\n111\n"))
    solve()
    capture = capsys.readouterr()
    assert capture.out == "10\n"


def test_lancut3(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("2 11\n50\n60\n"))
    solve()
    capture = capsys.readouterr()
    assert capture.out == "10\n"


def test_lancut4(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("2 11\n50\n59\n"))
    solve()
    capture = capsys.readouterr()
    assert capture.out == "9\n"


def test_lancut5(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("3 3\n2\n1\n1\n"))
    solve()
    capture = capsys.readouterr()
    assert capture.out == "1\n"


def test_lancut6(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("3 3\n6\n1\n1\n"))
    solve()
    capture = capsys.readouterr()
    assert capture.out == "2\n"


def test_lancut7(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("3 9\n6\n1\n1\n"))
    solve()
    capture = capsys.readouterr()
    assert capture.out == "0\n"


def test_lancut8(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("3 1\n6\n2\n1\n"))
    solve()
    capture = capsys.readouterr()
    assert capture.out == "6\n"
