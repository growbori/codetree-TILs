#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int arr[10] = {};
    int max_1 = 0;
    int max_2 = 1000;
    for (int i = 0; i < 10; i ++) {
        cin >> arr[i];
        if (arr[i] < 500) {
            if (max_1 < arr[i]) {
                max_1 = arr[i];
            }
        }
        if (arr[i] > 500) {
            if (max_2 > arr[i]) {
                max_2 = arr[i];
            }
        }
    }
    cout << max_1 << " " << max_2;


    return 0;
}