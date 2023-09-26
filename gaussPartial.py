from numpy import array, zeros, fabs, linalg

a = array([[5.4,-3.2,8.1],[17,21,-22],[5,-4,1]], float)
#the b matrix constant terms of the equations 
b = array([13,25,-8], float)

print("Solution by NumPy:")


print(linalg.solve(a, b))

n = len(b)
x = zeros(n, float)

#first loop specifys the fixed row
for k in range(n-1):
    if fabs(a[k,k]) < 1.0e-12:
        
        for i in range(k+1, n):
            if fabs(a[i,k]) > fabs(a[k,k]):
                a[[k,i]] = a[[i,k]]
                b[[k,i]] = b[[i,k]]
                break

 #applies the elimination below the fixed row

    for i in range(k+1,n):
        if a[i,k] == 0:continue

        factor = a[k,k]/a[i,k]
        for j in range(k,n):
            a[i,j] = a[k,j] - a[i,j]*factor
            #we also calculate the b vector of each row
        b[i] = b[k] - b[i]*factor
print(a)
print(b)


x[n-1] = b[n-1] / a[n-1, n-1]
for i in range(n-2, -1, -1):
    sum_ax = 0
  
    for j in range(i+1, n):
        sum_ax += a[i,j] * x[j]
        
    x[i] = (b[i] - sum_ax) / a[i,i]

print("The solution of the system is:")
print(x)