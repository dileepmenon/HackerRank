#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int t, n, rem, quo,coun;
	cin >> t;
	for (int a0 = 0; a0 < t; a0++)
	{
		coun = 0;
		cin >> n;
		rem=n % 10;
		quo = n;
		while (quo!=0)
		{
			if (rem != 0)
			{
				if (n%rem == 0)
					coun++;
			}
			quo = quo/ 10;
			rem = quo%10;
		}

		cout << coun << endl;
	}
    return 0;
}


