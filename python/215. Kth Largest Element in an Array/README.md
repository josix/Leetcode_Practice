# 215. Kth Largest Element in an Array
Given one array with N elements and one integer k, return the k-th largest number in the array.
## Questions
### Types
The input types: array would be array of integers and k would be integer
The output woud be one integer
### Sizes
The length of given array would be range from 1 to one hundred thousand 
### Range
The range of each number in the array would be -10000 to 10000
The range of k would be from 1 <=  numbers of array <= 100,000
### Repetitive
Yes the array would contain repetitive numbers
### Sorted
No the given array is not sorted
### Editable
Yes you can edit the array in place
### Error Handling
What if no k largest in that array, e.g k=10 arr=[1,2]? No, there’s no such case in this question.

## Coding Time
### Thoughts 1 - Heap
Because I need to keep the numbers in order and get the top k largest number in that array, I will build one heap at first and put the elements in the heap so that I could keep the order all the time. And I will take O(n log n) time complexity. And after all elements are in that heap. I will pop item from that heap and get the K largest one when I pop k times.

```python
def find_k_largest_items(array:list[int], k:int) -> int:
    import heapq
    hq = []
    for num in array: 					# O(N)
        heapq.heappush(hq, -num) 			# O(logN)
    for _ in range(k - 1):				# O(k)
        heapq.heappop(hq)				# O(logN)
    return -heapq.heappop(hq)				# O(logN)
```
#### Time Complexity
heappush would take O(logN) and for all n numbers it would take O(N log N)
and for each heappop it would take O(logN), the worst case of taking the largest one item would be O(N log N) when the item is the largest one in that array.
So tht complexity would be O(n log n)

#### Space Complexity
one heap array would take O(N), that’s all




