
print("Hello World!")

EXPECTED_BAKE_TIME = 40
#functions
def bake_time_remaining(enter):
    total = EXPECTED_BAKE_TIME - enter
    return total

def prep_time_in_min(layers):
    prep_time = layers*2
    return prep_time

def elapsed_time(enter, pt):
    """notes!!!"""
    elapse = enter+pt
    print("Elapsed time (prep+ current bake time): "+str(elapse)+" mins!")

def total(EXPECTED_BAKE_TIME, pt):
    total = EXPECTED_BAKE_TIME + pt
    print("Est total time (prep+bake time): " + str(total) + " mins!")

#Start of program
print("Baking a lasagna. The expected bake time is "+ str(EXPECTED_BAKE_TIME)+ " minutes.")

#Data validation 1
while True:
        enter=int(input("Enter the baking time completed>> "))
        if enter<=40:
            if enter >=0:
                break
        print("Invalid entry...")
#printing results
bt = bake_time_remaining(int(enter))
print("Time remaining: "+str(bt)+" mins.")

#Data Validation 2
while True:
    layers=int(input("Enter the number of layers (has to be 10 or less)>> "))
    if layers <=10:
        if layers >= 1:
            break
    print("Invalid entry...")
#printing results
pt=prep_time_in_min(int(layers))
print(str(pt)+" mins spent prepping the layer(s)\n")
#printing results
elapsed_time(int(enter),int(pt))
total(int(EXPECTED_BAKE_TIME), int(pt))

"""
Test run 1:
/Users/Home/HelloWorld/pythonProject2/.venv/bin/python /Users/Home/HelloWorld/pythonProject2/.venv/lib/python3.12/pythonprac.py 
Hello World!
Baking a lasagna. The expected bake time is 40 minutes.
Enter the baking time completed>> 15
Time remaining: 25 mins.
Enter the number of layers (has to be 10 or less)>> 3
6 mins spent prepping the layer(s)

Elapsed time (prep+ current bake time): 21 mins!
Est total time (prep+bake time): 46 mins!

Process finished with exit code 0

"""