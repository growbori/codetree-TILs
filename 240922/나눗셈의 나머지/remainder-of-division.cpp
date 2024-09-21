#include <iostream>
using namespace std;

int main() {
    int arr[10] = {0};  // 나머지 카운트를 위한 배열, 0으로 초기화
    int a, b;
    cin >> a >> b;
    int sum = 0;

    while (a >= 1) {
        int c = a % b;  // 나머지 계산
        arr[c]++;       // 해당 나머지 등장 횟수 증가
        a = a / b;      // 몫으로 a 갱신
        if (a == 0) {
            break;
        }
    }

    for (int j = 0; j < 10; j++) {
        sum += arr[j] * arr[j];  // 등장 횟수를 제곱하여 합산
    }

    cout << sum << endl;

    return 0;
}