#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string word[10] = {};
    for (int i=0; i < 10; i ++) {
        cin >> word[i];
    }
    int sum = 0;
    for (int i=0; i < 10; i ++) {
        sum += word[i].length();
    }    
    cout << sum;
    return 0;
}