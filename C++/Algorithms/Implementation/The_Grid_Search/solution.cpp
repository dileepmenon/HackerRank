#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int foun;
	int t;
	int R, C;
	cin >> t;
	int r, c,pos1,pos2,sum1,sum2,strt1,strt2,end1,end2;
	for (int a0 = 0; a0 < t; a0++) 
	{
        foun=0;
		cin >> R >> C;
		vector<string> G(R);
		for (int G_i = 0; G_i < R; G_i++) {
			cin >> G[G_i];
		}

		cin >> r >> c;
		vector<string> P(r);
		for (int P_i = 0; P_i < r; P_i++) {
			cin >> P[P_i];
		}

		if (R % 2 == 0)
		{
			  strt1 = 0, strt2 = R - 1;
			  end1 = (R / 2) - 1, end2 = R / 2;
        }
        else
		{
			   strt1 = 0, strt2 = R - 1;
			   end2 = ((R - 1) / 2)+1, end1= (R - 1) / 2;
		}
            while (strt1 <= end1)
			{
				 sum1 = 0;
				 sum2 = 0;
				 pos1 = G[strt1].find(P[0]);
				 pos2 = G[strt2].find(P[r - 1]);
				if (pos1!=-1 && strt1+r-1<=R-1)
				{
					for (int i = strt1,c1=0; i<=strt1+(r-1); i++,c1++)
					{
						if (G[i].substr(pos1,c) == P[c1])
						{
							sum1 += 1;
						}
					}
				}
				if (pos2 !=-1 && strt2-(r-1)>=0)
				{   
					for (int i = strt2,c2=r-1; i>=strt2-(r-1); i--,c2--)
					{
	
						if (G[i].substr(pos2,c) == P[c2])
						{
							sum2 += 1;
						}
					}
				}
				if (sum1 == r || sum2 == r)
				{
					foun = 1;
					cout << "YES"<<endl;
					break;
				}

				strt1++;	
                strt2--;
			}
			if (foun == 0)
				cout << "NO"<<endl;

    }
    return 0;
}


