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


## api 

### user

curl --location --request GET 'http://127.0.0.1:5000/api/v1/user/{이메일}' \
--header 'Content-Type: application/json' \
--data-raw '' 

### status

curl --location --request POST 'http://127.0.0.1:5000/api/v1/status/{이메일}' \
--header 'Content-Type: application/json' \
--data-raw '{"text":"퇴근", "emoji":":four_leaf_clover:"}'

### message

curl --location --request POST 'http://127.0.0.1:5000/api/v1/message/{이메일}' \
--header 'Content-Type: application/json' \
--data-raw '{"text":"성공적으로 신청되었습니다."}'