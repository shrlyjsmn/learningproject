def permutationEquation(p):
    permutationpx=[]
    for x in range(1,len(p)+1):
        for y in range(len(p)) :
            if x == p[y] :
                permutationpx.append(y+1)  
    permutationpy=[]
    for y in permutationpx:
        for i in range(len(p)):
            if y == p[i]:
                permutationpy.append(i+1)
    return permutationpy

print(permutationEquation([2,3,1])) #2 3 1
print(permutationEquation([4,3,5,1,2])) #1 3 5 4 2