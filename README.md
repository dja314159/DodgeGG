# DodgeGG
Prediction &amp; Recommend about LOL


<Prediction Win rate on Selection>


- API 신청완료(11/11, 승인까지 일주일 정도 걸린다고 함)
- 한명의 계정으로 최근 10게임 승패 여부 확인 완료.

1. 데이터 수집

	- 한 match의 10명 소환사의 최근 5판 gameId 불러오기
		1) 선택한 match의 gameId를 통해 소환사 10명의 정보 받아오기
		2) 각 소환사들의 Id를 통해 최근게임에서 현재 탐색중인 matchId의 인덱스 조사하기
		3) 해당 인덱스로부터 +5 인덱스 까지의 gameId 저장하기
	
	- 위 단계를 n번 거치면서 학습을 위한 데이터를 수집하기

2. 학습

	- 한팀에 있는 5명의 이전 게임 데이터를 전부 다(25게임)을 몽땅 넣어서 그냥 NN학습 시키기
	- 좀더 진전된 방법?
