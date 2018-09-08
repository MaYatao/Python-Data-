from die import  Die
import pygal

#创建2个Ｄ６
die1=Die()
die2=Die()

#掷几次骰子，并将结果储存到一个列表中
results=[]
for rool_num in range(1000):
    result=die1.roll()+die2.roll()
    results.append(result)

#分析结果
frequencies=[]
for value in range(2,die1.num_sides+die2.num_sides+1):
    frequence =results.count(value)
    frequencies.append(frequence)

#对结果进行可视化
hist=pygal.Bar()

hist.title="Result of  rolling one  D6 1000 times"
hist.x_labels=['2','3','4','5,','6','7','8','9','10','11','12']
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')