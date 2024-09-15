#include <iostream>
using namespace std;

int main() {
    // 3명의 증상과 체온을 입력받기 위한 변수 선언
    char symptom1, symptom2, symptom3;  // 증상 (Y 또는 N)
    int temp1, temp2, temp3;  // 체온
    
    // 입력 받기
    cin >> symptom1 >> temp1;
    cin >> symptom2 >> temp2;
    cin >> symptom3 >> temp3;
    
    int count_A = 0;  // A에 해당하는 사람 수를 셈
    
    // 첫 번째 사람에 대한 처리
    if (symptom1 == 'Y' && temp1 >= 37) {
        count_A++;
    }
    
    // 두 번째 사람에 대한 처리
    if (symptom2 == 'Y' && temp2 >= 37) {
        count_A++;
    }
    
    // 세 번째 사람에 대한 처리
    if (symptom3 == 'Y' && temp3 >= 37) {
        count_A++;
    }
    
    // A에 해당하는 사람이 2명 이상일 경우 위급 상황 (E) 출력
    if (count_A >= 2) {
        cout << "E" << endl;
    }
    // 그렇지 않으면 (N) 출력
    else {
        cout << "N" << endl;
    }
    
    return 0;
}