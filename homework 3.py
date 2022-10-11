#1
marks = {'Andy':88, 'Amy':66, 'James': 90, 'Jules': 55, 'Arthur': 77}
def printGrade(student_name):
    if student_name in marks.keys():
        print(marks[student_name])
    else:
        print('I cannot find student name')
    
printGrade('Amy')
printGrade('Ashley')

#2
def while_n_less_than(num):
    n = 4
    while n < num:
        print(n)
        print(n ** 2)
        break
    else:
        print('greater than', num)
        
while_n_less_than(8)

#3
def adding_integers(num):
    sum = 0
    i = 1
    n = num
    while i <= n:
        sum = sum + i
        i = i + 1
    print(sum)
        
adding_integers(6)

print('#4')

def adding_integers2(num):
    sum = 0
    for i in range(1, num):
        print('i is', i, 'sum is', sum)
        sum = sum + i
    print(sum)

adding_integers2(6)

#5
l = list(range(1,100))
import statistics 
def question5(v1):
        print(statistics.mean(v1))
        print(sum(v1))
        print(statistics.stdev(v1))

question5(l)

#6
def minimal(v1, v2, v3, v4):
    min = v1
    if v2 < min:
        min = v2
    if v3 < min:
        min = v3
    if v4 < min:
        min = v4
    return min

print(minimal(20, 12, 23, 30))
    
#7

def myfunction(st1, st2, st3):
    return(st1 + ' ' + st2 + ' ' + st3)
print(myfunction('chocolate', 'covered', 'strawberry'))

