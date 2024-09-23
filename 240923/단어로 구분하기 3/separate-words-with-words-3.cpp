#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

int main() {
    string word;
    getline(cin, word);  // 문장을 입력받음
    stringstream ss(word);
    vector<string> words;  // 단어를 저장할 벡터

    string first;
    while (ss >> first) {
        words.push_back(first);  // 단어를 벡터에 저장
    }

    // 벡터에 저장된 단어를 거꾸로 출력
    for (int i = words.size() - 1; i >= 0; i--) {
        cout << words[i] << endl;
    }

    return 0;
}