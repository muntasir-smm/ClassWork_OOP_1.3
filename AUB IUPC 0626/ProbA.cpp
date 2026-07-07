#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long a, b;

    while (cin >> a >> b && (a || b))
    {
        int carry = 0;
        int counter = 0;

        while (a > 0 || b > 0)
        {
            int sum = (a % 10) + (b % 10) + carry;

            if (sum >= 10)
            {
                counter++;
                carry = 1;
            }
            else
            {
                carry = 0;
            }

            a /= 10;
            b /= 10;
        }

        if (counter == 0)
            cout << "No carry operation.\n";
        else if (counter == 1)
            cout << "1 carry operation.\n";
        else
            cout << counter << " carry operations.\n";
    }

    return 0;
}