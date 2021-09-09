'''
class based + less time complex code;
'''
import pandas as pd

class Sdata:
	def __init__(self, sd):
		self.sd = sd

	def pf(self, m):
		if m < 35:
			return 0
		else:
			return 1

	def summary(self):
		std = []
		name = []
		py = []
		java = []
		node = []
		php = []

		stds = [i for i in range(1,11)]
		pass_ = [0 for i in range(10)]
		fail = [0 for i in range(10)]
		ratio = [0 for i in range(10)]

		for i in range(len(self.sd)):

			std.append(self.sd['Std'][i])
			name.append(self.sd['name'][i])

			py.append(self.pf(self.sd['python'][i]))
			java.append(self.pf(self.sd['java'][i]))
			node.append(self.pf(self.sd['node'][i]))
			php.append(self.pf(self.sd['php'][i]))

			if py[i] and java[i] and node[i] and php[i]:
				pass_[std[i]-1] = pass_[std[i]-1] + 1
			else:
				fail[std[i]-1] = fail[std[i]-1] + 1

		for i in range(len(stds)):
			loop_count = loop_count + 1
			r = pass_[i] * 100 / fail[i]
			ratio[i] = round(r, 2)

		dresult = {
			'std' : stds,
			'pass' : pass_,
			'fail' : fail,
			'ratio' : ratio,
		}

		fresult = pd.DataFrame(dresult)
		fresult.to_excel("cresult.xlsx", index=False)
		
		print(fresult)

tpd = pd.read_excel('sdata.xlsx')
sdobj = Sdata(tpd)
sdobj.summary()
