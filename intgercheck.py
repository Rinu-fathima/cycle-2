n=int(input("Enter number of integers to input for first list:"))
list1=[]
for i in range(n):
        num1=int(input("Enter Integers:"))
        list1.append(num1)
m=int(input("Enter number of integers to input for first list:"))
list2=[]
for i in range(m):
        num2=int(input("Enter Integers:"))
        list2.append(num2)
if len(list1)==len(list2):
        print("Lists are of same length")
else:
        print("Lists are of different length")
if sum(list1)==sum(list2):
        print("The lists have same sum value")
else:
        print("The lists have different sum value")

common=set(list1) & set(list2)
if common:
        print(f"Common values in both list{common}")
else:
        print("There are no common value in both lists")


