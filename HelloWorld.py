firstName = "J"
lastName = "G"
firstNum = 243
secNum = 2.34
print(lastName +', '+firstName+"\n")
print(str(firstNum) +', '+ str(secNum)+"\n")
print(int(secNum),float(firstNum))

regions = ["North", "South", "East", "West"]
sales = [30000,20000,40000,50000]
employees = ["Alice", "Vera", "Flo", "Mel"]

employees[2] = "Belle"
for employees in employees:
    print(employees)

firstNumber=input("First number>>")
secondNum=input("Second number>>")
sum = float(firstNumber)+float(secondNum)
print("Sum: ",firstNumber,"+",secondNum ,"=",sum)

"""
Test run 1:
/Users/Home/HelloWorld/FirstpythonProject8.26/.venv/bin/python /Users/Home/HelloWorld/FirstpythonProject8.26/.venv/HelloWorld.py 
G, J

243, 2.34

2 243.0
Alice
Vera
Belle
Mel
First number>>4
Second number>>2
Sum:  4 + 2 = 6.0

Process finished with exit code 0
"""