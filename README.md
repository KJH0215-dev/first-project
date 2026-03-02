# first-project

###### 3월 1일 기록

1. python 파일 만들기(hello.py)

2\.	print("Hello World")을 작성

3\.	Git으로 파일 추가하기

 		- cd Desktop = 내 컴퓨터 지정

 		- move ..\\(오늘 내가 만든 파일).

 		- git status = 지금 상태 확인

 		- git add . =  이 파일을 저장한다.

 		- git commit -m(m의 뜻은 메세지) "문구( \[EX]Hello World 추가)" = 변경된 내용을 저장한다.

 		- git push = GitHub로 업로드

4\. 파일 수정 후 다시 위의 3개의 과정 반복

---

###### 3월 2일 기록

C언어 컴파일러 설치



1. 폴더구조

C:\\mingw64\\(include/lib/bin)



2	환경 변수(PATH)설정

환경 변수 검색 --> PATH에 C:\\mingw64\\bin 추가

WHY? 컴퓨터가 gcc 명령어를 어디서 찾을 지 알 수 있도록 길을 설정 해주어야 함



3\.	gcc 동작 확인

VSCODE 가동 후에 main\*\*\*.c(.c 안붙이면 애가 무슨 파일인지 못알아 먹으니 주의!!)\*\*\* 에 변수 입력 후

터미널(Terminal)에서 ***gcc --version***치고 이후에 정상 출력 되면 설치 성공!



4\.	Hello C! 만들기

 		#include <stdio.h>

 		int main() {printf("Hello C!\\n"); return 0;}

\#include <stdio.h> 기능 ----> 표준 입출력 기능을 사용하기 위해 포함



int main 기능 ----> 프로그램 시작을 알림



printf 기능 ----> 화면에 출력

< ++ 왜 C 언어는 printf인가?---> print + format(형식에 맞춰 출력한다.) C언어는 변수를 출력 시 자료형을 직접 지정해야함 근데 파이썬은 그냥 자동 지정되어 나옴 >



\\n 기능 ----> 줄을 바꿈



return0;기능 ----> 정상 종료의미



5\.	컴파일\&실행

컴파일 = gcc main.c -o main



실행 = .\\main



======> 출력 = Hello C! (이후 줄 바뀜)



교훈)

오타 조금이라도 나면 다 망하더라...

C언어는 컴퓨터 친화적이라 인간에게 맞게 수정을 거쳐야 한다.

파이썬은 인간에게 더 가까운 문자라 괜찮더라.

