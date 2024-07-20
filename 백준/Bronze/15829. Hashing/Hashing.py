n = int(input())
s = input()
M=1234567891
an = 0
stack = 1

for i in s:
    k = ord(i)-96
    an+=stack*k
    stack*=31
    an%=M
    stack%=M
    
print(an%M)