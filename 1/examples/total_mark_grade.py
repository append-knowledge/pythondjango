sub1=int(input("enter the mark "))
sub2=int(input("enter the mark "))
sub3=int(input("enter the mark "))
sub4=int(input("enter the mark "))
total=sub1+sub2+sub3+sub4
print("total mark is =",total)
if total>=150:
    print("1st class")
elif 150 > total >= 100:
    print("2nd class")
elif total<100:
    print("failed")