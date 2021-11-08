import io
from ans_15650 import *


def test_NandM2_1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("8 3\n"))
    solve()
    sOut = capsys.readouterr()
    assert (
        sOut.out
        == "1 2 3 \n1 2 4 \n1 2 5 \n1 2 6 \n1 2 7 \n1 2 8 \n1 3 4 \n1 3 5 \n1 3 6 \n1 3 7 \n1 3 8 \n1 4 5 \n1 4 6 \n1 4 7 \n1 4 8 \n1 5 6 \n1 5 7 \n1 5 8 \n1 6 7 \n1 6 8 \n1 7 8 \n2 3 4 \n2 3 5 \n2 3 6 \n2 3 7 \n2 3 8 \n2 4 5 \n2 4 6 \n2 4 7 \n2 4 8 \n2 5 6 \n2 5 7 \n2 5 8 \n2 6 7 \n2 6 8 \n2 7 8 \n3 4 5 \n3 4 6 \n3 4 7 \n3 4 8 \n3 5 6 \n3 5 7 \n3 5 8 \n3 6 7 \n3 6 8 \n3 7 8 \n4 5 6 \n4 5 7 \n4 5 8 \n4 6 7 \n4 6 8 \n4 7 8 \n5 6 7 \n5 6 8 \n5 7 8 \n6 7 8 \n"
    )
