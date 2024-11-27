
<div align="center">

![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=300&section=header&text=SKN5%203rd-Projet%20Team%202&fontSize=60)

<div align="center">

  <h2> 👀 Team Overview 👀 </h2>

  |<img src="https://github.com/user-attachments/assets/e6176d94-55ad-4e20-b2b9-8ac260ac0c4d" width="150" height="150"/>|<img src="https://github.com/user-attachments/assets/b5eac200-ab02-4f7d-ae32-b74f5a933fcd" width="150" height="150"/>|<img src="https://github.com/user-attachments/assets/ac77a03b-af69-415c-bf13-5cc4ce400f5c" width="150" height="150"/>|<img src="https://github.com/user-attachments/assets/f54fe4d8-5735-443b-86e5-7fdb57ef5fdb" width="150" height="150"/>|
  |:-:|:-:|:-:|:-:|
  |Choi Young min<br/>[@MartinusChoi](https://github.com/MartinusChoi)<br/>RAG Chain, Fine Tune|Seo Jang Ho<br/>[@wkd-gh](https://github.com/wkd-gh)<br/>Data Preprocess, Streamlit|Kim Ji Yeon<br/>[@wldus0210](https://github.com/wldus210)<br/>Fine Tune, Evaluation|Cho Ju Young<br/>[@chojy86](https://github.com/MartinusChoi)<br/>Crawling|

  <h3> 📎 Team Notion Page 📎 </h3>
  <a href="https://upbeat-william-67d.notion.site/3-3ccbdb236b0d40218dcced9abe1e30b2"><img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white"></a>

  <br/>
  <br/>

  <h2> 📌Project Outline📌 </h2>
  
  <h3> 📎 Topic 📎 </h3>
    
  ### LLM 을 연동한 내 외부 문서 기반 질의 응답 시스템
  ### 응급처치 대응 매뉴얼 조회 시스템  + 인근 병원 조회 서비스

  <br/>
  
  <h3> 📎 BackGround 📎 </h3>

  <img src="https://github.com/user-attachments/assets/c884a85d-1074-4389-b305-31867252ddb5" width="700" height="500"/>

  <br/>
  
  🏷 **'응급 처치 절차'** 는 '골든 타임' 내에 수행될 경우 생존률을 매우 향상시킬 수 있는 중요한 내용이다.
  
  🏷 이에 따라 '응급 처치'에 관한 교육이 확대되고 있지만, **실제로 이해하고 기억하는 비율은 11.7%에 불과**하다고 한다.
  
  🏷 실제로 갑자기 눈 앞에 응급상황이 펼쳐졌을 때, **곧바로 자신있게 대응할 수 있는 사람은 많지 않을 것**이다.
  
  🏷 이에 따라, 그 자리에 **'응급 처치 절차'에 대해 알려주고**, **원하는 지역의 병원을 알려줄 수 있는 시스템**은 갑자기 발생할 수 있는 상황에서 주변의 소중한 사람을 지켜줄 수 있는 **든든한 조력자**가 될 것이다.

  <br/>
   
  <h3> 📎 Outline 📎 </h3>

  <img src="https://github.com/user-attachments/assets/450e0de6-0e49-4f6c-9210-4e626e95f894" width="700" height="500"/>

  ### [ 개요 ]

  🏷 응급처치에 대한 메뉴얼 제공, 인근 병원 위치(기본정보) 제공

  🏷 응급처치에 대한 메뉴얼 제공 : pdf 메뉴얼 정보 + 크롤링 정보 → RAG 기반 답변 제공
  
  🏷 인근 병원 위치(기본정보) 제공 : CSV을 기반으로 RAG 기반 답변 제공
  
  ### [ 데이터 ]

  🏷 정부 누리 집 응급 처치 가이드 (pdf)

  🏷 스포츠 안전 재단 응급처치 매뉴얼(pdf파일)

  🏷 공공 데이터 지역 별 의료 시설 현황 (csv)

  ### [ 베이스 모델 ]
  
  🏷 gpt-4o-mini

  ### [ 어플리케이션 형태 ]

  🏷 Streamlit 기반 Chat-Bot

  ### [ 주요 산출물 ]

  🏷 웹-어플리케이션

  🏷 보고서 

  🏷 발표 자료


  <br/>
  <br/>

  <h2> 📌 Application Overview 📌 </h2>

  <img src="https://github.com/user-attachments/assets/e93a88a4-5d13-4a7f-86a1-fbd596583f2f" width="1000" height="480"/>
  
  🏷 시작 화면 : 응급처치 메뉴얼 과 병원 정보를 물어볼 수 있는 채팅창, 병원을 검색할 수 있는 사이드 검색 창

  <br/>

  <img src="https://github.com/user-attachments/assets/cfd6cfd2-ddf6-4375-b0af-bea09900219d" width="1000" height="480"/>
  
  🏷 응급 처치 절차 질문

  <br/>

  <img src="https://github.com/user-attachments/assets/90df97d3-7103-4f12-85b3-242c847bf520" width="1000" height="480"/>
  
  🏷 인근 병원 정보 검색

  <br/>

  <img src="https://github.com/user-attachments/assets/45a7ec94-3497-4f53-b023-bb1cb9a63109" width="1000" height="480"/>

  🏷 좌측 사이드 검색 바에서 병원 정보 검색

<br/>
<br/>

<h2> 📌 Fine-Tuning 📌 </h2>

<h3> 📎 Data Format 📎 </h3>

<img src="https://github.com/user-attachments/assets/1876cb96-4dab-4d61-8913-05c4481e0c80" width="850" height="300"/>

🏷 OpenAI API를 활용하여 응급처치 메뉴얼에서 텍스트를 추출하여 question, answer 예시 데이터 생성, jsonl 파일화

🏷 Fine-tuning data 수 : 133 QA-pair
<br/>

<h3> 📎 Fine tuning 📎 </h3>

<img src="https://github.com/user-attachments/assets/b579f72a-b891-43da-be48-4d242045c7fd" width="850" height="480"/>

🏷 Training Loss : 0.4100

🏷 초기단계에서는 Loss가 높았으나, 학습이 진행됨에 따라 안정적으로 감소함.

<br/>

<h3> 📎 Evaluation 📎 </h3>

### [답변 분석]

<img src="https://github.com/user-attachments/assets/83502f1f-e696-4d12-baa6-0eeace8c6e51" width="850" height="250"/>

🏷 파인튜닝 이전 답변

🏷 매우 상세하지만 질문에 대한 핵심 응답이 부각되지 않고 불필요하게 상세함

<img src="https://github.com/user-attachments/assets/0e664801-1539-49f3-91fa-3358419b58c3" width="850" height="60"/>

🏷 파인튜닝 이후 답변

🏷 “흐르는 찬물에 환부를 식히고, 깨끗한 거즈로 덮어 감염 방지”라는 내용으로 질문에 바로 응답

🏷 기본 모델 대비 질문 의도에 더 적합하고 간결하게 응답 제공

<br/>

### [평가 지표]

| 🏷 모델 평가에 BERTscore, Hallucination Score 사용 |
|:-:|
| **BERTscore** : 모델이 생성한 응답과 참조 텍스트 간 의미적 유사성 측정 |
| **Precision** : 의미적으로 유사한 부분의 비율 |
| **Recall** : 참조 텍스트의 의미를 얼마나 잘 포함하고 있는지 측정 |
| **F1 Score** : Precision과 Recall의 조화 평균 |
| **Hallucination Score** : 생성된 응답이 참조 텍스트와 전혀 관련 없는 내용을 포함했는지 측정 |


| **<기본 모델 성능>** |
|  :-: |
| **🏷 BERTScore** |
| Precision: 55.71 |
| Recall: 73.02 |
| F1 Score: 63.05 |
| **🏷 Hallucination Score** |
| Hallucination Score: 0.00% |


| **<파인튜닝 모델 성능>** |
|  :-: |
| **🏷 BERTScore** |
| Precision: 69.50 |
| Recall: 79.33 |
| F1 Score: 73.77 |
| **🏷 Hallucination Score** |
| Hallucination Score: 0.00% |

### 결론 

🏷 BERTScore : 파인튜닝된 모델이 Precision에서 13.79%p 증가, Recall에서 6.31%p 증가, F1 Score에서 10.72%p 증가

🏷 Hallucination Score: 모두 0.00%로, 허구적 응답을 생성하지 않았음

🏷 기본모델에 비해 파인튜닝 된 모델이 전반적으로 향상되었으며, 허구적 응답 생성이 발생하지 않는 안정적인 성능을 보임



<br/>
<br/>
    
  <h2>📌 Comment 📌</h2>

  ### 🏷 최영민

  LLM을 도메인 특화 시키고, RAG기반의 Chain을 구성하여 Chat-bot 시스템을 구현하는 전체적인 과정을 모두 경험할 수 있는 값진 시간이었습니다. 팀원들 모두 열정적으로 참여해주어 완성도 높은 결과를 만들 수 있었습니다. Langchain, RAG, GPT-4o 등 최신 기술들을 활용해보면서 앞으로 생성형 LLM 기반 프로젝트를 진행할 때 참고할 수 있을 만한 기준점이 될 수 있을 것 같아 뿌듯합니다.

  ### 🏷 서장호

  여러가지 API키를 사용해보면서 결과가 나오는 것을 보며 재미를 느꼈고 시간만 더 많았다면 더 다양한 기능들을 넣어서 완성해보고 싶다는 욕심이 생긴 시간이었습니다

  ### 🏷 김지연

  이번 프로젝트는 한달간 배운 내용들로 직접 llm을 구현하고 파인튜닝을 진행해보며 많이 성장할 수 있는 값진 기회였던 것 같습니다! 팀원분들 수고하셨습니다:)

  ### 🏷 조주영

  LLM을 배우면서 텍스트전처리 과정이 제일 중요한 것을 이번 프로젝트를 하면서 깨달았습니다. 웹 크롤링 후에 텍스트 전처리 하지 않으면 활용가치가 떨어지고, 다음 스텝에 영향이 미치게 되어서 "좋은 결과가 만들어지지 않는다"는것을 배운 기회가 되었습니다.


<br/>
<br/>
    
  <h2>📫 How to reach Team 📫 </h2>

  [![Gmail](https://img.shields.io/badge/Gmail-EA4335?style=flat-square&logo=Gmail&logoColor=white)](martinus.choi@gmail.com)
  [![Naver](https://img.shields.io/badge/Naver-03C75A?style=flat-square&logo=Naver&logoColor=white)](martinus99@naver.com)

<br/>
<br/>

  <h2> ✋ Todays ✋</h2>

  [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FMartinusChoi&count_bg=%23636ADD&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

</div>