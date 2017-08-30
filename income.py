#!/usr/bin/env python
#-*- coding: utf-8 -*-
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
myBook = xlrd.open_workbook(r'fx_CJ095_1065.xlsx')
mySheet = myBook.sheet_by_index(0)

#get datas
time = mySheet.col(0)
time = [x.value for x in time]
time = [datetime.datetime(*xldate_as_tuple(x, 0)).strftime('%Y/%m/%d') for x in time if isinstance(x, float)]
tps = mySheet.col_values(14)

#drop the 1st line of the data, which is the name of the data.
# time.pop(0)
tps.pop(0)

#declare a figure object to plot
fig = plt.figure(figsize = (15,8))

#plot tps
plt.plot(tps, color='#57B7E0', label='收入')

#advance settings
plt.title('收入')
ax = fig.add_subplot(1,1,1)

# ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y/%m/%d'))#设置时间标签显示格式
plt.xticks(range(len(time)),time,rotation=25)
for i in range(0, len(time)):
    ax.annotate(str(tps[i]), (i, tps[i]))
    

#show the figure
plt.legend(loc='upper left', bbox_to_anchor=(0.9, -0.09), fancybox=True, ncol=5)

plt.savefig(u"收入.png")
# plt.show()
