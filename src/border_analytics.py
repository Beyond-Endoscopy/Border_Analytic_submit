#!/usr/bin/env python
# coding: utf-8


#Import sys and csv to read the input and write the output.

import sys
import csv



#Wrap the functions into a class.

class border_crossing_data:
    def __init__(self, csvfilename, features = None):
        self.csvfilename = csvfilename
        self.features = features
  
#Read the imput file.

    def read_file(self):
        with open(self.csvfilename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            result = []
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                result.append(row)
                line_count += 1
            print(f'Processed {line_count} lines.')
            return result

#Counting how many different values are there in a given feature.  
                          
    def value_count(self, lst = None, feature = None):
        result = []
        if lst == None:
            lst = self.read_file()
        for item in lst:
            if item[feature] not in result:
                result.append(item[feature])
        return result
 
#Picking up the data points with certain prescribed values on some given features.
                          
    def sub_lst_by_feature(self, lst = None, dic = None):
        result = []
        if lst == None:
            lst = self.read_file()
        for item in lst:
            x = True
            for s in dic.keys():
                if item[s] != dic[s]:
                   x = False
                   break
            if x == True:
                result.append(item)
        return result
  
  #Compute the sum of the feature 'Values' for the data points having certain prescribed values on some given feature.
                          
    def compt_sum(self, lst = None, dic = None):
        sum = 0
        if lst == None and dic != None:
            lst = self.sub_lst_by_feature(dic)
        for item in lst:
            sum += int(item['Value'])
        return sum

  #Compute the average of the feature 'Values' for the data points having certain prescribed values on some given feature.                       
                          
    def compt_avg(self, lst = None, dic = None):
        if lst == None and dic != None:
            lst = self.sub_lst_by_feature(dic)
        l = len(lst)
        if l == 0:
            print("You have an empty dataset!")
        else:
            return self.compt_sum(lst)//l
 
 #Generate the result.                         
                          
    def result_generate(self, lst = None):
        if lst == None:
            lst = self.read_file()
        result = []
        borders = self.value_count(lst, 'Border')
        dates = self.value_count(lst,'Date')
        measures = self.value_count(lst, 'Measure')
        for x in borders:
           for y in dates:
              for z in measures:
                dic = {}
                dic['Border'] = x
                dic['Date'] = y
                dic['Measure'] = z
                temp_l = self.sub_lst_by_feature(lst, {'Border': x, 'Date': y, 'Measure': z})
                if len(temp_l) != 0:
                    dic['Sum'] = self.compt_sum(temp_l)
                    dic['Avg'] = self.compt_avg(temp_l)
                    result.append(dic)
        return result
                          
   #Generate the report, a csv file.                       
                          
    def report_generate(self, output_file, result = None):
        if result == None:
            result = self.result_generate()
        
        with open(output_file, mode='w') as csv_file:
            fieldnames = ['Border', 'Date', 'Measure', 'Sum', 'Avg']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for item in result:
               writer.writerow(item)


#Testing the code on the given dataset.                          
                          
input_file = sys.argv[1]
output_file = sys.argv[2]


all_data = border_crossing_data(input_file)





all_data.report_generate()

