str=input("Enter a string which has reoccurance of first character in string:")
str2=str.lower()
firstchar=str2[0]
newstr=firstchar+str2[1:].replace(firstchar,'$')
print(f"New string is :{newstr}")

