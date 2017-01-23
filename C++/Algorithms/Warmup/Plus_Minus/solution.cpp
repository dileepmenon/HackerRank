#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int n,pos=0,neg=0,zer=0,t;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0;arr_i < n;arr_i++)
    {
       cin >> arr[arr_i];
       if(arr[arr_i]!=0)
       {
         t=arr[arr_i];
         if (((abs(t)/t)==1))
               pos++;
         if  (((abs(t)/t)== -1))
               neg++;
       }
       else
        zer++;
      }
    cout<<(float)pos/n<<endl;
    cout<<(float)neg/n<<endl;
    cout<<(float)zer/n;
    return 0;
}


