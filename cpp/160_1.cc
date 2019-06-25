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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if(headA == NULL or headB == NULL) return NULL;
        int headA_length = 0;
        int headB_length = 0;
        ListNode* current = headA;
        while(current) {
            current = current -> next;
            headA_length++;
        }
        current = headB;
        while(current) {
            current = current -> next;
            headB_length++;
        }
        int diff = headB_length < headA_length ? headA_length - headB_length: headB_length - headA_length;
        cout << diff <<endl;
        if (headB_length < headA_length) {
            cout << "B < A" << endl;
            ListNode* first = headB;
            ListNode* second = headA;
            for(int i = 0 ; i< diff; i++)second = second -> next;
            while(first != second && first && second){
                first = first -> next;
                second = second -> next;
            }
            if (first == NULL || second == NULL){
                return NULL;}
            else{
                return first;
            }
        } else if (headB_length > headA_length) {
            cout << "B > A" << endl;
            ListNode* first = headA;
            ListNode* second = headB;
            for(int i = 0 ; i< diff; i++)second = second -> next;
            while(first != second && first && second){
                first = first -> next;
                second = second -> next;
            }
            if (first == NULL || second == NULL){
                return NULL;}
            else{
                return first;
            }
        } else {
            cout << "Same Len" << endl;
            ListNode* first = headA;
            ListNode* second = headB;
            while(first != second && first && second){
                first = first -> next;
                second = second -> next;
            }
            if (first == NULL || second == NULL){
                return NULL;}
            else{
                return first;
            }
        }
    }
};
