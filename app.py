import concurrent.futures
import time


def word_count(line):
    return line
    

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