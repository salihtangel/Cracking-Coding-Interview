#include <iostream>
using namespace std;


int fibonaccii(int i, int memo[]) {

    if (i == 0 || i == 1) return i;


    if (memo[i] == 0) {
        memo[i] = fibonaccii(i - 1, memo)+ fibonaccii(i - 2, memo);
    }
    return memo[i];
}

int fibonacci(int n) {

    return fibonaccii(n, new int[n + 1]);

}



int main (){

    cout<<fibonacci(5);
}