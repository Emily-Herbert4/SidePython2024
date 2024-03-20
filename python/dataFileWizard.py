import os 
import datetime

# Parent Directory path 
parent_dir = "C:/college/Spring2024/Quantum Computing/data"
# Directory 
date = datetime.datetime.now()
directory = f"data{date.month}-{date.day}-{date.year}"
# Path 

def create_folder():
    path = os.path.join(parent_dir, directory) 
    try:
        os.mkdir(path)
        print("Directory '% s' created" % directory) 
        
    except OSError as error: 
        if os.path.exists(path) is False:
            print("Something is off ")
            print(error)   

def store_plots(plotname):
    path = '/Some/path/to/Pics2'
    try:
        path =os.path.join(path, plotname)
    except OSError as error:
        if os.path.exists(path):
            os.remove(path)
            path =os.path.join(path, plotname)
        print(error)   