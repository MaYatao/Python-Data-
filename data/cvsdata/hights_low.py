import   csv
from   matplotlib  import  pyplot   as   plt
from   datetime  import  datetime

#从文件中获取日期，最高气温,最低气温
filename='/home/tao/Desktop/py/data/cvsdata/death_valley_2014.csv'
with   open(filename) as  f:
    reader=csv.reader(f)
    header_low=next(reader)
    #print(header_low)

    #for  index,column_header  in   enumerate(header_low):
       # print(index,column_header)

#    hights=[]
     
    dates, hights,lows=[],[],[]
    for  row in  reader:
        try:
            current_time=datetime.strptime(row[0],"%Y-%m-%d")
            low=int(row[3])
            hight=int(row[1])
        except ValueError:
            print(current_time,'missing data')
        else:
            hights.append(hight)
            dates.append(current_time)
            lows.append(low)
    
    #根据数据绘制图形
    fig=plt.figure(dpi=128,figsize=(10,6))
    plt.plot(dates,hights,c="red",alpha=0.5)
    plt.plot(dates,lows,c="blue",alpha=0.5)
    plt.fill_between(dates,hights,lows,facecolor='blue',alpha=0.1)

    #设置图形格式
    plt.title("Daily  hight temperatures, 2014",fontsize=24)
    plt.xlabel("",fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperatures(F)",fontsize=16)
    plt.tick_params(axis="both",which="major",labelsize=26)


    plt.show()