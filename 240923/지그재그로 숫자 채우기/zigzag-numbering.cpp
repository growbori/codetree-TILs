#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    cin >> a >> b;
    int arr[a][b] = {};
    int num = 0;
    for (int j = 0; j < b; j ++) {
        if (j % 2 == 0) {
            for (int i = 0; i < a; i ++) {
                arr[i][j] = num;
                num ++;
            }
        }
        else {
            for (int i = a-1; i >= 0; i --) {
                arr[i][j] = num;
                num ++;
            }
        }
    }
    for (int i = 0; i < a; i ++) {
        for (int j = 0; j < b; j ++) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}