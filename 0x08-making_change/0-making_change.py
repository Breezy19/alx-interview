#!/usr/bin/python3
"""
Module for making change using dynamic programming
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    """
    if total < 1:
        return 0

    # Initialize a list to store the minimum number of coins for each amount
    # The length of dp is total + 1 to include 0 as the base case
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed to make 0 total
    dp[0] = 0

    # Iterate through all possible amounts from 1 to total
    for amount in range(1, total + 1):
        # Iterate through all available coin values
        for coin in coins:
            # If the coin value is less than or equal to the current amount
            if coin <= amount:
                # Update the minimum number of coins needed
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still float('inf'), it means the total cannot be met
    if dp[total] == float('inf'):
        return -1

    return dp[total]


if __name__ == "__main__":
    # Example usage
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))