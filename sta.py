import matplotlib.pyplot as plt
import json
import numpy as np

with open('./count.json', 'r', encoding='utf-8') as f:
	data = json.load(f)
		
res = []
for key in data.keys():
	res.append(data[key])

res = [i for i in res if i>40000]

res = sorted(res, reverse=True)
x = list(range(len(res)))
x = np.array(x)
y = np.array(res)

plt.plot(x, y)
plt.show()