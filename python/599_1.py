class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        from collections import defaultdict
        restaurant_to_index1 = { restaurant:index for index, restaurant in enumerate(list1) }
        restaurant_to_index2 = { restaurant:index for index, restaurant in enumerate(list2) }
        common_interest = set(restaurant_to_index1) & set(restaurant_to_index2)
        ans = []
        min_index_sum = 10000
        index_sum_to_restaurants = defaultdict(list)
        for restaurant in common_interest:
            index_sum = restaurant_to_index1[restaurant] + restaurant_to_index2[restaurant]
            index_sum_to_restaurants[index_sum].append(restaurant)
            if index_sum < min_index_sum:
                min_index_sum = index_sum
        print(min_index_sum)
        return index_sum_to_restaurants[min_index_sum]
            
            
            
