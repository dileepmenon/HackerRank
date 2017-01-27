#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int n,c;
    cin >> n;
    vector<string> grid(n);
    for(int grid_i = 0;grid_i < n;grid_i++){
       cin >> grid[grid_i];
    }
    for(int j=1;j<=n-2;j++)
    {  for(int i=1;i<=n-2;i++)
       {if (grid[j][i]>grid[j][i+1]&&grid[j][i]>grid[j][i-1]&&grid[j][i]>grid[j+1][i]&&grid[j][i]>grid[j-1][i])
           grid[j][i]='X';
       }
    }
    for(int grid_i = 0;grid_i < n;grid_i++){
      cout<<grid[grid_i]<<endl;
    }
    return 0;
}


