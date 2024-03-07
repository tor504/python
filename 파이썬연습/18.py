# 남녀 파트너 정해주기 프로그램 만들기 -> zip
from random import shuffle

m = ['슈퍼맨','심봉사','로미오','이몽룡','마루치']
f = ['원더우먼','뺑덕','줄리엣','성춘향','아라치']

shuffle(m)
shuffle(f)

couples = zip(m,f)

for i,couple in enumerate(couples):
    print('커플%d:[%s]-[%s]'%(i+1,couple[0],couple[1]))

