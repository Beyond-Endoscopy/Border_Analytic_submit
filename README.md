# Border_Analytic_submit
The final submission files for the coding exam
# 1.The problem
The problem, basically, is to classify the data according to the borders (whether it is US-Canada border or US-Mexico border), date and measures (The type of transportation) first, then compute the sum of values and average of values. The point of this exam is that we are not allowed to use pandas (otherwise just groupby first then take the sum and mean, there is nothing more to do). We must use the basic codes such as for loop and while loop to do analysis.

# 2.The code
1. First I import csv. This is a package coming with Python 3.8. We use this package to read the csv file.

2. Next I define a class called border_crossing_data. It is not necessary to wrap the functions into a class. I think it looks better and    makes it easy to use repeatedly for different inputs.

3. The functions
   * read_file: Using csv.DicReader to read the data points as dictionaries into a list. At the same time, we print the the feature names      and the number of data points processed.
   
   * value_count: It's input is a list of dictionaries and a list of feature names. For a fixed feature, in general we don't know how many different values it takes (even though in this example it is easy      to see). We use this function to count the different values for a feature. For exmaple, apply this function to the entire dataset and      the feature 'Borders', we get ['US-Canada Border', 'US-Mexico Border'].
   
   * sub_lst_by_feature: Its inputs are a list of dictionaries and a dictionary. It generates a list containing data points with precribed values for certain features. For example, you can take the      value of dic to be {'Borders': 'US-Canada Border', 'Measures': 'Bus Passengers'}, then this function will pick up data points whose        border value is US-Canada and whose tranportation measure is bus passengers. This function allows us to take sum and means when we        classify our data points according to different group of features.
   
   * compt_sum: Its inputs are a list of dictionaries and a dictionary. This function computes the sum of values for the input. For example, we can take the list to be the whole dataset (self.read_file()), and the dic to be {'Borders': 'US-Canada Border', 'Measures': 'Bus Passengers'}. Then this function computes the sum of number of bus passengers crossing the US-Canada border from Jan 1996 to Dec 2019.
   
   * compt_avg: Similar to the function compt_sum, instead, we compute the average (over different portals) instead of the sum. For example, using the list of entire dataset and the dic to be {'Borders': 'US-Canada Border', 'Measures': 'Bus Passengers'}, we can compute the average of number of bus passengers over the years 1996 - 2019.
   
   * result_generate: This function compute the desired result: the sum and average of all the values according every prescribed border, date and transportation means. It stores the results (in the form of dictionaries) into a list.
   
   * report generate: It writes the result into a csv file called 'report.csv'.

# 3.The input and output
  The input is the csv file 'Border_Crossing_Entry_Data.csv' (given by you) and the output is 'report.csv'.
  
# 4.The name of the py file
  The name of the code file is border_analytics.py, according to your instruction.
