list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

# Mean
mean = sum(list1) / len(list1)
print("Среднее арифметическое: ", mean)

# Median
list1.sort()

if len(list1) % 2 == 0:
    m1 = list1[len(list1) // 2]
    m2 = list1[len(list1) // 2 - 1]
    median = (m1 + m2) / 2
else:
    median = list1[len(list1) // 2]
print("Медиана: ", median)

# Mode
frequency = {}
for i in list1:
    frequency.setdefault(i, 0)
    frequency[i] += 1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print("Мода: ", mode)

# Square deviations
deviations = [(x - mean) ** 2 for x in list1]
square_deviations = (sum(deviations) / (len(list1) - 1)) ** 0.5
print("Стандартное отклонение (Среднеквадратическое отклонение): ", square_deviations)

# Variance
variance = square_deviations * square_deviations
print("Дисперсия: ", variance)
