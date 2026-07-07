#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long n;

    while (cin >> n && n)
    {
        long long r = sqrt(n);

        if (r * r == n)
        {
            cout << "yes\n";
        }
        else
        {
            cout << "no\n";
        }
    }
}
