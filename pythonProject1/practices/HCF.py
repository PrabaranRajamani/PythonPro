def find_hcf(x, y):
    smaller = x if x < y else y

    hcf = 0

    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i

    return hcf


num1 = int(input("Enter the no 1:"))
num2 = int(input("Enter the no 2:"))

result = find_hcf(num1, num2)
print("The HCF of", num1, "and", num2, "is:", result)
