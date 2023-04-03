import concurrent.futures
import time
from collections import Counter 


def word_count(line):
    new_list = line.split(' ')
    result = Counter(new_list)
    return result
    

# generator function
def frequency_analysis_generator(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
       with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        
        for line in file:
            future = executor.submit(word_count, line)
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            yield future.result()

if __name__ == '__main__':
    print("To run file, you need to type the following command into you terminal")
    print("python console.py")
    print("and then follow the instructions")
    