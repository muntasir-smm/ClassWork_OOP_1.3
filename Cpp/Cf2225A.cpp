#include <bits/stdc++.h>
using namespace std;
using int64 = long long;

int main()
{
    int t;
    long long x, y;
    cin >> t;

    while (t--)
    {
        cin >> x >> y;

        if (y == 2 * x)
        {
            cout << "NO\n";
        }
        else
        {
            cout << "Yes\n";
        }
    }
}