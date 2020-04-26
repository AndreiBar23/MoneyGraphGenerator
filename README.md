# MoneyGraphGenerator

Python Script that will take one input .txt file and will generate a bar graph that will show the monthly earnings for a year. After the last bar plot column, it will be displayed the mean of the earnings per year. 

The example file Money.txt accepts the following formatting:
 - Money_value,Currency(which is not implemented at the moment), Month_Name(3 letters)
 - The Money_value parameter from the .txt file could be also a list. Example: 100,200,300'
 - The first line of the document will be ignoring when calling the Script. 
 
 Dependencies:
  - Python 3
  - Matplotlib
  - Numpy
  - Tkinter 
  
  When running the Script the user will be prompt using the Tkinter File Explorer GUI To choose the .txt file as input.
