numbers=[-10,23,43,-3,-4,8,0]
positive_numbers=[num for num in numbers if num>0]
print(f"Positive numbers:{positive_numbers}")
N=4
square=[num**2 for num in range(1,N+1)]
print("Square of first N numbers:",square)
word="goodmorning"
words=word.lower()
vowels=[char for char in word if char in 'aeiou']
print(f"Vowels in the word:{vowels}")
word="hello"
ordinalvalue=[ord(char) for char in word]
print(f"Ordinal values of each character:{ordinalvalue}")

