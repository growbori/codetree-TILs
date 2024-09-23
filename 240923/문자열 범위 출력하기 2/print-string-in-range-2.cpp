#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string word;
    cin >> word;
    int n;
    cin >> n;
    int len = word.length();
    if (len > n) {
        for (int i = len-1; i >= len-n; i --) {
            cout << word[i];
        }
    }
    else {
        for (int i = len-1; i >= 0; i --) {
            cout << word[i];
        }
    }

    return 0;
}