#include <iostream>
using namespace std;


int fibonacci2(int i, int memo[]) {
    
    if (i == 0 || i == 1) return i;


    if (memo[i] == 0) {
        memo[i] = fibonacci2(i - 1, memo)+ fibonacci2(i - 2, memo);
    }
    return memo[i];
}

int fibonacci(int n) {

    return fibonacci2(n, new int[n + 1]);

}

int main(){

    cout<<fibonacci(6);
    cout<<"salihtangeldsdsdsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss";

    return 1;
}