import random
import statistics
from unittest import result
import plotly.figure_factory as plf
import plotly.graph_objects as pgo
dice_result = []
for i in range (0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)
mean = sum(dice_result)/len(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)
sd = statistics.stdev(dice_result)
print(mean, median , mode , sd)
fsd_start, fsd_end = mean - sd, mean + sd 
ssd_start , ssd_end = mean - (2*sd), mean + (2*sd)
tsd_start , tsd_end = mean - (3*sd), mean + (3*sd)
figure = plf.create_distplot([dice_result],["result"],show_hist= False)
figure.add_trace(pgo.Scatter(x = [mean,mean],y = [0,0.17], mode = "lines"))
figure.add_trace(pgo.Scatter(x = [fsd_start,fsd_start],y = [0,0.17], mode = "lines"))
figure.add_trace(pgo.Scatter(x = [fsd_end, fsd_end], y = [0, 0.17], mode = "lines"))
figure.add_trace(pgo.Scatter(x = [ssd_start,ssd_start], y = [0,0.17], mode = "lines"))
figure.add_trace(pgo.Scatter(x=  [ssd_end,ssd_end], y = [0,0.17], mode = "lines"))
figure.add_trace(pgo.Scatter(x = [tsd_start,tsd_start], y = [0,0.17], mode = "lines"))
figure.add_trace(pgo.Scatter(x = [tsd_end, tsd_end], y = [0,0.17], mode = "lines"))
data1 = [result for result in dice_result if result > fsd_start and result < fsd_end]
data2 = [result for result in dice_result if result > ssd_start and result < ssd_end]
data3 = [result for result in dice_result if result > tsd_start and result < tsd_end]
print("{}% of data lies within first standard deviation".format(len(data1)*100/len(dice_result)))
print("{}% of data lies within second standard deviation".format(len(data2)*100/len(dice_result)))
print("{}% of data lies within third standard deviation".format(len(data3)*100/len(dice_result)))
figure.show()
 