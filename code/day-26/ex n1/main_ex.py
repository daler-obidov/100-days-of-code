with open('/home/daler/code/100-days-of-code/code/day-26/ex n1/file1.txt') as f1:
    list1 = f1.readlines()
with open('/home/daler/code/100-days-of-code/code/day-26/ex n1/file2.txt') as f2:
    list2 = f2.readlines()



result = [int(num) for num in list1 if num in list2]

print(result)