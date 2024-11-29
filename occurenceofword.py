  GNU nano 4.8                                                      occurenceofword.py                                                                 
text=input("Ente a text:")
words=text.split()
word_count={}
for i in words:
        i=i.lower()
        if i in word_count:
                word_count[i]+=1
        else:
                word_count[i]=1
print(f"Word occurence are:{word_count}")

