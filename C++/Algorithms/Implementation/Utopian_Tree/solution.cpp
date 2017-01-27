#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int t,n,hei,j;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        cin >> n;
        hei=1;
    if (n==0)
      cout<<hei<<endl;
    else     
     {for(j=0;j<n;j++)
       {if (j%2==0)
          hei=hei*2;
        else
           hei=hei+1;   
        }   
      cout<<hei<<endl;  
    }
    
    }
    return 0;
}


