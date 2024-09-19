#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int cnt_c = 0;
    int cnt_w = 0;
    int cnt_t = 0;
    int a = 0;
    cin >> a;
    for (int i = 1; i <= a ; i ++) {
        if (i % 12 == 0) {
            cnt_t ++;
        }
        else if (i % 3 == 0) {
            cnt_w ++ ;
        }
        else if (i % 2 == 0) {
            cnt_c ++;
        }
    }

    cout << cnt_c << " " << cnt_w << " " << cnt_t ;
    return 0;
}