#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


    int main()

    {
    string time;
    cin >> time;
    int var;
	if (time[8] == 'A')
	{
		if (time[0] == '1' && time[1] == '2')
		{
			cout << "00"+time.substr(2,6);
		}
		else
			cout << time.substr(0,8);
	}
	else
	{
		if (time[0] == '1' && time[1] == '2')
		{
			cout << time.substr(0,8);
		}
		else
		{
			if (time[0] == 0)
			{
				var = time[1]-48 + 12;
				cout << to_string(var)+time.substr(2,6);
			}
			else
			{
				var = stoi(time.substr(0, 2))+12;
				cout << to_string(var)+ time.substr(2,6);
			}
		}
	}
    return 0;
}


