#include <stdio.h>
using namespace std;

int main()
{
    for (int i = 1; i < 10; i *= 2)
    {
        printf("%d", i);
    }
    return 0;
}
