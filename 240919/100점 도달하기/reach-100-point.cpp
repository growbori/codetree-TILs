#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, i;
    cin >> a;
    for (i = a; i <= 100; i ++) {
        if (i >= 90) {
            cout << "A ";
        }
        else if (i >= 80) {
            cout << "B ";
        }     
        else if (i >= 70) {
            cout << "C ";
        }  
        else if (i >= 60) {
            cout << "D ";
        }        
        else if (i < 60) {
            cout << "F "; 
        }



        
    }
    return 0;
}