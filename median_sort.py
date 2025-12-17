numbers=[20,40,60,80,100,10,30,50,70,90]
n=len(numbers)
for i in range(n):
    for j in range(0,n-i-1):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
if n%2==1:
    median=numbers[n//2]
else:
    median=(numbers[n//2-1]+numbers[n//2])/2
print("Sorted:",numbers)
print("Median:",median)