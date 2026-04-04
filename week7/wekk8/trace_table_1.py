num = 0
x = 999
y = 0
line = ""

f = open("/home/ravi/projects/python-coding-club/week7/wekk8/SalesFile.txt", "r")
for line in f:
    num = int(line)
    if num < x:
        x = num
    if num > y:
        y = num
print(x,y)
f.close()
