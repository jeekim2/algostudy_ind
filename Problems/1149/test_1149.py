import io
from ans_1149 import solve


def test_paint_1(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.stdin",
        io.StringIO(
            "3\n \
            26 40 83\n \
            49 60 57\n \
            13 89 99\n"
        ),
    )
    solve()
    capture = capsys.readouterr()
    assert capture.out == "96\n"


def test_paint_2(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.stdin",
        io.StringIO(
            "6\n \
            30 19 5\n \
            64 77 64\n \
            15 19 97\n \
            4 71 57\n \
            90 86 84\n \
            93 32 91\n"
        ),
    )
    solve()
    capture = capsys.readouterr()
    assert capture.out == "208\n"


def test_paint_3(monkeypatch, capsys):
    # greedy로 풀 경우 만족 불가 case
    monkeypatch.setattr(
        "sys.stdin",
        io.StringIO(
            "8\n \
            71 39 44\n \
            32 83 55\n \
            51 37 63\n \
            89 29 100\n \
            83 58 11\n \
            65 13 15\n \
            47 25 29\n \
            60 66 19\n"
        ),
    )
    solve()
    capture = capsys.readouterr()
    assert capture.out == "253\n"
