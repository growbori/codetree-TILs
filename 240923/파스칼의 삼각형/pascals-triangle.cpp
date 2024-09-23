#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int arr[n][n];

    // 파스칼 삼각형 초기화 및 계산
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            if (j == 0 || j == i) {
                arr[i][j] = 1; // 삼각형의 양 끝은 1
            } else {
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]; // 이전 행의 두 값의 합
            }
        }
    }

    // 파스칼 삼각형 출력
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}