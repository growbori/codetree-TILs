#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int arr[10];
    int check[10] = {};
    for(int i = 0; i < 10; i ++) {
        cin >> arr[i];
        check[arr[i]] ++;
    }
    for (int i = 1; i <= 6; i ++) {
        cout << i << " - " << check[i] << endl ;
    }

    return 0;
}