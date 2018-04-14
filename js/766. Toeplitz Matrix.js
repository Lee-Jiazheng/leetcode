// Easy
// 遍历矩阵，是否与右下数字相同。
// 尽管宏观是每条线判断， 微观仍是两个数字。


/**
 * @param {number[][]} matrix
 * @return {boolean}
 */
var isToeplitzMatrix = function(matrix) {
    for (var row = 0; row < matrix.length - 1; row++) {
        for(var col = 0; col < matrix[row].length - 1; col++) {
            if (matrix[row][col] != matrix[row+1][col+1]) { return false;}
        }
    }
    return true;
};