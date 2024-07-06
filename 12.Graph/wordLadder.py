from collections import deque
from typing import List

def word_ladder_length(beginWord: str, endWord: str, wordList: List[str]) -> int:
    # Create a set of wordList for fast lookup
    word_set = set(wordList)
    if endWord not in word_set:
        return 0

    # BFS queue: (current_word, current_length)
    queue = deque([(beginWord, 1)])

    while queue:
        current_word, current_length = queue.popleft()

        # Check all possible transformations of current_word
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + c + current_word[i+1:]
                
                # When next_word is the endWord
                if next_word == endWord:
                    return current_length + 1
                
                # If the transformed word is in the word set
                if next_word in word_set:
                    word_set.remove(next_word)  # Remove to prevent revisiting
                    queue.append((next_word, current_length + 1))

    # If endWord is not reachable
    return 0

# Example usage
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
output = word_ladder_length(beginWord, endWord, wordList)
print(output)  # Expected output: 5
