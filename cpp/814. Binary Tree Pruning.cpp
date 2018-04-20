/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

 // 注意传引用
class Solution {
public:
    TreeNode* pruneTree(TreeNode* root) {
        Find(root);
        return root;
    }
    
private:
    void Find(TreeNode *&root) {
        if (!hasOne(root)) {
            root = NULL; return;
        } else {
            Find(root->left);
            Find(root->right);
        }
    }
    
    bool hasOne(TreeNode *node) {
        if (!node) return false;
        if (node->val == 1) return true;
        return hasOne(node->left) || hasOne(node->right);
    }
};