# Problem [6359] : 만취한 상범
from math import floor

T = int(input())

for _ in range(T):
    n = int(input())
    print(floor(n ** 0.5))
