__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

# Assigment Files
# Dirk-Jan Vethaak
import os
from pathlib import Path
import glob
import time

from os import listdir
from os.path import isfile, join

import zipfile

# neded \c due to windows folder diffrence in win10 and wincpy check
def get_cache_dir():
    script_dir = os.path.dirname(__file__)
    new_dir = r'{}\cache'.format(script_dir)
    return new_dir 

def clean_cache():
    # Show current dir path
    script_dir = os.path.dirname(__file__)
    print(f"Python Script dir: {script_dir}")

  

    # check if folder exits
    p= Path(get_cache_dir())
    

    if (p.exists()):
        # ifexist clean folder
        print("clean folder")
        files = glob.glob(get_cache_dir()+"/*")
        for f in files:
            #print(f)
            os.remove(f)
        
            

    else :
        # Make new folder cache
        print("make new folder")
        os.makedirs(get_cache_dir())
 


def cache_zip(zip_path,cache_dir):
    #unzip zip in cache folder

      print("unzip folder")
      clean_cache()
      zip = zipfile.ZipFile(zip_path)
      zip.extractall(path=cache_dir)

      # give time to update folder
      time.sleep(5)


def cached_files():
    #return list of files but no folders
    print("get list of chached file")
    onlyfiles = [os.path.join(get_cache_dir()+"\\", f) for f in os.listdir(get_cache_dir()) if 
    os.path.isfile(os.path.join(get_cache_dir(), f))]
    
    print(onlyfiles) 
    return onlyfiles

def find_password(file_list):
    #Search password in files
    print("search password")
    
    password = ""

    for datafile in file_list:
        #read file and close directly
        with open(datafile) as f:
            lines = f.readlines()
        for line in lines:
            if "password" in line:
                
                print(f"Found Password in : {datafile}")
                # extract password from line
                password = line.split()[1]


    print(password)

    return password


# Test program
#print("Start:")
clean_cache()
#cache_zip("xxxxx", " xxxx  ") removed due privacy
find_password(cached_files())
#print("end")


