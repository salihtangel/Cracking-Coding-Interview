
  struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };
#include<iostream> 
#include<string.h>
#include <stdlib.h>     /* atoi */
using namespace std;

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        char arr1 [100];
        char arr2 [100];
        int i = 99;
        while(l1 != NULL && l2 != NULL){
            //cout<<l1->val;
            //cout<<l2->val;
            arr1[i] = l1->val + '0';
            arr2[i] = l2 ->val + '0';

            l1 = l1->next;
            l2 = l2->next;
            i--;
        }

  
        int x = atoi(arr1);
        int y = atoi(arr2);
        cout<<x;
        cout<<"sasa";

        return l1 ;      
    }
};

int main(){
    ListNode* l1;
    l1.val =
    addTwoNumbers();
    return 1;
}