text = input().split()
statistics = {}
for i in text:
    if len(i) in statistics:
        statistics[len(i)] += 1
    else:
        statistics[len(i)] = 1

keys = sorted(statistics.keys())

for i in keys:
    print(i, ': ', statistics[i], sep='')
