/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        ListNode* current = head;
        int length = 0;
        while(current){
            current = current -> next;
            length++;
        }
        cout << length << endl;
        return this -> build_tree(head, length);
    }
    TreeNode* build_tree(ListNode* head, int length){
        if(length == 0) return NULL;
        TreeNode* root = new TreeNode(0);
        ListNode* current = head;
        for(int i = 0 ; i < length / 2;i++){
            current = current -> next;
        }
        // cout << "current: " << current -> val << "length: " << length << endl;
        root -> val = current -> val;
        root -> left = this -> build_tree(head, length / 2);
        if (length == 1){
            root -> right = NULL;
        } else{
            root -> right = this -> build_tree(current -> next, length - length / 2 - 1);
        }
        return root;
    }
};
