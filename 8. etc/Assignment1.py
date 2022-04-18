import random

"""
    1. 랜덤 조합
    다음의 기능을 수행하는 함수 mix_members 를 Python 소스코드로 작성하세요
    상황:
    사내의 팀원들 전체를 대상으로 랜덤한 조를 구성하려고 합니다. 한 조는 최소 5명, 최대 7명으로
    구성하고, 조의 개수는 최소화해야 합니다.
    상황 상세 및 조건:
    1. 제공하는 members 리스트에는 각 member의 이름이 담고있습니다.
    2. members 리스트의 길이는 10 이상 100 이하 입니다.
    3. 한 조는 최소 5명, 최대 7명으로 구성합니다.
    4. 생성하는 조의 개수를 최소화합니다.
    a. 70명의 팀원으로 10개 조를 구성해야 합니다. (14개조 x)
    5. output은 아래와 같은 형태를 따릅니다.
    a. 1조, 2조, 3조... 순으로 조의 이름을 지정합니다.
    b. {‘1조': [‘김수한무', ’거북이', ‘두루미'...], ‘2조': [‘배트맨', ‘슈퍼맨', ‘엑스맨' ...]...}
    6. 동일한 members 를 넣었을 때도 매번 랜덤한 결과를 내어 놓아야 합니다.
    7. 함수 실행시 결과값을 Amazon EC2 t2.micro 기준 1.5초 이내에 제공해야 합니다.
    Input
    - members (list[String])
    ex) [ ‘김수한무', ’거북이', ‘두루미', ‘배트맨’, ‘슈퍼맨’, ‘엑스맨’, ‘젠틀맨’... ]
    Output
    - python Dictionary 형태
    ex) {‘1조': [‘김수한무', ’거북이', ‘두루미'...], ‘2조': [‘배트맨', ‘슈퍼맨', ‘엑스맨' ...]...}
"""


# 딕셔너리 가공 및 출력
def set_dict1(divide_, list_):
    global members
    length = len(list_)
    index = random.randrange(0, length)
    list_ = list(list_)
    result = []
    for x in list_:
        tmp = [7] * divide_
        for y in x:
            tmp.append(y)

        result.append(tmp)
    result = result[index]
    random.shuffle(result)
    dict_ = {}
    order = 0
    start_ = 0

    for i in result:
        order += 1

        tmp_list = members[start_:start_ + i]
        start_ += i
        dict_.setdefault(f'{order}조', tmp_list)

    return dict_


# 줄어든 범위를 토대로 DFS 수행
def rec(level, list_, remain):
    global min_, group_list

    if remain < 0:
        return
    if remain == 0:
        # 가장 작은길이 = 최소 선택횟수, 배열 초기화
        if min_ > level:
            min_ = level
            group_list.clear()

        # 가장 최저길이를 만족하는 배열만 등록.
        if min_ == level:
            list_.sort()

            group_list.add(tuple(list_))

        return

    for step in (7, 6, 5):

        next_ = remain - step
        if 0 < next_ < step or next_ < 0:
            continue
        tmp = list(list_)
        tmp.append(step)
        rec(level + 1, tmp, next_)


def mix_members1(list_):
    global divide
    remain = len(list_)
    max_unit = 7
    min_unit = 5

    if remain < min_unit:
        print('불가')
        return

    k = remain // max_unit
    if k > 3:
        divide = k - 3
        remain -= (max_unit * divide)

    rec(0, [], remain)

    return set_dict1(divide, group_list)


if __name__ == '__main__':
    group_list = set()
    divide = 0
    min_ = 999              # DFS에서 비교값으로 사용.
    num = 100               # TODO 멤버의 수
    # 테스트에 사용할 배열 생성
    members = list(range(num))
    print(mix_members1(members))
    # 작업 코드
