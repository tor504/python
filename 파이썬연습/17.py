# lotto 추출기
from random import shuffle
from time import sleep

num = input("로또 게임 회수를 입력하세요")

for i in range(int(num)):
    balls = [x + 1 for x in range(45)]
    a = []
    for j in range(6):
        shuffle(balls)
        number = balls.pop()
        a.append(number)

    a.sort()
    print('로또번호[%d]:'%(i+1),end='')
    print(a)
    sleep(1)