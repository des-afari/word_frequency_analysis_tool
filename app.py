import concurrent.futures
import time
from collections import Counter 


def word_count(line):
    new_list = line.split(' ')
    result = Counter(new_list)
    return result
    

# generator function
def frequency_analysis_generator():
    with open('file.txt', mode='r', encoding='utf-8') as file:
       with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        
        for line in file:
            future = executor.submit(word_count, line)
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            yield future.result()


for value in frequency_analysis_generator():
    print(value)