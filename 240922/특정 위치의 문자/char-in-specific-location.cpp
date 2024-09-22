#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    char arr[6] = {'L', 'E', 'B', 'R', 'O', 'S'};
    char c;
    string ans = "None";
    for (int i = 0; i <6; i ++) {
        cin >> c;
        if (c == arr[i]) {
            ans = to_string(i);
            break;
        }
    }
    cout << ans;
    return 0;
}