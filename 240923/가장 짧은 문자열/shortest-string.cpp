#include <iostream>
#include <vector>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string word;
    vector<int> vec;
    for (int i = 0; i < 3; i ++) {
        cin >> word;
        vec.push_back(word.length());
    }
    int short_word = 21;
    int long_word = 0;
    for (int i = 0; i < 3; i ++) {
        if (vec[i] < short_word) {
            short_word = vec[i];
        }
        else if (vec[i] > long_word){
            long_word = vec[i];
        }
    }

    cout << long_word - short_word ;

    return 0;
}