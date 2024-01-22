import main
import os
import time
import matplotlib.pyplot as plt

def get_data(file_types,benchmark_data):
    time_data={}
    size_data={}
    for file_type in file_types:
        time_data[file_type]=[]
        size_data[file_type]=[]
        for num_years in benchmark_data:
            symbol_name='SBIN'
            df=main.get_stock_data(symbol_name,num_years)
            entries=df.shape[0]
            time_taken,size_taken=zip(*main.print_stock_data(df,[file_type],symbol_name))
            time_data[file_type].append(time_taken[0]*100/entries)
            size_data[file_type].append(size_taken[0]*100/entries)
        time_data[file_type]= sum(time_data[file_type])/len(time_data[file_type])
        size_data[file_type]= sum(size_data[file_type])/len(size_data[file_type])
    return time_data,size_data

def benchmark_time_data(time_data, file_name):
    types=list(time_data.keys())
    times=list(time_data.values())
    types_without_txt=types[:-1]
    times_without_txt=times[:-1]
    plt.bar(types,times)
    plt.xlabel('File type')
    plt.ylabel('Time taken per 100 entries (milliseconds)')
    plt.title('Time taken vs File type')
    plt.savefig(file_name)
    plt.clf()

    plt.bar(types_without_txt,times_without_txt)
    plt.xlabel('File type')
    plt.ylabel('Time taken per 100 entries (milliseconds)')
    plt.title('Time taken vs File type')
    plt.savefig('time_without_txt.png')
    plt.clf()

def benchmark_size_data(size_data,file_name):
    types=list(size_data.keys())
    sizes=list(size_data.values())
    plt.bar(types,sizes)
    plt.xlabel('File type')
    plt.ylabel('Size per 100 entries (KB)')
    plt.title('Size vs File type')
    plt.savefig(file_name)
    plt.clf()

file_types=['csv','parquet','pickle','json','feather','txt']

benchmark_data = [1,3,6,8,10]
time_data,size_data=get_data(file_types,benchmark_data)
benchmark_time_data(time_data,'time.png')
benchmark_size_data(size_data,'size.png')


    

    


    

