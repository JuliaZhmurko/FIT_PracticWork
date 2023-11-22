from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

with open("sentences.txt","r") as infile:
        word_list=infile.read().split()

counts = Counter(word_list)
print(counts)
x, y = zip(*counts.items())
x1 = np.array(x)
y1 = np.array(y)
plt.xlabel("Words")
plt.ylabel("Count repeat")
plt.bar(x1, y1)
plt.xticks(rotation=90)
plt.show()