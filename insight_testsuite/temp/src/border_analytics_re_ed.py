#!/usr/bin/env python
# coding: utf-8




import csv
import sys




def to_dic(lst):
    e = {}
    for item in lst:
        key = (item['Border'], item['Date'], item['Measure'])
        if key in e:
            e[key][0] += int(item['Value'])
        else:
            e[key] = []
            e[key].append(int(item['Value']))
            e[key].append(0)
            e[key].append(0)
    return e


def get_6_to_10(s):
    return s[6:10]

def get_year_lst(d):
    result = []
    for key in d:
        x = get_6_to_10(key[1])
        if x not in result:
            result.append(x)
    return result

def get_year_1(year, dic):
    result = {}
    for key in dic:
        x = get_6_to_10(key[1])
        if x == year:
            result[key] = dic[key]
    return result

def compute_avg(dic):
    for key in dic:
        for x in dic:
            if x[0] == key[0] and x[2] == key[2] and x[1] < key[1]:
                dic[key][1] += dic[x][0]
                dic[key][2] += 1
    for key in dic:
        if dic[key][2] == 0:
            dic[key].append(0)
        else:
            dic[key].append(int(dic[key][1]/dic[key][2] + 0.5))
    return dic

def turn_in_list(d):
    result = []
    for key in d:
        dic = {}
        dic['Border'] = key[0]
        dic['Date'] = key[1]
        dic['Measure'] = key[2]
        dic['Value'] = d[key][0]
        dic['Average'] = d[key][3]
        result.append(dic)
    return result

def sort_feature(lst):
    lst = sorted(lst, key = lambda i: (i['Date'], i['Value'], i['Measure'], i['Border']), reverse = True)
    return lst





def cross_report(input_file, output_file):
    with open(input_file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            input_lst = []
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                input_lst.append(row)
                line_count += 1
            print(f'Processed {line_count} lines.')
                          
    input_dic = to_dic(input_lst)
    
    list_of_years = get_year_lst(input_dic)
    
    a_list = []
                          
    for s in list_of_years:
        a_list.append(get_year_1(s, input_dic))
    
    b_list = []
                          
    for item in a_list:
        b_list.append(sort_feature(turn_in_list(compute_avg(item))))             
                          
    c_list = []
    for item in b_list:
        c_list += item                
    
    with open(output_file, mode='w') as csv_file:
            fieldnames = ['Border', 'Date', 'Measure', 'Value', 'Average']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for item in c_list:
                writer.writerow(item)
        
    return output_file         

input_file = sys.argv[1]
output_file = sys.argv[2]



r2 = cross_report(input_file, output_file)







