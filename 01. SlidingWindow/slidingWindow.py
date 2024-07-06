# Sliding Window Template
# Problem: Longest Substring Without Repeating Characters

def length_of_longest_substring(input_string: str) -> int:
    char_index = {}
    left = 0
    max_length = 0
    
    for right in range(len(input_string)):
        if input_string[right] in char_index:
            left = max(left, char_index[input_string[right]] + 1)
        char_index[input_string[right]] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Unit tests
assert length_of_longest_substring("abcabcbb") == 3
assert length_of_longest_substring("bbbbb") == 1
assert length_of_longest_substring("pwwkew") == 3
