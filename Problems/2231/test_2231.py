import io
from ans_2231 import solve


def test_sepSum1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("216\n"))
    solve()
    capture = capsys.readouterr()
    assert capture.out == "198\n"


def test_sepSum2(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("2\n"))
    solve()
    capture = capsys.readouterr()
    assert capture.out == "1\n"
    # 착각하기 쉬운 반례 - input이 1 이면 부분합은 1+1=2


def test_sepSum3(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("3\n"))
    solve()
    capture = capsys.readouterr()
    assert capture.out == "0\n"
