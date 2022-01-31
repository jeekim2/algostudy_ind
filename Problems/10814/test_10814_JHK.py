import io
from ans_10814_JHK import solve


def test_10814_1(monkeypatch, capsys):
    inData = "3\n" + "21 Junkyu\n" + "21 Dohyun\n" + "20 Sunyoung\n"
    outData = "20 Sunyoung\n" + "21 Junkyu\n" + "21 Dohyun\n"

    monkeypatch.setattr("sys.stdin", io.StringIO(inData))
    solve()
    capture = capsys.readouterr()
    assert capture.out == outData


def test_10814_2(monkeypatch, capsys):
    inData = "4\n" + "1 B\n" + "1 C\n" + "1 A\n" + "1 Z\n"
    outData = "1 B\n" + "1 C\n" + "1 A\n" + "1 Z\n"

    monkeypatch.setattr("sys.stdin", io.StringIO(inData))
    solve()
    capture = capsys.readouterr()
    assert capture.out == outData
