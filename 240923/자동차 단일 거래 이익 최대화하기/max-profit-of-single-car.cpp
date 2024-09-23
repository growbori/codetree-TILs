#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    int arr[n] = {};
    for (int i = 0; i < n; i ++) {
        cin >> arr[i];
    }
    int front, back, ans;
    vector<int> check;
    for (int i = 0; i < n; i ++) {
        for (int j = i; j < n; j ++) {
            front = arr[i];
            back = arr[j];
            ans = back - front;
            check.push_back(ans);
        }
    }

    int max_value = 0;  // 최대값을 저장할 변수

    for (int i = 0; i < check.size(); ++i) {
        if (check[i] > max_value) {
            max_value = check[i];
        }
    }

    std::cout << max_value << std::endl;
    return 0;
}