#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string word;
    getline(cin, word);
    cout << word.substr(2, 8);
    return 0;
}