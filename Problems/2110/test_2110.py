import io
from ans_2110 import solve


def test_wifi_1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("5 3\n1\n2\n8\n4\n9\n"))
    solve()
    capture = capsys.readouterr()
    assert capture.out == "3\n"


def test_wifi_2(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("8 4\n1\n2\n3\n5\n6\n7\n9\n13\n"))
    solve()
    capture = capsys.readouterr()
    assert capture.out == "4\n"


def test_wifi_3(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("6 4\n1\n6\n7\n9\n10\n11\n"))
    solve()
    capture = capsys.readouterr()
    assert capture.out == "2\n"
