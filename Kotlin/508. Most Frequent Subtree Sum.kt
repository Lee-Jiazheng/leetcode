// Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

// Examples 1
// Input:

//   5
//  /  \
// 2   -3
// return [2, -3, 4], since all the values happen only once, return all of them in any order.
// Examples 2
// Input:

//   5
//  /  \
// 2   -5
// return [2], since 2 happens twice, however -5 only occur once.
// Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.

/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int = 0) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    val res = mutableListOf<Int>()
    fun findFrequentTreeSum(root: TreeNode?): IntArray {
        getSums(root)
        var mp = mutableMapOf<Int, Int>()
        for (r in res) {
            if (r in mp) mp[r] = mp[r]!!.plus(1) else mp[r] = 1
        }
        val _max = mp.values.max()
        val _res = mutableListOf<Int>()
        for (_num in mp.keys) {
            if (mp[_num] == _max) _res.add(_num)
        }
        println("$_res, $_max, $mp")
        return _res.toIntArray()
    }

    fun getSums(root: TreeNode?): Int {
        if (root == null) return 0
        val _sum = getSums(root.left) + getSums(root.right) + root.`val`
        res.add(_sum)
        return _sum
    }
}