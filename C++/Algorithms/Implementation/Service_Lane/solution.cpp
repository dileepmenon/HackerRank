#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n,min;
    int t;
    int i;
    int j;
    cin >> n >> t;
    vector<int> width(n);
    for(int width_i = 0;width_i < n;width_i++){
       cin >> width[width_i];
    }
    for(int a0 = 0; a0 < t; a0++){
        cin >> i >> j;
        min=width[i];
        for(int x=i+1;x<=j;x++)
         { if(min>width[x])
             min=width[x];
         }
        if(min==1)
          cout<<"1"<<endl;
        else if(min==2)
          cout<<"2"<<endl;
        else
          cout<<"3"<<endl;
    }
    return 0;
}


