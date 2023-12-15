import os
import json
import csv
import pickle

def save_results_to_json(dictionary):
    with open('json_file.json', 'w', encoding='utf-8') as json_file:
        json.dump(dictionary, json_file, indent=4, separators=(',', ':'))

def save_results_to_csv(dictionary):
    data = [["Dir", "Files"]]
    for key, value in dictionary.items():
        data.append([key, value])
    with open('csv_file.csv', 'w', encoding='utf-8') as csv_f:
        write_csv = csv.writer(csv_f, dialect='excel-tab', delimiter=',')
        write_csv.writerows(data)

def save_results_to_pickle(dictionary):
    with open('pickle_file.bin', 'wb') as pickle_file:
        pickle.dump(dictionary, pickle_file)

def get_dir_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size
    
  #  return os.path.getsize(path)

def traverse_directory(directory):
    array = []
    dict_ = {}  
    count = 0
    for dir_path, dir_file, file_name in os.walk(directory):
        if count == 0:
            count +=1
        else:
            dict_['Path'] = str(dir_path)
            dict_['Type'] = 'Directory'
            dict_['Size'] = get_dir_size(dir_path)
            array.append(dict_)            
            dict_ = {}  
        if len(file_name) != 0:
            for f in file_name:               
                dict_['Path'] = str(dir_path + '/' + f)
                dict_['Type'] = 'File'
                dict_['Size'] = os.path.getsize(dir_path + '/' + f)
                array.append(dict_)            
                dict_ = {}
    return array


#[
#         {'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457}, 
#         {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21}, 
#         {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079}, 
#         {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9}, 
#         {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21}, 
#         {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85}, 
#         {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 684}, 
#         {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 342}, 
#         {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171}, 
#         {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101}, 
#         {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}
# ]


   # for dir_path, dir_file, file_name in os.walk(directory):
       # result[f'{dir_path}'] = [f'{i} = {os.path.getsize(os.path.abspath(dir_path + "/" + i))} byte' for i in file_name]
   # return result
    
if __name__ == '__main__':
    #directory = input('Input path: ')
    #result: dict = traverse_directory('New folder')
    
    #result: dict = traverse_directory(directory)
    #save_results_to_json(result)
    #save_results_to_csv(result)
    #save_results_to_pickle(result)

    result = traverse_directory('New folder')
    print('done')
    for i in result:
        print(i)



[
    {'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457}, 
    {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21}, 
    {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079}, 
    {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9}, 
    {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21}, 
    {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85}, 
    {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 684}, 
    {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 342}, 
    {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171}, 
    {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101}, 
    {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}
]


[
    {'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457}, 
 {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21}, 
 {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079}, 
 {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9}, 
 {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21}, 
 {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85}, 
 {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 171}, 
 {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 171}, 
 {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171}, 
 {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101}, 
 {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}
 ]





[
   # {'Path': 'geekbrains', 'Type': 'Directory', 'Size': 4096}, 
    {'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457}, 
    {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21}, 
    {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079}, 
    {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9}, 
    {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21}, 
    {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85}, 
    {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 4096}, 
    {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 4096}, 
    {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 4096}, 
    {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101}, 
    {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}
]
