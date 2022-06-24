https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/929000/Recursive-solution-long-explanation


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.helper(1, n)


    def helper(self, start, end):
        if start > end: # edge case, see exposition below
            return [None] 
        
        all_trees = [] # list of all unique BSTs
        for curRootVal in range(start, end+1): # generate all roots using list [start, end]
			# recursively get list of subtrees less than curRoot (a BST must have left subtrees less than the root)
            all_left_subtrees = self.helper(start, curRootVal-1)
			
			# recursively get list of subtrees greater than curRoot (a BST must have right subtrees greater than the root)
            all_right_subtrees = self.helper(curRootVal+1, end) 
			
            for left_subtree in all_left_subtrees:   # get each possible left subtree
                for right_subtree in all_right_subtrees: # get each possible right subtree
                    # create root node with each combination of left and right subtrees
                    curRoot = TreeNode(curRootVal) 
                    curRoot.left = left_subtree
                    curRoot.right = right_subtree
					
					# curRoot is now the root of a BST
                    all_trees.append(curRoot)
		
        return all_trees


# C++ code

class Solution {
public:
    
    vector<TreeNode*> dfs(int start, int end){
        if(start >  end)
            return vector<TreeNode*>{NULL};
        
        
        vector<TreeNode*> res;
        
        for(int i = start; i <= end; i++){
            vector<TreeNode*> left = dfs(start, i - 1);
            vector<TreeNode*> right = dfs(i + 1, end);
            
            for(auto l : left){
                for(auto r : right){
                    TreeNode* root = new TreeNode(i);
                    root->left = l;
                    root->right = r;
                    res.push_back(root);
                }
            }
        }
        return res;

    }
    
    vector<TreeNode*> generateTrees(int n) {
        return dfs(1, n);
    }
};