/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == NULL || k == 0)return head;
        int length = 0;
        ListNode *current = head;
        while(current){
            current = current -> next;
            length++;
        }
        cout << length << endl;
        k = k % length;
        ListNode *first = head;
        ListNode *second = head;
        for (int i = 0; i < k ;i++){
            if (second -> next != NULL){
                second = second -> next;
            } else {
                second = head;
            }
        }
        if (second == first) return head;
        ListNode *last_second, *last_first;
        while (second != NULL){
            last_second = second;
            last_first = first;
            first = first -> next;
            second = second -> next;
        }
        last_first -> next = NULL;
        last_second -> next = head;
        head = first;
        
        return head;
    }
};
