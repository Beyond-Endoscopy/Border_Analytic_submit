# Border_Analytic_submit

$ Purpose of the project

In this project a program was built to analyzing the number of times certain of vehicles (inclusing passengers, pedestrians and so on) crossing the US-Canada border and the US-Mexico border. The running monthly average was also built. 

# The input dataset out put dataset

The input dataset is an excel file (.csv) about the border crossing information at US-Canada border and US-Mexico border. It has 7 features: Port Name, State, Port Code, Border, Date, Measure, Value. The output file should contain five features: Border, Date, Measure, Value (a sum, not the previously mentioned 'Value') and Average. 

# The code

The Value feature in the output dataset is the following: for each combination of Border, Date, Measure, sum up the Value in the input dataset over different Ports. Basically this is do the groupby operation on the input dataset according the combination of Border, Date, Measure, and then sum the Value (This is the way to do it in MySQL). Here I build a dictionary using the three tuple （Border: ...,Date:..., Measure:...) as the keys. for each key, its value is a list of three numbers: [Value (the sum needed), 0, 0]. The two zeros for later use, when we compute the Average.

The Average means the average of the total crossings of the vehicle at the same border in all the months previous to the month in the same year. To do this, first I build a dictionary for each year, using the function get_year_1. Then use the function compute_avg to get the Average. 

Finally, build a list of dictionaries of the form {Border:..., Date:..., Measure:..., Value:..., Average:...} from the above dictionaries. Using with open write mode to write this list of dictionaries into the report file.

