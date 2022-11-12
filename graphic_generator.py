import matplotlib.pyplot as plt

fh = open("resulting_data.csv", "r", encoding="utf-8")
f = fh.readlines()


del f[0]


x_netscore = []
y_retweets = []

for x in f:
    x = x.rstrip()
    x = x.split(",")
    x_netscore.append(int(x[4]))
    y_retweets.append(int(x[0]))

print(f'x: {x_netscore}\ny: {y_retweets}')

plt.scatter(x_netscore, y_retweets)
plt.show()