#include "game.h"

int main()
{
	bool notAWinner;

	Game aGame;

	aGame.add("Chet");
	aGame.add("Pat");
	aGame.add("Sue");

	do {
		aGame.rolling();
		//rolling 역할 1 : 주사위를 굴린다.
		//rolling 역할 2 : 퀴즈 카드를 한장 뽑는다.		
		
		//rolling 함수에서는 말의 위치(place)만 갱신한다.		
		//answer 함수에서는 지갑, 코인, 페널티박스 상태값들을 갱신한다.
		if (rand() % 9 == 7) {
			notAWinner = aGame.wrongAnswer(); //퀴즈 오답처리 후, 감옥감, 턴을 넘김
		}
		else {
			notAWinner = aGame.wasCorrectlyAnswered(); //퀴즈 정답처리 후, 턴을 넘김
		}
	} while (notAWinner);
}
