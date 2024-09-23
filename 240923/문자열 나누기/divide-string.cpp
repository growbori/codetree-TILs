#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    string a;
    string word;
    for (int i = 0; i < n; i ++) {
        cin >> word;
        a.append(word);
        
    }
    for (int i = 0; i < a.length(); i ++) {
        cout << a.substr(i, 5) << endl;
        i = i + 4;
    }
    return 0;
}