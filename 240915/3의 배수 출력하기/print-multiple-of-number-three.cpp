#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int i = 1;
    int a ;
    cin >> a;
    while (i <= a) {
        if (i % 3 == 0){
            cout << i << " ";
            
        }
        i ++;
    }
    return 0;
}