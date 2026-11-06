import matplotlib.pyplot as plt

# Sample age data
ages = [18, 19, 20, 21, 22, 23, 24, 25,
        19, 20, 21, 22, 23, 24, 25, 26,
        27, 21, 22, 23, 24, 20, 19, 28,
        29, 30, 22, 23, 24, 25, 26, 27]

# Create histogram
plt.hist(ages, bins=6, edgecolor='black')

# Add labels and title
plt.title("Age Distribution of Population")
plt.xlabel("Age")
plt.ylabel("Number of People")

plt.show()