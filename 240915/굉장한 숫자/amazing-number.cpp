#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a;
    cin >> a;
    if ((a % 2 == 1 && a % 3 == 0) || (a % 2 == 0 && a % 5 == 0)) {
        cout << "true";
    }
    else {
        cout << "false";
    }
    return 0;
}