import random


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
