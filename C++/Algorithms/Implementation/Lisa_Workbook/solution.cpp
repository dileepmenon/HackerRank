#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


int main() {
    int n,k,coun=0;
    cin>>n>>k;
    int min=1,max;
    vector<int>t(n);
    int div;
    for (int i=0;i<n;i++)
       { cin>>t[i];
         if (t[i]>k)
         { div=ceil((float)t[i]/k);
           max=min+div-1;
           for(int p=min,j=1,m=1;p<=max; p++,m++)
            {   for(;j<=k*m && j<=t[i]; j++)
                    if(j==p)
                      {coun++;
                      }
            }
         min=max+1;
         }
         else
          {
             for(int x=1;x<=t[i];x++)
              {if (min==x)
                 {coun+=1;
                 }
                 }
            min+=1;
           }
       }
    cout<<coun;
    return 0;
}


