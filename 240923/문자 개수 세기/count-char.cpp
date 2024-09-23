#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string word;
    getline(cin, word);
    char x;
    cin >> x;
    int c = word.length();
    int cnt = 0;
    for (int i = 0; i < c; i ++) {
        if (word[i] == x) {
            cnt ++;
        }
    }
    cout << cnt;
    return 0;
}