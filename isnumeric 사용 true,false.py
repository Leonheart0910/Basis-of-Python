a = '123123123'
cnt = 0
while a.isnumeric():
    cnt += 1
    print(cnt)
    if cnt == 5:
        break