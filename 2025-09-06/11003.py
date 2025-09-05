#슬라이딩 윈도우 최소값

import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
nums = map(int, input().split())

print(N, L, nums)
dq = deque() 
out = []


