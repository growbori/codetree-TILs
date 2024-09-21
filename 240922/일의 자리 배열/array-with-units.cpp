#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    cin >> a >> b;
    int arr[10];
    arr[0] = a;
    arr[1] = b;
    for (int i = 2; i < 10; i ++) {
        arr[i] = arr[i-1] + arr[i-2];
    }
    for (int j = 0; j < 10; j ++) {
        cout << (arr[j]%100) % 10 << " ";
    }

    return 0;
}