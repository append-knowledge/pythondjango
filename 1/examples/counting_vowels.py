x=input('enter a word ')
y=('aeiou')
vowel=0
for i in x:
    if i in y:
        vowel+=1
if vowel==0:
    print("vowels not found")
else:
    print("number of vowels is",vowel)
