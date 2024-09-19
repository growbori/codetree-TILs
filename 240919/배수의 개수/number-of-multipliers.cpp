#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int i;
    int cnt = 0;
    int cntq = 0;
    for (i = 1; i <= 10; i ++) {
        int a;
        cin >>a;

        if(a % 3 == 0) {
            cnt ++;
        }
        if (a % 5 == 0) {
            cntq ++ ;
        }
    }
    cout << cnt << " " << cntq ;
    return 0;
}