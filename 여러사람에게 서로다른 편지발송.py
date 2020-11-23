dongari = '''
----------------------
%s 회원님

안녕하셨습니까 ? 이번에 우리 동아리에서는
봄을 맞이하여 %s로 MT를 떠납니다.
참가 회비는  %d 원  입니다. 많이 참석하여
즐거운 시간을 가지시기 바랍니다.

회장 일수꾼 올림
-------------------------'''
print(dongari % ('강당수', '요단강', 14500))

mem1 = ( 'Tom', 'USA ', 5110000 )
mem2 = ( 'Garry', 'JAPAN ', 1230000 )
mem3 = ( 'Smith', 'JAPAN ', 1230000 )
mem4 = ( 'Elizabeth' , 'France', 3313000 )
mem5 = ( 'Gromly', 'Korea', 135000 )

ml = [mem1, mem2, mem3, mem4, mem5]
for w in ml:
    print(dongari % w)

