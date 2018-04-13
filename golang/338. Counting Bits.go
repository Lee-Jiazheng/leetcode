package golang

/** 
* 从1开始，每个数子的二进制位，等于不算最低位的二进制1个数+奇数偶数判断最低位1的个数。
*/
func countBits(num int) []int {
    res := []int{0}
    for i := 1; i <= num; i++ {
        res = append(res, res[i>>1] + i%2)
    }
    return res
}