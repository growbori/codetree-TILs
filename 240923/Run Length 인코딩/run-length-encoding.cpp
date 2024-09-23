#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string word;
    cin >> word;
    string ans[word.length()] = {};
    int count = 0;
    char check;
    for (int i = 0; i < word.length()-1; i ++) {
        if (word[i] == word[i+1] && i != word.length()-2){
            check = word[i];
            count ++;
        }
        else if (word[i] != word[i+1]) {
            ans.push_back(check);
            check = word[i+1];
            ans.push_back(count +1);
            count = 0;
        } 
        else {
            check = word[i];
            count += 1;
            ans.push_back(check);
            ans.push_back(count +1);
        }
    }
    return 0;
}