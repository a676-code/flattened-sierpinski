# flattened_sierpinski.py
# Andrew Lounsbury
# 29/3/23
# Purpose: generate a particular fractal sequence

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# converts a decimal number to a list of binary digits
def decimalToBinary(n):
    digits = []
    while n >= 1:
        digits.append(n % 2)
        if n % 2 == 1:
            n = int((n - 1) / 2)
        elif n % 2 == 0:
            n = int(n / 2)
    return digits

# checks if two numbers have overlapping 1's in binary
def overlap(a, b):
    a_digits = decimalToBinary(a)
    b_digits = decimalToBinary(b)
    
    if len(a_digits) < len(b_digits):
        for i, d in enumerate(a_digits):
            if d == 1 and b_digits[i] == 1:
                return True
    return False

def generate_flattened_sierpinski(n):
    a = [0]
    i = 2
    while len(a) < n:
        for x in reversed(range(i)):
            if not overlap(x, i):
                a.append(x)
        i += 1
    return a

print(generate_flattened_sierpinski(50))

# Scatter Plots
n = 10
sequence = generate_flattened_sierpinski(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(len(sequence))]
sns.scatterplot(x="index", y='Number', data=df)
plt.show()

n = 100
sequence = generate_flattened_sierpinski(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y='Number', data=df)
plt.show()

n = 1000
sequence = generate_flattened_sierpinski(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(len(sequence))]
sns.scatterplot(x="index", y='Number', data=df)
plt.show()

n = 10000
sequence = generate_flattened_sierpinski(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(len(sequence))]
sns.scatterplot(x="index", y='Number', data=df)
plt.show()

n = 100000
sequence = generate_flattened_sierpinski(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(len(sequence))]
sns.scatterplot(x="index", y='Number', data=df)
plt.show()

n = 10
sequence = generate_flattened_sierpinski(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df_averages = pd.DataFrame(average_sequence, columns=["Average"])
df_averages['index'] = [i for i in range(len(sequence))]
sns.scatterplot(x="index", y="Average", data=df_averages)
plt.show()

n = 100
sequence = generate_flattened_sierpinski(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df_averages = pd.DataFrame(average_sequence, columns=["Average"])
df_averages['index'] = [i for i in range(len(sequence))]
sns.scatterplot(x="index", y="Average", data=df_averages)
plt.show()

n = 1000
sequence = generate_flattened_sierpinski(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df_averages = pd.DataFrame(average_sequence, columns=["Average"])
df_averages['index'] = [i for i in range(len(sequence))]
sns.scatterplot(x="index", y="Average", data=df_averages)
plt.show()

n = 10000
sequence = generate_flattened_sierpinski(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df_averages = pd.DataFrame(average_sequence, columns=["Average"])
df_averages['index'] = [i for i in range(len(sequence))]
sns.scatterplot(x="index", y="Average", data=df_averages)
plt.show()

n = 100000
sequence = generate_flattened_sierpinski(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df_averages = pd.DataFrame(average_sequence, columns=["Average"])
df_averages['index'] = [i for i in range(len(sequence))]
sns.scatterplot(x="index", y="Average", data=df_averages)
plt.show()