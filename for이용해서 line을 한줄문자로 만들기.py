text = """모두가 뇌절이라고 말하지
그러나 나는 뇌절 맞지 않아았지
그대들이여 다들 일어나
우리 함께 유로파를 보아야지
모두 챔스 티켓의 손이 누구에게 가는지
알아 맞춰 보자구~!"""
outfile = open("aa.txt", "w")
s = ""
for line in text:
    myline = line.strip()
    s += myline
outfile.write(s)