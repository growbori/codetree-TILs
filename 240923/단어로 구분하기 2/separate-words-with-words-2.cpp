#include <iostream>
#include <sstream>
using namespace std;

int main() {
    string line;
    getline(cin, line);  // 한 줄의 문자열을 입력받음

    stringstream ss(line);  // stringstream을 사용하여 공백으로 분리
    string word;
    int index = 1;  // 단어의 인덱스를 1부터 시작

    while (ss >> word) {
        if (index % 2 != 0) {  // 인덱스가 홀수인 경우만 출력
            cout << word << endl;
        }
        index++;  // 인덱스를 증가시킴
    }

    return 0;
}