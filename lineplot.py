from matplotlib import pyplot as plt

print(plt.style.available)
plt.style.use('ggplot')

dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

plt.xlabel("Ages")
plt.ylabel("Median Salary")
plt.title("Median Salary by age")

plt.plot(dev_x, dev_y, label='All Devs', color='g', linestyle='-.', linewidth='3', marker='o')
plt.legend(loc="upper right")
plt.show()

