data = [10, 20, 20, 30, 40, 40, 40, 50, 60, 60, 70, 70, 70, 70, 80, 90]
freq = {}
for n in data:
    freq[n] = freq.get(n, 0) + 1
max_freq = max(freq.values())
modes = [k for k, v in freq.items() if v == max_freq]
print("Mode(s):", modes)
print("Highest Frequency:", max_freq)
