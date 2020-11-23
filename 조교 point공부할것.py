def chkRel(b, l): # 사각형이 주어지고 각 점과 사각형간의 관계 판별 함수
    return [{(b[0]<x<b[2] and b[1]<y<b[3]):"IN", (x<b[0] or x>b[2] or y<b[1] or y>b[3]):"OUT"}.get(True,"ON") for x, y in [map(int, i.split()) for i in l]]

with open("point.inp", "r") as fi, open("point.out", "w") as fo: # 파일 입출력 처리
    fo.write('\n'.join(chkRel(list(map(int, fi.readline().split())),fi.readlines()))) # 각 점에 대한 관계 결과 작
