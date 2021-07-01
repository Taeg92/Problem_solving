from collections import deque


def is_valid(arr):
    pair = {"}": "{", "]": "[", ")": "("}
    stack = []

    for chr in arr:
        if chr not in pair:
            stack.append(chr)
        else:
            if not stack:
                return False
            token = stack.pop()
            if token != pair[chr]:
                return False

    if stack:
        return False
    return True

# function isValid(arr) {
#   const pair = { "}": "{", "]": "[", ")": "(" };
#   const stack = [];
#   for (let i = 0; i < arr.length; i++) {
#     const chr = arr[i];
#     if (pair[chr] === undefined) stack.push(chr);
#     else {
#       if (stack[stack.length - 1] !== pair[chr]) return false;
#       stack.pop();
#     }
#   }
#   if (stack.length) return false;
#   return true;
# }


def solution(s):
    answer = 0
    for i in range(len(s)):
        arr = deque(s)
        arr.rotate(-i)
        if is_valid(arr):
            answer += 1

    return answer


s = "[](){}"
print(solution(s))
