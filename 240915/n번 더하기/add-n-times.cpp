#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    cin >> a >> b;
    int i = 1;
    while (i <= b) {
        cout << a + b<< endl;
        a = a + b;
        i ++;  
    }
    return 0;
}