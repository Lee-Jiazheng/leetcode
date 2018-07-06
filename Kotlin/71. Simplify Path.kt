/*
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

*/


class Solution {
    fun simplifyPath(path: String): String {
        val temp = mutableListOf<String>()
        for (p in path.split("/")) {
            when (p) {
                ".." -> if (temp.size != 0) temp.removeAt(temp.size-1) else temp.size
                ".", "" -> temp.size
                else -> temp.add(p)
            }
        }
        return temp.filter { it != "" }.joinToString("/", "/")
    }
} 