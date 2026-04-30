#include <iostream>
#include <cstdlib>  // for rand()
#include <ctime>    // for time()

using namespace std;

// random number between [a, b)
int random_number(int a, int b) {
    int t = b - a;
    int res;

    do {
        res = 0;
        for (int i = 0; (1 << i) < t; ++i) {
            res = (res << 1) + (rand() & 1);
        }
    } while (res >= t);

    return res + a;
}

int main() {
    srand(time(0)); // seed random generator

    cout << random_number(10, 20) << endl;

    return 0;
}