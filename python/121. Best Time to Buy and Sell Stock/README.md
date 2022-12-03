# 121. Best Time to Buy and Sell Stock
Given an array with integers that represents the stock price each day, and your program is required to find out two days for buying one share and sell out that stock to maximize the profit. 

## Questions
### Types
The input would be one array of integers
The return value would be one integer representing the max profit

### Sizes

The length of the array would be range from 1 to 100,000

### Ranges
The range of each value in the array would be from 0 to 10000

### Repetitive
The numbers may be repetitive 

### Sorted
No, the array is not sorted
### Editable (Inplace)
Yes
### Error Handling
What if there’s no max profit in the array? Return zero.

## Coding Time
### Thoughts 1 - Sliding Window
For the given questions, I need to select two days that are sufficient to max the profits. So the most efficient way is I can traverse this array in one pass and make the profit as monotonic. And that’s the trick to do the one pass.
7, 6, 4, 3, 1
7, 1, 5, 3, 6, 4
```python
def best_time_to_buy_and_sell(array: list[int]) -> int:
    current_profit = 0
    best_start_day = 0
    best_end_day = 0
    current_end_day = 0
    while current_end_day + 1 != len(array): 					# O(N)
        day_profit = array[current_end_day] - array[best_start_day]		# O(1)
        if day_profit > current_profit:						# O(1)
            best_end_day = current_end_day
        elif array[current_end_day] < array[best_start_day]:
            best_start_day = current_end_day
        current_profit = max(current_profit, day_profit)
        current_end_day += 1
    return current_profit
```

#### Time Complexity
since all manipulation is one pass on the array so the time complexity is O(N)

#### Space Complexity
only use constant numbers of variable so it is O(1)

