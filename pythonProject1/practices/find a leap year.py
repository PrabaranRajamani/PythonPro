year = int (input("enter the year :"))

if year % 400== 0  and year % 100 ==0:
    print(f'{year} is a leap year ')
elif (year % 4 == 0) and (year % 100 != 0):
    print(f'{year} is a leap year ')
else :
    print(f'{year} is nt an leap year')