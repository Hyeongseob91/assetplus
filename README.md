# AssetPlus Backend

AssetPlus는 금융 리포트 요약, 실시간 금융 뉴스 분석, 그리고 일반 상담을 제공하는 AI 기반 챗봇 서비스입니다.

## 주요 기능

1. **리포트 요약**
   - 요약하고싶은 텍스트를 입력받아, 핵심 내용만 요약하는 기능

2. **금융 뉴스 분석**
   - 네이버 뉴스, 금융 분야의 조회수 상위 5개 뉴스 기사 수집 및 요약

3. **일반 상담**
   - 일반적인 금융관련 상담이 가능한 Chatbot 형태의 AI 도우미

## 기술 스택

- **Backend**: Python, FastAPI
- **WebSocket**: 실시간 양방향 통신
- **AI**: OpenAI GPT-4 Realtime API
- **데이터 수집**: BeautifulSoup4, aiohttp

## 설치 방법

1. **필요한 패키지 설치**
```bash
pip install -r requirements.txt
```

2. **환경 변수 설정**
`.env` 파일을 생성하고 다음 내용을 추가:


## 실행 방법

1. **서버 실행**
```bash
python main.py
```

2. **서버 접속**
- WebSocket 엔드포인트: `ws://localhost:8000/ws/chat`
- API 문서: `http://localhost:8000/docs`

## 사용 방법

1. **리포트 요약**
   - '리포트' 명령어 입력
   - 요약할 리포트 텍스트 입력

2. **금융 뉴스**
   - '뉴스' 명령어 입력
   - 자동으로 최신 뉴스 수집 및 분석

3. **일반 상담**
   - 자유롭게 질문 입력
   - AI가 자연스럽게 응답

## 프로젝트 구조
assetplus-backend<br>
├── main.py<br>
├── server.py<br>
├── requirements.txt<br>
├── .env<br>
└── README.md<br>


## API 엔드포인트

- **WebSocket**: `ws://localhost:8000/ws/chat`
  - 실시간 양방향 통신
  - 모든 기능을 하나의 연결로 처리

## 주의사항

1. **API 키 보안**
   - OpenAI API 키는 반드시 `.env` 파일에 저장하세요

2. **에러 처리**
   - 네트워크 오류
   - API 호출 제한
   - 잘못된 입력 처리

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.

## 기여 방법

1. 이슈 생성
2. 브랜치 생성
3. 변경사항 커밋
4. Pull Request 생성


프로젝트 관련 문의사항은 이슈를 통해 남겨주세요.