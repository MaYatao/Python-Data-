import  matplotlib.pyplot as  plt  

x_values=list(range(1,1001))

y_values=[x**2 for x in x_values]

#plt.scatter(x_values,y_values,c="red",edgecolors="none",s=40)
#plt.scatter(x_values,y_values,c=(0,0,0.8),edgecolors="none",s=40)
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors="none",s=40)

#设置图表标题并给坐标加上标签
plt.title("Square  Numbers",fontsize=24)
plt.xlabel("Value",fontsize=24)
plt.ylabel("Square of  value" ,fontsize=24)

#设置刻度标记的大小
plt.tick_params(axis="both",which="major",labelsize=14)

#设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])


#plt.show()   显示
#实参1表示保存名，在此文件目录，实参2表示去掉空白部分，可省略
plt.savefig("Squares_plot.png",bbox_inchs="tight")