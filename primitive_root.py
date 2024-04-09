def print2d(matrix):
    if(len(matrix)%2!=0):
        for i in range(0,len(matrix),2):
            for j in matrix[i]:
                print(j,end=' ')
            print()
    else:
        for row in matrix:
            for item in row:
                print(item, end=" ")
            print()


n = int(input("Enter the range: "))
a = n-1
lst = [[0]*(a) for i in range(a)]
# print(lst)
for i in range(a):
    for j in range(a):
        lst[i][j] = ((i+1)**(j+1))%n
print2d(lst)
primitive =[]
for i in range(a):
    found = False
    for j in range(a-1):
        if lst[i][j] == 1:
            found = True
            break
    if not found:
        if lst[i][a-1]==1:
            primitive.append(i+1)
if len(primitive)==0:
    print("No Primitive roots")
else:
    print(primitive)