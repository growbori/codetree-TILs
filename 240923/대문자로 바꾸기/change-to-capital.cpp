#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    char arr[5][3];
    for (int i = 0; i < 5; i ++) {
        for (int j = 0; j < 3; j ++) {
            cin >> arr[i][j];
        }
    }
    
    for (int i = 0; i < 5; i ++) {
        for (int j = 0; j < 3; j ++) {
            cout << char(int(arr[i][j]) - 32) << " ";
        }
        cout << endl;
    }
    return 0;
}