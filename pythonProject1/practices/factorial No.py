# num = int(input("Enter the no:"))


# if num < 0:
#     print("fac doesn't exist zero")
# elif num== 0:
#     print("fact of zero is 1")
# else:
#     fact = 1
#     for i in range (1, num+1):
#         fact = fact *i
#     print(fact)

# using recursion



def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter the number: "))
print(factorial(n))
