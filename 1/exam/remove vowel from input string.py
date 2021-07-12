wrd=input("enter the string ")
vowel='a','e','i','o','u'
for i in wrd:
    if i in vowel:
        continue
    else:
        print(i)