import copy as c
a=[1,2,3,[4,5],6,7]
b=c.deepcopy(a)
a[3][1]="Aman"
print(a)
print(b)
