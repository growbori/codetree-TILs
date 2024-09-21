#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int cnt = 65;  // ASCII 코드 65는 'A'

    for (int i = 0; i < n; i++) {
        // 왼쪽 공백 출력
        for (int j = 0; j < i; j++) {
            cout << "  ";
        }

        // 문자 출력
        for (int k = i; k < n; k++) {
            cout << (char)cnt << " ";
            cnt++;
        }
        cout << endl;
    }

    return 0;
}