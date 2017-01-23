#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int n,t;
    cin >> n;
    for (int i=0;i<n;i++)
    {t=n-i-1;
     while(t>0)
     {cout<<" " ;t--;
     }
     for(int j=0;j<=i;j++)
      cout<< "#";
     cout<<endl;
    }
    return 0;
}


