# June Challenge Day 3: Two City Scheduling
# Problem:
# There are 2N people a company is planning to interview. The cost of 
# flying the i-th person to city A is costs[i][0], and the cost of flying 
# the i-th person to city B is costs[i][1].

# Return the minimum cost to fly every person to a city such that exactly 
# N people arrive in each city.

# Example 1:
# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110

# Explanation: 
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.

# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

# Note:
# 1 <= costs.length <= 100
# It is guaranteed that costs.length is even.
# 1 <= costs[i][0], costs[i][1] <= 1000

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # send all 2N people to City A and keep track of total cost
        # while sending to City A, find difference of City B - City A
        # difference will be the cost of sending someone from City B to A
        # sort based on difference
        # those with the lowest difference will yield the highest "return"
        # getting the highest return will lead to the minimum cost
        
        # runtime: O(nlogn): iterate through all 2N people (2n), sort (nlogn),
        #                    iterate through first N people (N)
        # space: O(n): store all 2N people in difference array
        
        total = 0
        differences = []
        
        for cost in costs:
            # add cost of sending everyone to city A
            total += cost[0]
            # track difference of City B - City A
            differences.append(cost[1] - cost[0])
        
        differences.sort()
        
        # calculate difference if we had sent N people to city B instead
        for i in range(0, len(differences) // 2):
            total += differences[i]
        
        return total