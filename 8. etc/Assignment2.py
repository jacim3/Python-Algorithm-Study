import random
import numpy as np


"""
# ----------------------------------------------------------------------------------------------------------------------
    * Input
    ['10:00~14:00', '15:00~18:00', '11:00~13:00;14:00~16:00', '10:00~11:00', '15:00~18:00']
    ['11:00~14:00', '14:00~16:00', '16:00~18:00', '10:00~11:00;12:00~13:00', '14:00~16:00']
    ['14:00~16:00', '16:00~18:00', '10:00~12:00', '12:00~14:00', '14:00~16:00']
    ['14:00~18:00', '10:00~18:00', '12:00~14:00', '14:00~15:00;16:00~17:00', '10:00~12:00']
# ----------------------------------------------------------------------------------------------------------------------    
    * OutPut (자유 형식) - 내 풀이. -> 결과는 매번  달라짐
    -1, -1, -2, -2, -3, -3, -4, -4
    -4, -4, -4, -4, -2, -2, -3, -3
    -3, -3, -1, -4, -1, -1, -2, -2
    -2, -5, -3, -3, -4, -5, -5, -5

    * 테이블 출력 설명
    사람 A = -1,
    사람 B = -2,
    사람 C = -3,
    사람 D = -4.
    아무도 불가 = -5
    10시간 초과로 불가 = -6
# ----------------------------------------------------------------------------------------------------------------------
"""

# DFS 를 사용 하여 풀이. 수행시간 제한은 없으므로,
def get_efficient_time(level, count, timetable, remain):
    global min_, table_, hour_unit, days_unit
    # 테이블 루프 돌리기
    # 마지막 도착

    # min_은 시간표 마킹에 실패한 횟수를 기록. DFS에서 하나를 우선적으로 탐색하여 min_이 초기화 되므로,
    # min_값이 설정된 경우, 해당 횟수를 넘어가는 로직은 수행하지 않도록 방지.
    if min_ < count:
        return

    if level == hour_unit * days_unit:
        if min_ > count:
            min_ = count

        # TODO timestable 파라메타를 복사 후 입력해야 올바드게 들어감.
        if count == 6 and min_ == 6:
            tmp = timetable.copy()
            table_.append(tmp)
        return

    skip_count = 0
    is_failed = False
    # i = 사람 인덱스

    # 각각의 사람이 가진 주간 스케쥴을 토대로 차례로 루프
    for i, personal in enumerate(schedule):

        # 해당 사용자가 일을 못함
        if personal[level] == 0:
            skip_count += 1

        # 해당 사람이 일을 할 수 있음.
        else:
            if remain[i] > 0:

                tmp = list(remain)
                timetable[level] = (i + 1) * -1  # 테이블 마킹
                tmp[i] -= 1
                get_efficient_time(level + 1, count, timetable, tmp)
                is_failed = False

            # 해당 사람이 일을 할 수 있으나, 잔여 시간이 없음. -> 루프를 돌면서 모두 체크해야 함. (다음 사람이 일을 할 수도 있음)
            else:
                skip_count += 1
                is_failed = True

        # 일할 수 있는 사람이 아무도 없는 경우
        if skip_count == 4:
            check = -5
            if is_failed:
                check = -6
            timetable[level] = check
            get_efficient_time(level + 1, count + 1, timetable, remain)


def get_timedata(list_):
    list_week = []
    split_ = ';'
    global days, table_
    for i, v in enumerate(list_):
        list_day = []
        val = str(v)
        # 쪼개서 근무할 수 있는 시간이 여러 날짜일 경우가 있음.
        count = val.count(';') + 1
        list_day = [0] * 8
        for j in range(count):

            text = val
            if count > 1:
                text = text.split(split_)[j]

            for k in range(int(text[0:2]) - 10, int(text[6:8]) - 10):
                list_day[k] = 1

        list_week.append(list_day)
    return list(np.ravel(list_week))


def make_timetable(a_time, b_time, c_time, d_time):
    all_time = [a_time] + [b_time] + [c_time] + [d_time]
    global schedule
    all_list = []
    for i, v in enumerate(all_time):
        all_list.append(get_timedata(v))

    working_times = [10] * len(peoples)  # 알바생이 하루에 일 할수 있는 시간
    schedule = all_list
    get_efficient_time(0, 0, [0] * 40, working_times)

    # TODO 빈 시간을 최초화 하는 방법으로 테이블을 생성하는데는 많은 경우의 수가 생기고, 이를 랜덤으로 리턴함
    result_table = table_[random.randrange(0, len(table_) - 1)]
    return np.reshape(result_table, (5, 8))


if __name__ == '__main__':
    a = ['10:00~14:00', '15:00~18:00', '11:00~13:00;14:00~16:00', '10:00~11:00', '15:00~18:00']
    b = ['11:00~14:00', '14:00~16:00', '16:00~18:00', '10:00~11:00;12:00~13:00', '14:00~16:00']
    c = ['14:00~16:00', '16:00~18:00', '10:00~12:00', '12:00~14:00', '14:00~16:00']
    d = ['14:00~18:00', '10:00~18:00', '12:00~14:00', '14:00~15:00;16:00~17:00', '10:00~12:00']
    min_ = 999
    table_ = []
    schedule = []
    hour_unit = 8  # 하루 가게 오픈 시간
    days_unit = 5  # 일주일 중 일하는 날짜
    business_time = 8  # 하루 가게 영업시간
    days = ['월', '화', '수', '목', '금']
    peoples = ['A', 'B', 'C', 'D']
    print(make_timetable(a, b, c, d))

    # print(schedule[0])              # 사람 A 일정표 일렬로 늘림
    # print(schedule[1])              # 사람 B 일정표 일렬로 늘림
    # print(schedule[2])              # 사람 C 일정표 일렬로 늘림
    # print(schedule[3])              # 사람 D 일정표 일렬로 늘림
    print(f'빈 일정 (-5, -6) : {min_}개')
