import pandas as pd

sd = pd.read_excel('sdata.xlsx')

std = []
name = []

py = []
java = []
node = []
php = []

for col, item in sd.iteritems():

	def pf(m):
		if m<35:
			#print(0)
			return 0
		else:
			#print(1)
			return 1

	if col == "Std":
		for i in item:
			std.append(i)
	elif col == "name":
		for i in item:
			name.append(i)

	elif col == "python":
		for i in item:
			py.append(pf(i))
	elif col == "java":
		for i in item:
			java.append(pf(i))
	elif col == "node":
		for i in item:
			node.append(pf(i))
	elif col == "php":
		for i in item:
			php.append(pf(i))

stds = [i for i in range(1,11)]
pass_ = [0 for i in range(10)]
fail = [0 for i in range(10)]
ratio = [0 for i in range(10)]

for i in range(len(name)):
	if py[i] and java[i] and node[i] and php[i]:
		pass_[std[i]-1] = pass_[std[i]-1] + 1
	else:
		fail[std[i]-1] = fail[std[i]-1] + 1

for i in range(len(stds)):
	r = pass_[i] * 100 / fail[i]
	ratio[i] = round(r, 2)

dresult = {
	'std' : stds,
	'pass' : pass_,
	'fail' : fail,
	'ratio' : ratio,
}

fresult = pd.DataFrame(dresult)

print(fresult)

fresult.to_excel("result.xlsx", index=False)
