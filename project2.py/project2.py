import random

num1 = int(input('Tell me a number\n'))
num2 = int(input('Tell me another number\n'))

op = random.randint(0, 2)
op_list = ['+','-','*']

if op == 0:
    rhs = num1 + num2

if op == 1:
    rhs = num1 - num2

if op == 2:
    rhs = num1 * num2

print("Can you tell me the missing operator?")

qn = str(num1) + '__' + str(num2) + '=' + str(rhs)
answer = input(qn + '\n')

if answer == op_list[op]:
    print("well done")
else:
    print("try again")

print()
print()
print("Now a harder question + \n")
num3 = random.randint(1, 100)

#addition or sustraction

op1 = random.randint(0, 1)
op2 = random.randint(0, 1)

if op1 == 0:
    rhs = num1 + num2
if op1 == 1:
    rhs = num1 - num2

if op2 == 0:
    rhs = num1 + num2
if op2 == 1:
    rhs = num1 - num2

print("Now tell me the missing operator + \n")

qn = str(num1) + '__' + str(num2) + '__' + str(num3) + '=' + str(rhs)
answer = input(qn + '\n')

if answer == op_list[op]:
   print("Well Done")
else:
    print("try again")


print("LEVEL 2 ")

num3 = random.randint(1, 100)

#addition or sustraction

op1 = random.randint(0, 1)
op2 = random.randint(0, 1)

if op1 == 0:
    rhs = num1 + num2
if op1 == 1:
    rhs = num1 - num2

if op2 == 0:
    rhs = num1 + num2
if op2 == 1:
    rhs = num1 - num2

print("Now tell me the missing operator")

qn = str(num1) + '__' + str(num2) + '__' + str(num3) + '=' + str(rhs)
answer = input(qn + '\n')

if answer == op_list[op]:
   print("Well Done")
else:
    print("try again")