# -*-coding:utf-8-*-
#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import datetime
import matplotlib.dates as mdate
from xlrd import xldate_as_tuple
from matplotlib.font_manager import FontProperties

# font = FontProperties(fname=r"c:\\windows\\fonts\\simsun.ttc", size=14)

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
front = mySheet.col_values(6)
end = mySheet.col_values(7)

#drop the 1st line of the data, which is the name of the data.
front.pop(0)
end.pop(0)

#declare a figure object to plot
fig = plt.figure(figsize = (15,8))

bar_width = 0.4

#plot tps
left = [x for x in range(0, len(time))]
right = [x+bar_width for x in range(0, len(time))]
plt.bar(left, front, bar_width, color='b', label= '前命中量')
plt.bar(right, end, bar_width, color='r', label = '后命中量')

#advance settings
plt.title('前后命中量')
ax = fig.add_subplot(1,1,1)
# ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y/%m/%d'))#设置时间标签显示格式
plt.xticks(range(len(time)),time,rotation=25)
for i in range(0, len(time)):
    ax.annotate(str(front[i]), (i - 1, front[i]-10000), rotation=60)
for i in range(0, len(time)):
    ax.annotate(str(end[i]), (i , end[i]))
    

#show the figure
plt.legend(loc='upper right', bbox_to_anchor=(1, -0.09), fancybox=True, ncol=5)
# plt.show()
plt.savefig(u"前后命中量.png")

if __name__ == '__main__':
	pass
