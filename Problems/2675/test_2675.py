import io
from ans_2675 import solve


def test_iter1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("3\n3 abc\n2 a/x\n4 aaa"))
    solve()
    outDat = capsys.readouterr()
    assert outDat.out == "aaabbbccc\naa//xx\naaaaaaaaaaaa\n"
