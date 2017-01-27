#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int t,my_cash,cost,wrap_ex,num_choc,wrap_choc,sum=0;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++)
	{
    cin >> my_cash >> cost>> wrap_ex;
    num_choc=my_cash/cost;
    wrap_choc=num_choc/wrap_ex;
    sum=num_choc+wrap_choc;
    while (!((wrap_choc==1&&num_choc%wrap_ex==0) || wrap_choc==0))
      {
       num_choc=(num_choc%wrap_ex+wrap_choc);
       wrap_choc=num_choc/wrap_ex;
       sum+=wrap_choc;
      }
    cout<<sum<<endl;
    }
    return 0;
}


