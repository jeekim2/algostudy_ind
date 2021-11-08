from ans_4673 import *


def strcat(*args):
    strsum = ""
    for i in args:
        strsum += str(i) + "\n"
    return strsum


def test_answer1(capsys):
    solve(100)
    # capture(capsys, "hello")
    # capture(capsys, "world")
    captured = capsys.readouterr()
    # assert captured.out == "1\n3\n5\n7\n9\n"
    assert captured.out == strcat(1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97)
