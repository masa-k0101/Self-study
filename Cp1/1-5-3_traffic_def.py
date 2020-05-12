#textでは元々spを使っていた
import scipy as sp
import numpy as np

#ランダムに作ったtrafficデータを用いる
file_id = 'web_traffic.csv'
file_path = '/xxxx/xxxxx/.spyder-py3/workspace/'
rfile = file_path + file_id

#csvファイルを読み込み
data = np.genfromtxt(rfile, comments='#' ,delimiter=',')

x = data[:,0]
y = data[:,1]

#欠損部分を削除
x = x[~np.isnan(y)]
y = y[~np.isnan(y)]

#散布図を描画
import matplotlib.pyplot as plt
plt.scatter(x,y)

plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
#plt.glid()
#plt.show()

def error (f,x,y):
   return np.sum((f(x)-y)**2)

fp1, residuals, rank, sv, rcond = np.polyfit(x,y,1,full=True)
print("Model parameters: %s" % fp1)
print(residuals)

#最小二乗法(１次)計算
x1 = np.linspace(0,x[-1],1000)
a,b = np.polyfit(x,y,1)
y1 = a*x1 + b

#最小二乗法(2次)計算
a2,b2,c2 = np.polyfit(x,y,2)
y2 = a2*x1**2 + b2*x1 + c2

f1 = np.poly1d(fp1)
#print(error(f1,x,y))
#fx = 4.79068922*x + 104.93914142

fx = np.linspace(0,x[-1],1000)
plt.plot(fx,f1(fx),linewidth=4)

plt.plot(x1,y2,linewidth=4)
plt.text(0.1,a*0.1+b, 'y='+ str(round(a,4)) +'x+'+str(round(b,4)))
#plt.legend(["d=%i" % y1.order], loc="upper left")
