/**
 * @param {string} S
 * @return {number[]}
 */
var partitionLabels = function(S) {
    var pos = {}
    for (var i = 0; i < S.length; ++i) {
        pos[S[i]] = i
    }
    var end = 0, start = -1, res = []
    for (var i = 0; i < S.length; ++i) {
        // 记录到S[i]的时候，需要更新end, 确保下次分割位置是多过end的。
        if ((end = Math.max(end, pos[S[i]])) == i) {
            res.push(end - start)
            start = end
        }
    }
    return res
}