"""
sample input:
7
00:10 aaa
00:30 aaa
01:15 bbb
01:00 ccc
01:00 bbb
02:10 aaa
03:10 ccc

sample output:
ccc 19
aaa 16
bbb 13

학생들이 한 달간 통화한 n개의 통화 기록 A가 주어진다. 한 개의 통화 기록은 통화 시간과 학생 이름이 공백으로 구분되어 주어진다. 한 학생의 통화 기록이 여러 번 주어질 수 있다. 통화 시간은 시:분 형태로 주어지고 시와 분은 길이가 2인 문자열이다. 학생 이름은 알파벳 소문자로 이루어져 있다. 통화 요금표는 다음과 같다.

기본 시간(분): 100분, 기본 요금(원): 10, 단위 시간(분): 50, 단위 요금(원): 3
통화 요금은 학생별로 한 달간 통화한 누적 통화 시간에 대하여 청구된다. 누적 통화 시간이 기본 시간 이하라면 기본 요금이 청구된다. 누적 통화 시간이 기본 시간을 초과하면, 기본 요금에 더해서 초과한 시간에 대해서 단위 시간마다 단위 요금이 청구된다. 초과한 시간이 단위 시간으로 나누어떨어지지 않으면 올림 한다.

통화 요금이 많은 학생부터 이름과 통화 요금을 출력하자. 통화 요금이 같은 학생은 학생 이름 기준으로 오름차순으로 출력하자.

"""

cost_dict = {}
n = int(input())
for _ in range(n):
    duration, person = input().split(" ")
    hour, minute = map(int, duration.split(":"))
    print(person, duration, hour, minute)
    minute += hour * 60
    if person in cost_dict.keys():
        cost_dict[person] += minute
    else:
        cost_dict[person] = minute
print(cost_dict)


def process_payment(number):
    res = 10 if number <= 100 else 10 + ((number - 100) // 50) * 3
    # print(f'res is{res}')
    return res


res = [[name, process_payment(bill)] for name, bill in cost_dict.items()]
res.sort(key = lambda x: (x[1], x[0]), reverse= True)
for r in res:
    print(r[0], r[1])