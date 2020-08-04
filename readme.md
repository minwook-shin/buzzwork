## buzzwork for slack

코로나19로 인한 회사 원격근무에 도움이 되고자, 퇴근 후 조금씩 만들기 시작한 프로젝트

슬랙 api 를 손쉽게 사용할 수 있도록 재구성했습니다.

naming : buzz(ing) + (remote) work

## 필요한 사용자 권한

chat:write

users.profile:read

users.profile:write

users:read

users:read.email


## 서버 세팅

슬랙 봇을 생성하고 토큰을 가져와야 한다.

export SLACK_BOT_TOKEN="{토큰}"

