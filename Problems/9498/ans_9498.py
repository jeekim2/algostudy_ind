# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 
# 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

# 입력 -첫 째 줄에 시험 점수가 주어진다. 
# 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

def report():
    # (1) 입력
    score_report = int(input())

    # (2) 조건 판단 및 출력
    if (score_report < 0) or (score_report > 100):
        print("not correct score")
    elif 90 <= score_report <= 100:
        print("A")
    elif 80 <= score_report < 90:
        print("B")
    elif 70 <= score_report < 80:
        print("C")
    elif 60 <= score_report < 70:
        print("D")
    else:
        print("F")
    
if __name__ == "__main__":
    report()