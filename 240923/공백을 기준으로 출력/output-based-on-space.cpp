#include <iostream>
#include <string>
using namespace std;

int main() {
    // 문자열을 구현합니다.
	string str;
	string str2;
	
	// 공백을 포함한 문자열을 입력받습니다.
	getline(cin, str);
	getline(cin, str2);
	
	// 문자열을 전부 순회하며 공백을 제외한 모든 문자를 출력합니다.
	for(int i = 0; i < str.length(); i++)
		if(str[i] != ' ')
			printf("%c", str[i]);
	
	for(int i = 0; i < str2.length(); i++)
		if(str2[i] != ' ')
			printf("%c", str2[i]);

    return 0;
}