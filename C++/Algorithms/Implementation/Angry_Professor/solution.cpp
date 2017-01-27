#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int t,count[12];
    cin >> t;
    int n;
    int k;
    
    for(int a0 = 0; a0 < t; a0++)
    {   count[a0]=0;
        cin >> n >> k;
        vector<int> a(n);
        for(int a_i = 0;a_i < n;a_i++)
        {
           cin >> a[a_i];
           if (a[a_i]<=0)
               count[a0]++;
        }
        if (count[a0]<k)
           cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
    
    }
    
    return 0;
}


