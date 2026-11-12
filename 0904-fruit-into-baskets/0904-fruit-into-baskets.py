from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left = 0
        max_fruits = 0

        fruit_count = defaultdict(int)
        
        for right, fruit in enumerate(fruits):
            fruit_count[fruit] += 1

            while len(fruit_count) > 2:
                left_fruit = fruits[left]
                fruit_count[left_fruit] -= 1

                if fruit_count[left_fruit] == 0:
                    del fruit_count[left_fruit] 
                
                left += 1

            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits
