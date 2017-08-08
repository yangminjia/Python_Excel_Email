# -*-coding:utf-8-*-
#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import datetime
import matplotlib.dates as mdate
from xlrd import xldate_as_tuple
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\\windows\\fonts\\simsun.ttc", size=14)

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#open excel file and get sheet
myBook = xlrd.open_workbook(r'new.xlsx')
mySheet = myBook.sheet_by_index(0)

#get datas
time = mySheet.col(0)
time = [x.value for x in time]
time = [datetime.datetime(*xldate_as_tuple(x, 0)).strftime('%Y/%m/%d') for x in time if isinstance(x, float)]
dau = mySheet.col_values(1)
bline = mySheet.col_values(17)
#drop the 1st line of the data, which is the name of the data.
# time.pop(0)
# tps.pop(0)
dau.pop(0)
bline.pop(0)
#declare a figure object to plot
fig = plt.figure(figsize = (15,8))
bar_width = 0.4
#plot tps
# plt.plot(tps)
left = [x for x in range(0, len(time))]
plt.bar(left, dau, bar_width, color='b', label='DAU')
plt.legend(loc='upper right', bbox_to_anchor=(1, -0.09), fancybox=True, ncol=5)
#advance settings
plt.title('日活与总安装', fontproperties=font)
plt.xticks(range(len(time)),time,rotation=25)
ax = fig.add_subplot(1,1,1)
ax1 = ax.twinx()
ax1.plot(bline, label = 'GP Install/Total')
# ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y/%m/%d'))#设置时间标签显示格式

for i in range(0, len(time)):
    ax.annotate(str(dau[i]), (i-1, dau[i]))
for i in range(0, len(time)):
    ax1.annotate(str(format(bline[i], '.2%')), (i-1, bline[i]+0.01),rotation=60)
plt.legend(loc='upper left', bbox_to_anchor=(0.65, -0.09), fancybox=True, ncol=5)
# ax.annotate('100', (1,tps[1]))
# plt.savefig(u"收入.png")
#show the figure
plt.show()

if __name__ == '__main__':
	pass
