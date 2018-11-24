## 마크다운 작성법

마크다운 작성법은
[여기](https://heropy.blog/2017/09/30/markdown/)를 참고하세요.

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
***
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
***
## **중요! crawling 전 반드시 robots.txt 확인할 것**
robots.txt는 해당 페이지가 법적으로 crawling을 허용하는지 안하는지 확인 할 수 있는 파일  
(출처: <http://www.ddaily.co.kr/news/article.html?no=151940>)  

robots.txt파일은 사이트의 루트에 위치함.  
예를 들어, www.example.com 사이트의 경우 robots.txt 파일은 www.example.com/robots.txt에 위치  
반드시 크롤링 전 확인하고 진행할 것  
robots.txt 파일 읽는 법은 [여기](https://support.google.com/webmasters/answer/6062596?hl=ko)를 참조  
