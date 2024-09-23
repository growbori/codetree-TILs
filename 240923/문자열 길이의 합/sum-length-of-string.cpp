#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<string> words(n);  // n개의 문자열을 저장할 벡터
    int sum = 0;
    int first = 0;

    for (int i = 0; i < n; i++) {
        cin >> words[i];
        sum += words[i].length();  // 각 문자열의 길이를 합산
        if (words[i][0] == 'a') {
            first++;  // 첫 글자가 'a'인 단어의 개수를 셈
        }
    }

    cout << sum << " " << first << endl;  // 첫 단어의 첫 글자 출력

    return 0;
}