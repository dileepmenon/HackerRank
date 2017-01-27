#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
int t,a,b,coun,sq;
float c;
cin>>t;
for (int i=0;i<t;i++)
  { coun=0;
    sq=0;
    cin>>a>>b;
    for (int j=a;j<=b;j++)
    {  c=floor(sqrt(j)*100+0.5)/100;
       if (pow(c,2)-j==0)
       {sq=c;
        break;
       }
    }
   if (sq!=0)
   {for (int k = sq; k *k <= b; k++)
   		coun++;
   }
   cout<<coun<<endl;
  }
    return 0;
}


