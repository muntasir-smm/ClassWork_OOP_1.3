#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long t;
    cin >> t;

    while (t--)
    {
        long long n;
        cin >> n;

        int count = 0;
        for (long long i = 1; i < sqrt(n); i++)
        {
            long long x = i * i;
            long long g = __gcd(n, x);
            long long result = g + (n / g) * x;
            if (result == (n + x))
            {
                count++;
            }
        }
        cout << count << "\n";
    }
}