/**
 * @param {number} num
 * @return {number[]}
 */

var countBits = function(num) {
    var res = [0], cnt = 0
    while (cnt < num) {
        length = res.length
        for (var i=0; i<length && cnt<num; ++i, ++cnt) {
            res.push(res[i]+1)
        }
    }
    return res
};

/**
 * If number is 0, =>0
 * If number is 1, =>1
 * If number is 2, =>1
 * If number is 3, =>2
 * ...
 * The rule is  [1] = [0] + 1
 *              [2, 3] = [0, 1] + 1
 * 
 * Also, we can judge it by odd/even...(golang)
 */