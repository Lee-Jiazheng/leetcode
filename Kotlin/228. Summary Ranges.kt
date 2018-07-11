// Given a sorted integer array without duplicates, return the summary of its ranges.

// Example 1:

// Input:  [0,1,2,4,5,7]
// Output: ["0->2","4->5","7"]
// Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

// Example 2:

// Input:  [0,2,3,4,6,8,9]
// Output: ["0","2->4","6","8->9"]
// Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

class Solution {
    fun summaryRanges(nums: IntArray): List<String> {
        var pointer: Int = 0
        val res = mutableListOf<String>()
        for (index in 1..nums.size) {
            if (index != nums.size && nums[index] - nums[index-1] == 1) continue
            when {
                index -1 == pointer -> res.add(nums[pointer].toString())
                else -> res.add("${nums[pointer]}->${nums[index-1]}")
            }      
            pointer = index
        }
        return res
    }
}