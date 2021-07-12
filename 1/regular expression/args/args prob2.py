employees={
    1000:{'eid':1000,'ename':'ajay','salary':'23000','desi':'developer'},
    1001:{'did':1001,'ename':'arj','salary':'32000','desi':' python developer'},
    1002:{'eid':1002,'ename':'alok','salary':'42000','desi':'java developer'},
    1003:{'eid':1003,'ename':'alan','salary':'56000','desi':'dol developer'}

}
# print(employees[1002])
# print(employees[1002]['ename'])


#input from user
eid=int(input('enter the id number '))
property=input('enter the you want to display ')
if eid in employees and property in employees[eid]:
    print(employees[eid][property])
else:
    print('invalid eid or property ')
