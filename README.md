## 마크다운 작성법

마크다운 작성법은
[여기](https://github.com/sejong-interface/Interface_Manual/wiki/Git-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0%233-README.md-%ED%8C%8C%EC%9D%BC-%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B0!)를 참고하세요.

```python
from bs4 import BeautifulSoup
### 이렇게하면
### 파이썬 코드로 나온다길래
### 실험 ㅎㅎ
```
## 이력
**[2018-11-12]** FOOT / 한겨레(hani) 코드랑 결과파일예시 올렸으니까 알아서 참고하시고 짜세여 ㅎㅎ, KBS는 크롤링이 안되여..  
**[2018-11-22]** NO
  1. 조선일보 크롤링 코드와 결과파일 올림 (pj/josun.py  pj/josun.json)  
  2. 노컷뉴스 크롤링 코드와 결과파일 올림 (pj/nocut.py  pj/nocut.json)  

### CAUTION
json 파일로 변환하기 전 dictionary data는 collections.OrderedDict 모듈을 사용할 것.

### 저장 json 양식

  ~~~
  {
  "title": "네이버 모바일 첫화면 구글처럼 바뀌나…사내테스트 진행", // 제목
  "date": "20180927", //기사날짜 형식은 yyyyMMdd
  "press": "News1", // 언론사 이름
  "link": "http://news1.kr/articles/?3435488", //원문 기사 링크
  "reporter": "노평진", // 이름 석자
  "category": "경제" // 경제, 국제, 정치, 연예, 사회
  }
  ~~~
