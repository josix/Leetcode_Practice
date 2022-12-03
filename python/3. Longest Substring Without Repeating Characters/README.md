# 3. Longest Substring Without Repeating Characters

s = "abcabcbb"

“a” -> 1
“b” -> 1
“abc” -> 3
“cab” -> 3
“bca” -> 3

3 is the max one so the answer will be 3
## Questions
### Types
Input would be the strings
Output is the length of the longest substring -> integer
### Size
The length of strings from zero to 50,000
### Range
The strings consist of letters, symbols and spaces

### Sorted
No

### Repetitive
No limit

## Coding Time
### Thoughts 1 - Brute Force
all the substrings
count their length
keeping in one hashmap -> find the max one

finding all substrings will O(N^2)
keeping in hashmap will take O(1)
=> O(N^2)
### Thoughts 2 - Improving the traversing - One pass
-> Improving the efficiency of traverse

s = "abcabcbb"

substring “a”
max_length = 1

if the length of the next substring is longer than the kept one, then go on

substring “ab”
max_length = 2
…

substring “abc”
max_length = 3

Next on is “a”, so stop updating the max_lenght, and discarding the original ‘a’ and take the newest one to build the new substring with the expectation that the new substring would be the longest one.

“abcb” -> Discard the prefix “ab” and keep “cb” as the next substring

```python
def lengthOfLongestSubstring(self, s: str) -> int:
    if not len(s):
        return 0
    max_sub_length = 0
    current_substring = “”
    substring_length = len(current_substring)
    start_pos = 0
    end_pos = 0
    while end_pos + 1 != len(s): 								# O(N)
        candidate_substring = s[start_pos: end_pos]						# <= O(N)
        if s[end_pos] not  in set(current_substring):						# <= O(N)
            current_substring += s[end_pos]							# O(1)
        elif s[end_pos] in set(current_substring):						# <= O(N)
            current_substring = current_substring[current_substring.find(s[end_pos]) + 1:] + s[end_pos]
# O(m), where m is the length to the repetitive letter + O(1)
        substring_length = len(current_substring)				# < O(N)
        max_sub_length = max(max_sub_length, substring_length) 		# O(1)
        end_pos += 1								# O(1)
    return max_sub_length
```
#### Time Complexity
O(N * M), M depends on the longest length of sbustring

Worst case O(1 + …. + N) = O(N)
Spac#### e Complexity
O(N) for keeping substring and candidate_substring
-> O(2N)

Follow up
hash map -> letter to index

