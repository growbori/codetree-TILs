#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    char arr[6] = {'L', 'E', 'B', 'R', 'O', 'S'};
    char c;
    int i;
    for (int i = 0; i <6; i ++) {
        cin >> c;
        if (c == arr[i]) {
            cout << i;
            break;
        }

    }
    if (i == 6) {
    cout << "None";
    }
    return 0;
}