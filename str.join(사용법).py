str = "234434ㄴ";
print(str.isdecimal());

str = "$";
seq = ("a", "b", "c"); # This is sequence of strings.
print(str.join(seq));


# string => list
char_list = list('Python')
print(char_list)

string = "a b c d e f g h"
char_list = string.split() # default 인자: space
print(char_list)
string = "a:b:c:d:e:f:g:h"
char_list = string.split(':')
print(char_list)

# list => string
print(''.join(char_list))

#-----------------"abcd"를 각각의 문자로 끊음
#-----------------"ab","cd"로 하면 ab만세cd 이다
a = '만세'
b = ("abcd")
print(a.join(b))
a = "sk samsung"
c = list(a.split())
print(c)
a = '만세'
b = ("ab","cd")
print(a.join(b))
print(''.join(c))





