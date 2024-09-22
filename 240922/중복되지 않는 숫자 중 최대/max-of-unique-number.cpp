#include <iostream>
#include <vector>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    int arr[n] = {};
    int blank[1000] = {};

    for (int i = 0; i < n; i ++) {
        cin >> arr[i];
        blank[arr[i]] += 1;
    }
    vector<int> vec;

    for (int j = 0; j < 1000; j ++) {
        if (blank[j] == 1) {
            vec.push_back(j);
        }
    }

    if (!vec.empty()) {  // check 벡터가 비어 있지 않다면
        cout << vec.back();  // 벡터의 마지막 요소 출력
    } else {
        cout << -1;  // 벡터가 비어 있다면 -1 출력
    }
    

    return 0;
}