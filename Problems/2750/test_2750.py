#https://www.acmicpc.net/problem/2750
from ans_2750 import *
import io
"""
1. import mock 사용
 - 문제 : Import "mock" could not be resolved from sourcePylance 에러 발생
 - 원인 : path 인식 문제 같은데.. 해결책 잘 모르겠음..검색해도 모르겠음...
2. import io 사용
 - 배경 : 사용자 입력 데이터에 대한 pytest 수행을 위해 monkeypatch 모듈 사용
   * Monkeypatching : 런타임에 소프트웨어(예: 모듈, 개체, 메서드 또는 기능)를 동적으로 변경하는 것. 
   특히 외부 API 또는 라이브러리를 사용할 때 버그 수정 또는 프로토타이핑 소프트웨어에 자주 사용.
 - 참조 : 지환이형 풀이 test_2675 참조
 - 문제 : capsys.readouterr를 포함한 monkeypatch 문법 이해가 잘 안됨...ㅠ  
"""

def test_solve(monkeypatch, capsys):
        monkeypatch.setattr("sys.stdin",io.StringIO("5\n1\n3\n5\n2\n4"))
        solve()
        outDat = capsys.readouterr()
        assert outDat.out == "[1, 2, 3, 4, 5]"