#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        long long s, ep, gp;
        cin >> s >> ep >> gp;

        long long a = s * ep;
        long long c = ((s / 3) * gp + min(gp, (s % 3) * ep));
        // long long b = ((s + 2) / 3) * gp;
        // cout << min({a, b, c}) << endl;

        cout << min(a, c) << "\n";
    }
    return 0;
}