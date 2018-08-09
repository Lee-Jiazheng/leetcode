// Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

// Example 1:

// Input: n = 12
// Output: 3 
// Explanation: 12 = 4 + 4 + 4.

// Example 2:

// Input: n = 13
// Output: 2
// Explanation: 13 = 4 + 9.

func numSquares(n int) int {
    dp := make([]int, n+1)
    for i := 1; i <= n; i++ {
        min := -1
        for j := 1; j <= i; j++ {
            if (i - j*j < 0) { break }
            cur := 1 + dp[i-j*j]
            if (min == -1 || cur < min) { min = cur } 
        }
        dp[i] = min
    }
    return dp[n]
}