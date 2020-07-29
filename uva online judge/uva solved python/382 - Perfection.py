fast = True
last = True
while True:
    take = input()
    numlist = take.split()
    for num in numlist:
        length = len(num)
        num = int(num)
        sum =0
        if num!=0:
            if fast==True:
                print('PERFECTION OUTPUT')
                fast=False
            for i in range(1,int(num/2)+1):
                if num%i==0:
                    sum+=i
            result = 'Null'
            if sum == num:
                result = 'PERFECT'
            elif sum > num:
                result = 'ABUNDANT'
            else:
                result = 'DEFICIENT'

            for i in range(6-length-1):
                print(' ',end='')
            print(num,'',result)
        else:
            print('END OF OUTPUT')
            last = False
    if last == False:
        break