import io
from ans_2580_JHK import solve
from ans_2580_JHK_Fail import solve as solve_fail


def test_sudoku_1(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.stdin",
        io.StringIO(
            "0 3 5 4 6 9 2 7 8\n"
            + "7 8 2 1 0 5 6 0 9\n"
            + "0 6 0 2 7 8 1 3 5\n"
            + "3 2 1 0 4 6 8 9 7\n"
            + "8 0 4 9 1 3 5 0 6\n"
            + "5 9 6 8 2 0 4 1 3\n"
            + "9 1 7 6 5 2 0 8 0\n"
            + "6 0 3 7 0 1 9 5 2\n"
            + "2 5 8 3 9 4 7 6 0\n"
        ),
    )
    solve()
    capture = capsys.readouterr()
    assert (
        capture.out
        == "1 3 5 4 6 9 2 7 8\n"
        + "7 8 2 1 3 5 6 4 9\n"
        + "4 6 9 2 7 8 1 3 5\n"
        + "3 2 1 5 4 6 8 9 7\n"
        + "8 7 4 9 1 3 5 2 6\n"
        + "5 9 6 8 2 7 4 1 3\n"
        + "9 1 7 6 5 2 3 8 4\n"
        + "6 4 3 7 8 1 9 5 2\n"
        + "2 5 8 3 9 4 7 6 1\n"
    )


def test_sudoku_2(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.stdin",
        io.StringIO(
            "0 0 0 0 0 0 0 0 0\n"
            + "7 8 2 1 0 5 6 0 9\n"
            + "0 6 0 2 7 8 1 3 5\n"
            + "3 2 1 0 4 6 8 9 7\n"
            + "8 0 4 9 1 3 5 0 6\n"
            + "5 9 6 8 2 0 4 1 3\n"
            + "9 1 7 6 5 2 0 8 0\n"
            + "6 0 3 7 0 1 9 5 2\n"
            + "2 5 8 3 9 4 7 6 0\n"
        ),
    )
    solve()
    capture = capsys.readouterr()
    assert (
        capture.out
        == "1 3 5 4 6 9 2 7 8\n"
        + "7 8 2 1 3 5 6 4 9\n"
        + "4 6 9 2 7 8 1 3 5\n"
        + "3 2 1 5 4 6 8 9 7\n"
        + "8 7 4 9 1 3 5 2 6\n"
        + "5 9 6 8 2 7 4 1 3\n"
        + "9 1 7 6 5 2 3 8 4\n"
        + "6 4 3 7 8 1 9 5 2\n"
        + "2 5 8 3 9 4 7 6 1\n"
    )


def test_sudoku_1_Fail(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.stdin",
        io.StringIO(
            "0 3 5 4 6 9 2 7 8\n"
            + "7 8 2 1 0 5 6 0 9\n"
            + "0 6 0 2 7 8 1 3 5\n"
            + "3 2 1 0 4 6 8 9 7\n"
            + "8 0 4 9 1 3 5 0 6\n"
            + "5 9 6 8 2 0 4 1 3\n"
            + "9 1 7 6 5 2 0 8 0\n"
            + "6 0 3 7 0 1 9 5 2\n"
            + "2 5 8 3 9 4 7 6 0\n"
        ),
    )
    solve_fail()
    capture = capsys.readouterr()
    assert (
        capture.out
        == "1 3 5 4 6 9 2 7 8\n"
        + "7 8 2 1 3 5 6 4 9\n"
        + "4 6 9 2 7 8 1 3 5\n"
        + "3 2 1 5 4 6 8 9 7\n"
        + "8 7 4 9 1 3 5 2 6\n"
        + "5 9 6 8 2 7 4 1 3\n"
        + "9 1 7 6 5 2 3 8 4\n"
        + "6 4 3 7 8 1 9 5 2\n"
        + "2 5 8 3 9 4 7 6 1\n"
    )


def test_sudoku_2_Fail(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.stdin",
        io.StringIO(
            "0 0 0 0 0 0 0 0 0\n"
            + "7 8 2 1 0 5 6 0 9\n"
            + "0 6 0 2 7 8 1 3 5\n"
            + "3 2 1 0 4 6 8 9 7\n"
            + "8 0 4 9 1 3 5 0 6\n"
            + "5 9 6 8 2 0 4 1 3\n"
            + "9 1 7 6 5 2 0 8 0\n"
            + "6 0 3 7 0 1 9 5 2\n"
            + "2 5 8 3 9 4 7 6 0\n"
        ),
    )
    solve_fail()
    capture = capsys.readouterr()
    assert (
        capture.out
        == "1 3 5 4 6 9 2 7 8\n"
        + "7 8 2 1 3 5 6 4 9\n"
        + "4 6 9 2 7 8 1 3 5\n"
        + "3 2 1 5 4 6 8 9 7\n"
        + "8 7 4 9 1 3 5 2 6\n"
        + "5 9 6 8 2 7 4 1 3\n"
        + "9 1 7 6 5 2 3 8 4\n"
        + "6 4 3 7 8 1 9 5 2\n"
        + "2 5 8 3 9 4 7 6 1\n"
    )
