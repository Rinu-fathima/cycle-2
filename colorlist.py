colorlist1=input("Enter colors for list 1 in lowercase seprated by space:")
colorlist2=input("Enter colors for list 2 in lowercase seprated by space:")
color1=colorlist1.split()
color2=colorlist2.split()
newlist=[color for color in color1 if color not in color2]
print(f"list of colors from list 1 and not contained in list 2 are:{newlist}")
