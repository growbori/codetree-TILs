#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string word;
    cin >> word;
    int len;
    len = word.length();
    for (int i = 0; i < len; i ++ ) {
        cout << word[i] << endl;
    }
    return 0;
}