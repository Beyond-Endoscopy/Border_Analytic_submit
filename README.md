# Border_Analytic_submit

## Purpose of the project

In this project a program was built to analyze the number of times certain vehicles (including passengers, pedestrians and so on) crossing the US-Canada border and the US-Mexico border. The running monthly average was also computed by this program. 

## The input dataset out put dataset

The input dataset is an excel file (.csv) about the border crossing information at US-Canada border and US-Mexico border. It has 7 features: Port Name, State, Port Code, Border, Date, Measure, Value. The output file should contain five features: Border, Date, Measure, Value (a sum, not the previously mentioned 'Value') and Average. 

## The code

First we need to know what the 'Value' is and what the 'Average' is in the output file.

The feature 'Value': For each combination of values of 'Border', 'Date', 'Measure', we sum up all the 'Value' in the input dataset over different ports. For example, we can fix a tuple: 'Border': US-Canada Border, 'Date': 12/01/2019 12:00:00 AM, 'Measure': Pedestrian, then we sum over the feature 'Value' all the data points who have the same values on this tuple in the input dataset. 

To achieve the goal of computing this sum, I created a dictionary whose keys are these triples. The value for each key is a list of length three, the first number in the list is to record this sum, the second and the third number in the list are for later use. Using with open read mode, we get a list of dictionaries from the input file. Then I use the function to_dic to create the dictionary. 

The feature 'Averate' is a little bit complicated. It is defined in the following way: For a combination of values of 'Border', 'Date', 'Measure', the 'Average' is the average of the newly defined 'Value' over all these tuples whose 'Date' are the previous months in the same year. For example, for the tuple: 'Border': US-Canada Border, 'Date': 12/01/2019 12:00:00 AM, 'Measure': Pedestrian, the 'Average' is the average of the newly defined 'Value' over all the tuples whose 'Border' value is 'US-Canada Border', 'Measure' value is 'Pedestrian' and 'Date' are '11/01/2019, ...', '10/01/2019, ...',..., '02/01/2019,...'. The goal of computing 'Average' is achieved by a series of functions, starting from 'get_6_to_10' to 'compute_avg'. 

After computing the feature 'Average', I transform the dictionary into a list of dictionaries using the function 'turn_in_list'. Since we are asked to sort the output data points according to 'Date', 'Value', 'Measure', 'Border', I used the function 'sorted' to do this sorting. 

Finally, using with open write mode to write the output data points into the report file.
