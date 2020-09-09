def check(answer):
    for ans in answer:
        x, y, frame_type = ans

        # 기둥
        if frame_type == 0:
            if y == 0:
                continue
            elif [x-1, y, 1] in answer or [x, y, 1] in answer:
                continue
            elif [x, y-1, 0] in answer:
                continue
            else:
                return False
        # 보
        else:
            if [x, y-1, 0] in answer:
                continue
            elif [x+1, y-1, 0] in answer:
                continue
            elif ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = list()

    for frame in build_frame:
        x, y, frame_type, val = frame

        if val == 0:
            answer.remove([x, y, frame_type])
            if not check(answer):
                answer.append([x, y, frame_type])
        else:
            answer.append([x, y, frame_type])
            if not check(answer):
                answer.remove([x, y, frame_type])

    return sorted(answer)

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

print(solution(n, build_frame))