//https://leetcode.com/problems/longest-valid-parentheses/description/

/**
 * 主要思路：
 *  当是"("的时候，需要入栈。
 *  当是")"的时候，如果栈空，代表不可能从他开始是最长字串， 所以start = i+1, 标记下一个可能字串的起始位置
 *              如果栈不空，代表还有做括号可以用，则弹出一个，如果这时候栈空了，则代表有可能是()()这种形式，则i-start+1为当前结果。
 *                                                    如果栈不空，则找到弹出一个之后的栈的起始位置。是这种形式:(()(),则应获取到栈顶元素作为起始位置。
 */

/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function(s) {
    stack = [], start = 0, res = 0;
    for (var i = 0; i < s.length; i++) {
        if (s[i] == "(") {
            stack.push(i); continue;
        } 
        if (stack.length != 0) {
            stack.pop();
            if (stack.length == 0) {
                res = Math.max(i - start + 1, res);
            } else {
                res = Math.max(i - stack[stack.length-1], res);
            }
        } else {
            start = i+1;
        }
    }
    return res;
};