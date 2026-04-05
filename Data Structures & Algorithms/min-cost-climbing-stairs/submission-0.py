class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
            if len(cost) <3:
                return min(cost)
            prevCost = cost[1]
            prevPervCost=cost[0]

            for i in range(2,len(cost)):
                tmp=prevCost
                prevCost=min(tmp+cost[i],prevPervCost+cost[i])
                prevPervCost=tmp

            return min(prevCost,prevPervCost)
        