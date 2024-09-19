#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    int cnt = 0;

    while (true) {
        if (cnt != 0) {
            cout << "YES";
            break;
        } else {
            if (a < b) {
                for (int i = a; i <= b; i++) {
                    if (i % 7 == 0) {
                        cnt++;
                    }
                }
            } else {  // 여기에 else 블록의 시작 괄호 추가
                for (int i = b; i <= a; i++) {
                    if (i % 7 == 0) {
                        cnt++;
                    }
                }
            }  // 여기에 else 블록의 끝 괄호 추가
        }
    }

    return 0;
}