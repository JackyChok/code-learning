class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candies = [1] * n 

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        return sum(candies)

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    ratings1 = [1, 0, 2]
    result1 = solution.candy(ratings1)
    print(result1)  # Output should be 5

    # Test case 2
    ratings2 = [1, 2, 2]
    result2 = solution.candy(ratings2)
    print(result2)  # Output should be 4
