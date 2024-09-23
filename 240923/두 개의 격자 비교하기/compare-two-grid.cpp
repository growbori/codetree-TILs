#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    cin >> a >> b;
    int arr[a][b] = {};
    int second[a][b] = {};
    for (int i = 0; i< a; i ++) {
        for (int j = 0; j < b; j ++) {
            cin >> arr[i][j];
        }
    }
    for (int i = 0; i< a; i ++) {
        for (int j = 0; j < b; j ++) {
            cin >> second[i][j];
        }
    }    

    for (int i = 0; i< a; i ++) {
        for (int j = 0; j < b; j ++) {
            if (arr[i][j] == second[i][j]) {
                cout << 0 << " ";
            }
            else {
                cout << 1 << " ";
            }
        }
        cout << endl;
    }
    return 0;
}