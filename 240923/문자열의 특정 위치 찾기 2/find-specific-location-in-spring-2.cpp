#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string arr[5] = { "apple", "banana", "grape", "blueberry", "orange" };
    char a;
    cin >> a;
    int cnt = 0;
    for (int i = 0; i < 5; i ++) {
        if (arr[i][2] == a || arr[i][3] == a) {
            cout << arr[i] << endl;
            cnt ++;
        }
    }
    cout << cnt;
    return 0;
}