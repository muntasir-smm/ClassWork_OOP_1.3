#include <iostream>
using namespace std;

// Example 1: Method Overloading
class Calculator {
    public:
        int add(int a, int b) {
        return a + b;
    }
    double add(double a, double b) {
        return a + b;
    }
    int add(int a, int b, int c) {
        return a + b + c;
    }
};

int main() {
    Calculator calc;

    cout << "add(2, 3) = " << calc.add(2, 3) << endl;
    cout << "add(2.5, 3.7) = " << calc.add(2.5, 3.7) << endl;
    cout << "add(1, 2, 3) = " << calc.add(1, 2, 3) << endl;

    return 0;
}
