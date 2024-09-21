#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    for (int i = 1; i <= 19; i ++) {
        for (int j = 1; j <=10; j ++) {
            if (j == 10) {
                cout << i << " * " << 2 *j - 1 << " = " <<  i * (2 *j - 1) ;
                cout << endl;
            }
            else {
                cout << i << " * " << 2 *j - 1 << " = " <<  i * (2 *j - 1) << " / " << i << " * " << 2 *j << " = " <<  i * (2 *j);
                cout << endl;
            }
        }
    }
    return 0;
}