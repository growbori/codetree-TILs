#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    cin >> a >> b;
    int arr[a][b] = {};
    int num = 1;
    for (int i = 0; i < a; i ++) {
        for (int j = 0; j < b; j ++) {
            arr[i][j] = num;
            cout << arr[i][j] << " ";
            num ++;
        }
        cout << endl;
    }
    return 0;
}