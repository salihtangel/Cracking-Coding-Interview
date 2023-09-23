#include <iostream>
using namespace std;

bool find_magic_arr(int arr[]){
    if( arr[0]  == 0 )
        return true;

    if( arr[1] == 1)
        return true;
    
    if( arr[2 == 2])
        return true;
    
    else{
        return false;
    }
    
    
}

int main(){

    int arr[] = {1,2,3,4,5,6,7,8,9,10};
    int arr2[] = {3,4,6,7,8,9,10,123,2445};
    int arr3[] = {0};
 
    cout<<arr3[1];
    //cout<<"adsds";

    //cout<<find_magic_arr(arr3);

    return 0;
}