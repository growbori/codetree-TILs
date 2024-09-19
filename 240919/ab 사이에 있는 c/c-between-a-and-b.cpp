#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    int cnt = 0;

    if (a < b) {
        for (int i = a; i <= b; i++) {
            if (i % c == 0) {
                cnt++;
            }
        }
    } else {
        for (int i = b; i <= a; i++) {
            if (i % c == 0) {
                cnt++;
            }
        }
    }

    if (cnt != 0) {
        cout << "YES";
    } else {
        cout << "NO";  // 만약 `YES`를 출력할 조건이 없다면 `NO`를 출력
    }

    return 0;
}