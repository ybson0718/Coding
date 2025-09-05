#수들의 합
import sys
input =sys.stdin.readline

n=int(input())
count=0
s=0
for i in range(0,n):
    s=0
    for j in range(i,n):
        s+=j
        if s==n:
            count+=1
            break
        elif s>n:
            break
    
print(count)
        
    