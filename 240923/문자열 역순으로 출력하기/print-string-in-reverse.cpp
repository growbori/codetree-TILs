#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string arr[4] = {};
    string word;
    for (int i = 0; i < 4; i ++) {
        cin >> arr[i];
    }
    for (int i = 3; i >=0; i --) {
        cout << arr[i] << endl;
    }    
    return 0;
}