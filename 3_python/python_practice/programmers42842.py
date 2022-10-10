def solution(brown, yellow):
    sum_by = brown + yellow
    result = []
    answer = []
    for a in range(1, sum_by + 1):
        if sum_by % a == 0:
            result.append(a)
    if len(result) % 2 != 0:
        for b in range(2):
            answer.append(result[len(result) // 2])
    else:
        for c in range(len(result) // 2):
            if (result[c] - 2) * (result[len(result) - 1 - c] - 2) == yellow:
                answer.append(result[len(result) - 1 - c])
                answer.append(result[c])
                break
    return answer
print(solution(18, 6))