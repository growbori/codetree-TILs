#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    cin >> a >> b;
    int nums[a] = {};
    for (int i = 0; i < a; i ++) {
        cin >> nums[i];
    }
    int check[b] = {};
    for (int j = 0; j < b; j ++) {
        cin >> check[j];
        if (check[0] == 1) {
            cout << nums[check[1] -1];
        }
        else if (check[0] == 2) {
            for (int k = 0; k < a; k ++) {
                if (nums[k] == check[1]) {
                    cout << i+1;
                    break;
                }
            }
            else {
                cout << 0;
            }
        }
        else {
            for (int i = check[1]-1; i < check[2]; i ++) {
                cout << nums[i] << " " << endl;
            }
        }
    }
    
    return 0;
}