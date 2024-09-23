#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int arr[n] = {};
    for (int i = 0; i < n; i ++) {
        cin >> arr[i];
    }

    int minminus = 100;
    for (int i = 0; i < n-1; i ++) {
        if (minminus >= arr[i+1] - arr[i]) {
            minminus = arr[i+1] - arr[i];
        }
    }
    cout << minminus;
    return 0;
}