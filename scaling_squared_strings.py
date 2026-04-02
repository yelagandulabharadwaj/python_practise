'''
You are given a string of n lines, each substring being n characters long. For example:

s = "abcd\nefgh\nijkl\nmnop"

We will study the "horizontal" and the "vertical" scaling of this square of strings.

A k-horizontal scaling of a string consists of replicating k times each character of the string (except '\n').

Example: 2-horizontal scaling of s: => "aabbccdd\neeffgghh\niijjkkll\nmmnnoopp"
A v-vertical scaling of a string consists of replicating v times each part of the squared string.

Example: 2-vertical scaling of s: => "abcd\nabcd\nefgh\nefgh\nijkl\nijkl\nmnop\nmnop"
Function scale(strng, k, v) will perform a k-horizontal scaling and a v-vertical scaling.

example:
1.
input:
abcd
efgh
ijkl
mnop 
2,3
output: 'aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp'

2.
Kj
SH
1,2
output: 'Kj\nKj\nSH\nSH'
'''

def scale(strng, k, v):
    print(strng)
    strings=strng.split("\n")
    print(strings)
    if strng =='':
        return ''
    res=""
    for sub in strings:
        st= [x*k for x in sub]
        main_str="".join(st)
        for i in range(0,v):
            res=res+main_str+"\\n"
    res_send=res.split("\\n")
    res_send=res_send[:-1]
    # print("\n".join(res_send))
    return "\\n".join(res_send)

r ="abcd\nefgh\nijkl\nmnop"
print(scale(r,2,3))
r="Kj\nSH"
print(scale(r,1,2))
