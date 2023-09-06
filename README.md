# Largest Compounded Word Finder

This project aims to find the largest and second largest compounded words from a list of words. A compounded word is a word that is made up of two or more other words in the list.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [How it works](#how-it-works)
- [Efficiency and Complexity Analysis](#efficiency-and-complexity-analysis)

## Features

- Efficiently finds the largest and second largest compounded words.
- Uses a Trie data structure for efficient word insertion and search.
- Implements memoization to cache results and optimize recursive searches.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/word-search.git
   ```
2. Navigate to the project directory:
   ```bash
   cd word-search
   ```

## Usage

1. Add your list of words to a text file with one word per line. Set the name of the input file accordingly in the code.
2. Run the main code:
   ```bash
   python word_search.py
   ```
3. The output will display the two largest compounded words and the time taken to find them.

## Testing

Unit tests are provided to ensure the functionality of the Trie data structure and the compounded word search.

1. To run the tests, execute:
   ```bash
   python test_word_search.py
   ```

## How It Works

### Trie Data Structure

A Trie (or Prefix Tree) is a tree-like data structure that is used to store a dynamic set of strings. It's particularly useful for scenarios where there are large datasets of strings that need to be searched through, like in this project.

### Memoization

Memoization is an optimization technique used to speed up programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again.

## Efficiency and Complexity Analysis

### Time Complexity

1. **Trie Insertion**: Inserting all words into the Trie has a time complexity of O(n x m), where n is the number of words and m is the average length of a word.

2. **Sorting the Words**: Sorting the words by length ensures that we check the longest words first. The time complexity for sorting is O(n log n).

3. **Checking Each Word**: After sorting, we check each word to see if it's compounded using the Trie-based approach. In the worst case, this is O(n x m).

Combining all the above, the overall time complexity of the solution is O(n x m + n log n), which is dominated by O(n x m) for large inputs.

### Space Complexity

1. **Trie Storage**: The Trie will store all the words. In the worst case, if there are no common prefixes, the space complexity will be O(n x m).

2. **Memoization Cache**: The cache will store results for each unique substring encountered during the search. In the worst case, this can be O(m) for each word, leading to a total of O(n x m).

3. **Word Storage**: The list of words itself will take O(n x m) space.

4. **Miscellaneous**: Other variables and data structures used in the program, like the list of compounded words, will take up additional space but will not have a significant impact on the overall space complexity.

Combining all the above, the overall space complexity of the solution is O(n x m).

### Efficiency Considerations

- **Trie**: The Trie data structure ensures that words with common prefixes share storage, making it a space-efficient way to store and search for words.

- **Memoization**: By caching results of previous searches, the algorithm avoids redundant calculations, making it more time-efficient, especially for words with many common prefixes.

- **Sorting**: Sorting the words by length ensures that the longest words are checked first, which is crucial for finding the largest and second largest compounded words without checking every word.
