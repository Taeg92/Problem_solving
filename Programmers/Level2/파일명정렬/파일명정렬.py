import re


def solution(files):
    arr = [re.split("(\d+)", file) for file in files]
    return ["".join(sorted_arr) for sorted_arr in sorted(arr, key=lambda x: (x[0].lower(), int(x[1])))]


files = ["img12.png", "img10.png", "img02.png",
         "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))
