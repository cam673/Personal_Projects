/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* removeLeafNodes(TreeNode* root, int target) {
        TreeNode* tree = root;
        
        leafDelete(tree, target);
        
        return tree;
        
    }
    
    void leafDelete(TreeNode* leaf, int target)
    {
        if(leaf->left != nullptr)
        {
            leafDelete(leaf->left, target);
        }
        
        if(leaf->right != nullptr)
        {
            leafDelete(leaf->right, target);
        }
        
        if(leaf->left == nullptr && leaf->right == nullptr)
        {
            if(leaf->val == target)
            {
                delete leaf;
            }
        }
    }
};
