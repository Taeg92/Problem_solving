# Problem [15656] : N과 M(7)

from itertools import product

if __name__ == "__main__":
    N, M = map(int, input().split())
    D = sorted(list(map(int,input().split())))
    for prod in product(D, repeat=M):
        print(*prod)