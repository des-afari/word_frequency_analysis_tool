# generator function
def frequency_analysis_generator():
    with open('test.txt', mode='r', encoding='utf-8') as file:
        for line in file:
            yield line


result = frequency_analysis_generator()
