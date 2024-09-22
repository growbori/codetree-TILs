#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int arr[100] = {};
    for (int i = 0; i < 100; i ++) {
        cin >> arr[i];
    }

    int max_num = arr[0];
    for (int i = 1; i < 100; i ++) {
        if (arr[i] == 999 || arr[i] == -999) {
            break;
        }
        else {
            if (max_num < arr[i]) {
                max_num = arr[i];
            }
        }
        
    }
    int min_num = arr[0];
    for (int i = 1; i < 100; i ++) {
        if (arr[i] == 999 || arr[i] == -999) {
            break;
        }
        else {
            if (min_num > arr[i]) {
                min_num = arr[i];
            }
        }
        
    }

    cout << max_num << " " << min_num;
    return 0;
}