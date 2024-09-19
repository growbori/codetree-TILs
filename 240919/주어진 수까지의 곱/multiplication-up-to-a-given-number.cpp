#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int pro = 1;
    int a, b;
    cin >>a >> b;
    for (int i = a; i <= b; i ++) {
        pro *= i;
    }
    cout << pro;
    return 0;
}