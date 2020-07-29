import math
while True:
    result =-1
    num = int(input())
    if num != -1:
        for i in range(2,  int(math.sqrt(math.sqrt(num)))+2):
            check = num
            token = True
            for j in range(i):
                if check % i ==1 :
                    check -= (check//i)+1
                else:
                    token = False
                    break
            if check%i==0 and token:
                result = i
        if result != -1:
            print(num ,'coconuts,',result,'people and 1 monkey')
        else:
            print(num,'coconuts,','no solution')
    else:
        break

