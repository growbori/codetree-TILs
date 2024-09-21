#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    for (int i = 1; i <= n; i ++) {
        int a, b;
        cin >> a >> b;
        int mul = 1;
        for (int j = a; j <= b; j ++) {
            
            mul *= j;
        }
        cout << mul << endl;
    }
    return 0;
}