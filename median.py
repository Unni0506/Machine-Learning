numbers = [60, 70, 80, 90, 100, 10, 20, 30, 40, 50]
numbers.sort()
n = 0
for _ in numbers:
    n += 1
if n % 2 == 1:
    median = numbers[n // 2]
else:
    mid1 = numbers[(n // 2) - 1]
    mid2 = numbers[n // 2]
    median = (mid1 + mid2) / 2
print("Median:", median)