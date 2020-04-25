#imports
from tkinter import filedialog
from tkinter import *
import os
import sys
from numpy import zeros
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
from numpy import argmax, argmin, mean
import matplotlib.pyplot as plt
#import end

#fileExplorer Area
root = Tk()
filePath = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",
                                           filetypes=[("Text Files", "*.txt")])
root.destroy()
######
document = open(filePath, "r")

lines = document.readlines()
#ignore last line character 
lines =  [line[:-1] for line in lines]

#define month and money dict 
money_dict = {"JAN":0,"FEB":0,"MAR":0,"APR":0,"MAY":0,"JUN":0,"JUL":0,"AUG":0,
              "SEP":0,"OCT":0,"NOV":0,"DEC":0}

month_names = [key for key in money_dict]
month_names.append("Month AVG")
mean_plot_index = 12
money = 0
plot_title = "Monthly Fiscal Analysis"

#read string lines from textFile
#process lines to generate graph 
#processing starts from line 1 
for cnt, line in enumerate(lines):
    
    if cnt == 0 or line == '' or line =='\n':
        continue
    input_vect = line.split(" ")
    money_vect = input_vect[0].split(",")
    if(len(money_vect) > 1):
        for number in money_vect:
            money += int(number)
    else:
        money = int(input_vect[0])
    month = input_vect[2].upper()
    if(month in money_dict.keys()):
        money_dict[month] += money
        money = 0

money_list = []
for k, v in money_dict.items():
   money_list.append(v)
money_list.append(mean(money_list))
   
#figure
y_pos = np.arange(len(month_names))
plt.figure(num=plot_title, figsize=(12, 7), dpi=80)

#graph Area
barplot = plt.bar(y_pos, money_list, align='center', alpha=0.5, color="blue")
min_index = argmin([money for money in money_list[:-1] if money > 0], axis = 0) + 1
barplot[argmax(money_list)].set_color('green')
barplot[min_index].set_color('red')
barplot[mean_plot_index].set_color('orange')
plt.xticks(y_pos, month_names)
plt.ylabel('Money Per Month')
plt.title(plot_title)
plt.show()
document.close()
sys.exit()