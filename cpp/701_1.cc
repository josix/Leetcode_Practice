class MyLinkedList {
private:
    typedef struct Node{
        int val;
        Node *next;
    } ListNode;
    ListNode* head = NULL;
    int length = 0;
public:
    /** Initialize your data structure here. */
    MyLinkedList() {
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        if (index >= this -> length || index < 0) return -1;
        ListNode* current = this -> head;
        for(int i = 0 ; i < index; i++){
            current = current -> next;
        }
        return current -> val;
        
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        ListNode* new_node = new ListNode;
        new_node -> val = val;
        if(this -> head == NULL){
            this -> head = new_node;
            this -> head -> next = NULL;
        } else {
            new_node -> next = this -> head;
            this -> head = new_node ;
        }
        this -> length++;
        // ListNode* current2 = this -> head;
        // for(int i = 0 ; i<this -> length; i++){
        //     cout << current2 -> val << endl;
        //     current2 = current2 -> next;
        // }
        // cout << "end" << endl;        
        
    }
    
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
        ListNode* new_node = new ListNode;
        new_node -> val = val;
        new_node -> next = NULL;
        ListNode* current = this -> head;
        for(int i = 0; i < this -> length - 1 ;i++){
            current = current -> next;
        }
        current -> next = new_node;
        this -> length++;
        // ListNode* current2 = this -> head;
        // for(int i = 0 ; i<this -> length; i++){
        //     cout << current2 -> val << endl;
        //     current2 = current2 -> next;
        // }
        // cout << "end" << endl;        
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {
        if (index < 0){
            index = 0;
        }
        if (index > this -> length) return;
        if (index == 0){
            this -> addAtHead(val);
        } else if (index == this -> length){
            this -> addAtTail(val);
        } else{
            ListNode* new_node = new ListNode;
            new_node -> val = val;
            ListNode* current = this -> head;
            for(int i = 0; i < index - 1; i++ ){
                current = current -> next;
            }
            ListNode* tmp = current -> next;
            current -> next = new_node;
            new_node -> next = tmp;
            this -> length++;
        }
        // ListNode* current2 = this -> head;
        // for(int i = 0 ; i<this -> length; i++){
        //     cout << current2 -> val << endl;
        //     current2 = current2 -> next;
        // }
        // cout << "end" << endl;        
 
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {
        if (index >= this -> length || index < 0) return;
        if (index == 0){
            ListNode* tmp = this -> head;
            this -> head = tmp -> next;
            delete tmp;
        }else if (index == this -> length - 1){
            ListNode* current = this -> head;
            for(int i = 0; i < index;i++){
                current = current -> next;
            }
            delete current -> next;
            current -> next = NULL;
        }else{
            ListNode* current = this -> head;
            for(int i = 0; i < index - 1;i++){
                current = current -> next;
            }
            ListNode* tmp = current -> next;
            current -> next = current -> next -> next;
            delete tmp;
        }
        this -> length--;
        // ListNode* current2 = this -> head;
        // for(int i = 0 ; i<this -> length; i++){
        //     cout << current2 -> val << endl;
        //     current2 = current2 -> next;
        // }
        // cout << "end" << endl;    
       
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */
