"""Compute the longest common subsequence of two strings."""

# Add the three algorithms that compute the longest common
# subsequence (LCS) of two strings that contain either characters or
# numbers. Make sure to add the required function signatures and
# documentation to ensure that the code is clear and understandable.
# You must add comments that explain the purpose of each of the key
# statements inside of each of the LCS algorithms.


def lcs_recursive(str1: str, str2: str) -> str:
    """Compute the LCS of two strings using a recursive approach."""

    def helper(i: int, j: int) -> str:
        # Base case: if either string is empty, return an empty string
        if i == 0 or j == 0:
            return ""
        # If the characters match, include this character in the LCS
        if str1[i - 1] == str2[j - 1]:
            return helper(i - 1, j - 1) + str1[i - 1]
        # Otherwise, find the LCS by excluding one character from either string
        else:
            lcs1 = helper(i - 1, j)
            lcs2 = helper(i, j - 1)
            return lcs1 if len(lcs1) > len(lcs2) else lcs2

    return helper(len(str1), len(str2))


def lcs_dynamic(str1: str, str2: str) -> str:
    """Compute the LCS of two strings using dynamic programming."""
    m, n = len(str1), len(str2)
    # Create a 2D table to store the length of LCS
    dp = [["" for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill the table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                # If characters match, add to the LCS
                dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
            else:
                # Otherwise, take the longer LCS from the previous subproblems
                dp[i][j] = (
                    dp[i - 1][j]
                    if len(dp[i - 1][j]) > len(dp[i][j - 1])
                    else dp[i][j - 1]
                )

    return dp[m][n]


def lcs_calculate(str1: str, str2: str) -> str:
    """Compute the LCS of two strings using a custom iterative approach."""
    # Use a set to store all subsequences of str1
    subsequences = set()

    # Generate all subsequences of str1
    def generate_subsequences(s: str, index: int, current: str):
        if index == len(s):
            subsequences.add(current)
            return
        generate_subsequences(
            s, index + 1, current + s[index]
        )  # Include the character
        generate_subsequences(s, index + 1, current)  # Exclude the character

    generate_subsequences(str1, 0, "")

    # Find the longest subsequence of str1 that is also a subsequence of str2
    longest = ""
    for sub in subsequences:
        it = iter(str2)
        if all(char in it for char in sub) and len(sub) > len(longest):
            longest = sub

    return longest
