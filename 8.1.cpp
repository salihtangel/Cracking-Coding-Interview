#include <iostream>
using namespace std;


int stairway2(int i, int memo[]) {

    if (i == 1 ) return 1;
    if (i == 2 ) return 2;
    if (i == 3 ) return 4;
      

    //belirli bir oranti bulmakg gerekiyor.
    //icinin bos olup olmadigini kontrol ediyor.
    if (memo[i] == 0) {
        memo[i] = stairway2(i - 1, memo)+ stairway2(i - 2, memo);
    }
    return memo[i];
}

int stairway1(int n) {

    return stairway2(n, new int[n + 1]);

}

int main(){

    cout<<"salihtangel\n";
    cout<<stairway1(5);

    return 1;
}