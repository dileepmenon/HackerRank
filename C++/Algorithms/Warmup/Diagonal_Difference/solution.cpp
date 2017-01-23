#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int n,sum_pri_dia=0,sum_sec_dia=0;
    cin >> n;
    vector< vector<int> > a(n,vector<int>(n));
    for(int a_i = 0;a_i < n;a_i++)
	{
       for(int a_j = 0;a_j < n;a_j++)
	   {
          cin >> a[a_i][a_j];
       }
    }
    for(int i = 0;i < n;i++)
	   {
      sum_pri_dia=sum_pri_dia+a[i][i];
      sum_sec_dia=sum_sec_dia+a[i][n-1-i]  ;
       }
    cout<<abs(sum_pri_dia-sum_sec_dia);
    return 0;
}


