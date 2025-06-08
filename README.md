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
- **Model**: OpenAI 'gpt-4o-realtime-preview-2025-06-03'

## bacnend Server 설치 방법

1. **필요한 패키지 설치**
```bash
cd assetsplus-backend
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
- Local Server: `http://localhost:8000`
- API 인증 Server: `http://localhost:8080`

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

## 개발 현황
1. FastAPI 기반 backend Server 구축
2. Flutter 기반 frontend Client 구축
3. Android Studio를 활용한 UI/UX 테스트 진행

## 포함된 파일 항목
### 1. backend
- realtime_openai.py : RealTime API를 사용하는 AI Tool 모음
- main.py : FastAPI 기반의 WebSocket 통신 방식의 서버
- ephemeral_token.py : RealTime API Key를 사용 할 수 있도록, 기존의 API Key를 인증 받을 수 있는 서버
- stream_openai_test.py : WebSocket Test file

### 2. frontend
- main.dart : Flutter 기반 Frontend Script Code
- pubspec.yaml : 프로젝트의 의존성, 에셋, 환경설정 등
- assetplus.apk : 실제로 빌드된 apk 파일
