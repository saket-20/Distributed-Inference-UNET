import requests
import os
from concurrent.futures import ThreadPoolExecutor
import timeit
import sys

url = 'http://localhost:8080/pred'

dirname = "/Dark Circle/test" #enter the directory with the images you want to process

def process_file(file1):
    if "mask" not in file1 and file1[-4:] != ".csv":
        print(file1)
        file_path = os.path.join(dirname, file1)
        with open(file_path, 'rb') as file:
            response = requests.post(url, files={'image': file})
        file_contents = response.content
        with open(file1, 'wb') as file:
            file.write(file_contents)

start_time = timeit.default_timer()
with ThreadPoolExecutor(10) as executor:
    for file1 in os.listdir(dirname):
        executor.submit(process_file, file1)
elapsed = timeit.default_timer() - start_time
print(elapsed)
