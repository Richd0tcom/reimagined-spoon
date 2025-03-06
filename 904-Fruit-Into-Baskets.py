''' 
904. Fruit Into Baskets (MEDIUM)

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
 

Constraints:

1 <= fruits.length <= 10^5
0 <= fruits[i] < fruits.length'''


from typing import List


def totalFruit(fruits: List[int]) -> int:
    ''' 
    we will use the sliding window approach to solve this problem.

    we will keep a dictionary of the fruits and their count.
    we will keep a left and right pointer.
    we will move the right pointer until we have more than two fruits in the dictionary.
        if we have more than two fruit in the dictionary, we will move the left pointer until we have only two fruits in the dictionary. moving the left pointer we will decrement the fruit count and if the count is 0, we will remove the fruit from the dictionary.
    at each step, we will update the maximum length.
    '''
    fruit_count = {}

    left = 0
    max_length = 0

    for right in range(len(fruits)):
        fruit = fruits[right]
        fruit_count[fruit] = fruit_count.get(fruit, 0) + 1

        while len(fruit_count.keys()) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]

            left+=1

        max_length = max(max_length, right-left +1)

    return max_length

print(totalFruit([1,2,1]))

