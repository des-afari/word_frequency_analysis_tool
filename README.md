The goal of this project is to build a tool that can analyze a given text document and provide insights into the frequency of words used in it. The tool will utilize Generators, CMD and Multithreading to improve performance and make the tool efficient.

Here's how the tool will work:

1. The user will specify the text file that they want to analyze using the command-line interface.
2. The tool will then read the file and create a list of all the words present in the text.
3. The tool will then analyze the frequency of each word present in the text and create a dictionary with the words and their frequency count.
4. The user can then specify if they want to see the most frequently used words, least frequently used words, or all the words and their frequency count.
5. The tool will display the requested information in the command-line interface.

Here's how you can use Generators, CMD, and Multithreading in this project:

1. Generators: Use a generator function to read the text file and generate the list of words present in the text. This will improve performance and memory usage by reading the file in chunks instead of loading the entire file into memory.
2. CMD: Use the CMD module to create a command-line interface for the tool.
3. Multithreading: Use multithreading to split the word frequency analysis function into multiple threads, which will analyze different portions of the text file simultaneously, improving performance.