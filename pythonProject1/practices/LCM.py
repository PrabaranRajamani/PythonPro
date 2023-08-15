def find_lcm(x, y):
    greater = x if x > y else y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater = greater + 1

    return lcm


num1 = int(input("Enter no 1: "))
num2 = int(input("Enter no 2: "))

result = find_lcm(num1, num2)
print("The LCM of", num1, "and", num2, "is:", result)
