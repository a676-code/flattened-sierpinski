# flattened_sierpinski_1.py
# Andrew Lounsbury
# 29/3/23
# Purpose: generate a fractal sequence

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

def generate_flattened_sierpinski_1(n):
    a = [0]
    i = 2
    while len(a) < n:
        for x in reversed(range(i)):
            if not overlap(x, i):
                a.append(x)
        i += 1
    return a

print(generate_flattened_sierpinski_1(100))

# Scatter Plots
n = 10
sequence = generate_flattened_sierpinski_1(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(len(sequence))]
sns.scatterplot(x="index", y='Number', data=df)
plt.savefig("images/10_1.png")
plt.show()

n = 100
sequence = generate_flattened_sierpinski_1(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y='Number', data=df)
plt.savefig("images/100_1.png")
plt.show()

n = 1000
sequence = generate_flattened_sierpinski_1(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(len(sequence))]
sns.scatterplot(x="index", y='Number', data=df)
plt.savefig("images/1000_1.png")
plt.show()

n = 10000
sequence = generate_flattened_sierpinski_1(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(len(sequence))]
sns.scatterplot(x="index", y='Number', data=df)
plt.savefig("images/10000_1.png")
plt.show()

n = 100000
sequence = generate_flattened_sierpinski_1(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(len(sequence))]
sns.scatterplot(x="index", y='Number', data=df)
plt.savefig("images/100000_1.png")
plt.show()

# Scatter plots of Averages
n = 10
sequence = generate_flattened_sierpinski_1(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df_averages = pd.DataFrame(average_sequence, columns=["Average"])
df_averages['index'] = [i for i in range(len(sequence))]
sns.scatterplot(x="index", y="Average", data=df_averages)
plt.savefig("images/average_10.png")
plt.show()

n = 100
sequence = generate_flattened_sierpinski_1(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df_averages = pd.DataFrame(average_sequence, columns=["Average"])
df_averages['index'] = [i for i in range(len(sequence))]
sns.scatterplot(x="index", y="Average", data=df_averages)
plt.savefig("images/average_100.png")
plt.show()

n = 1000
sequence = generate_flattened_sierpinski_1(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df_averages = pd.DataFrame(average_sequence, columns=["Average"])
df_averages['index'] = [i for i in range(len(sequence))]
sns.scatterplot(x="index", y="Average", data=df_averages)
plt.savefig("images/average_1000.png")
plt.show()

n = 10000
sequence = generate_flattened_sierpinski_1(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df_averages = pd.DataFrame(average_sequence, columns=["Average"])
df_averages['index'] = [i for i in range(len(sequence))]
sns.scatterplot(x="index", y="Average", data=df_averages)
plt.savefig("images/average_10000.png")
plt.show()

n = 100000
sequence = generate_flattened_sierpinski_1(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df_averages = pd.DataFrame(average_sequence, columns=["Average"])
df_averages['index'] = [i for i in range(len(sequence))]
sns.scatterplot(x="index", y="Average", data=df_averages)
plt.savefig("images/average_100000.png")
plt.show()