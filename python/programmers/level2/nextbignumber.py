n = int(input("정수n 입력: "))

def solution(n):
    answer = 0
    i = n+1
    su = sum(list(map(int, list(bin(n).replace("0b", "")))))

    while(1):
        if(sum(list(map(int, list(bin(i).replace("0b", ""))))) == su):
            answer = i
            break
        i += 1

    return answer

# 다른 사람 풀이
'''

su = bin(n).count('1')
while True:
    n = n+1
    if su == bin(n).count('1'):
        break

return n

'''

print(solution(n))
