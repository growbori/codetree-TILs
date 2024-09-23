#include <iostream>
#include <vector>
using namespace std;

int main() {
    string word;
    getline(cin, word);

    for (int i = 0; i < word.length(); i++) {
        if (word[i] != ' ') {  // 공백이 아니면 문자를 출력
            cout << word[i];
        } else {
            cout << endl;  // 공백을 만나면 줄을 바꿈
        }
    }
    
    cout << endl; // 마지막 단어를 출력한 후 줄 바꿈 추가

    return 0;
}