#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    // 위쪽 반쪽
    for (int i = 0; i < n; i++) {
        // 왼쪽 공백 출력
        for (int j = 0; j < n - i - 1; j++) {
            cout << " ";
        }

        // 별 출력
        for (int k = 0; k < 2 * i + 1; k++) {
            if (k % 2 == 0)
                cout << "*";
            else
                cout << " ";
        }
        cout << endl;
    }

    // 아래쪽 반쪽
    for (int i = n - 2; i >= 0; i--) {
        // 왼쪽 공백 출력
        for (int j = 0; j < n - i - 1; j++) {
            cout << " ";
        }

        // 별 출력
        for (int k = 0; k < 2 * i + 1; k++) {
            if (k % 2 == 0)
                cout << "*";
            else
                cout << " ";
        }
        cout << endl;
    }

    return 0;
}