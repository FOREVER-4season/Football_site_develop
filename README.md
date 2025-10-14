<h1 align="center">⚽ 풋살경기 예약 플랫폼 - FLAB</h1>

## 📑 목차
- [👶 개요](#-개요)
- [❤️ 팀원 소개](#-팀원-소개)
- [⚙️ 기술 스택 및 도구](#-기술-스택-및-도구)
- [⚙️ 핵심 기능](#-핵심-기능)
- [🧱 프로젝트 설계, 구현](#-프로젝트-설계-구현)
- [📸 주요기능 실행 화면](#-주요기능-실행-화면)
- [📝 소감문](#-소감문)

---

## 👶 개요
- 프로젝트 목표 : 플라스크 파이썬 기반 다양한 API를 이용한 축구 구장 예약 중계 웹사이트 개발 프로젝트  
- 개발 기간 : 25/9/23 ~ 25/10/12  

---

## ❤️ 팀원 소개
<div align="center">

<table>
  <tr>
    <!-- spring -->
    <td align="center" width="230" style="vertical-align: top;">
      <img src="setting/static/img/hi1.jpg" width="120" height="150" alt="spring"><br><br>
      <b>박혜영 (spring)</b>
      <div style="width:60%;margin:6px auto;border-bottom:1px solid #aaa;"></div>
      <sub><b>Frontend / UI / 게시판</b></sub><br>
      <sub>공지사항 게시판 제작, 헤더/푸터 컴포넌트 구성,<br>게시물 정렬 및 jQuery UI 구현</sub><br><br>
      <a href="https://github.com/gangazigood"><img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white"></a>
    </td>
    <td align="center" width="230" style="vertical-align: top;">
      <img src="setting/static/img/hi2.jpg" width="120" height="150" alt="summer"><br><br>
      <b>백기림 (summer)</b>
      <div style="width:60%;margin:6px auto;border-bottom:1px solid #aaa;"></div>
      <sub><b>인증 / 배포 / DevOps</b></sub><br>
      <sub>회원가입 및 로그인 로직 구현,<br>이메일 구독, AWS EC2 + Gunicorn 배포 환경 구축</sub><br><br>
      <a href="https://github.com/girintr"><img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white"></a>
    </td>
    <td align="center" width="230" style="vertical-align: top;">
      <img src="setting/static/img/hi3.jpg" width="120" height="150" alt="autumn"><br><br>
      <b>이윤서 (autumn)</b>
      <div style="width:60%;margin:6px auto;border-bottom:1px solid #aaa;"></div>
      <sub><b>게시판 / 보안 / UI</b></sub><br>
      <sub>게시판 CRUD 로직, 파일 암호화 처리,<br>Bootstrap 기반 인터페이스 개선</sub><br><br>
      <a href="https://github.com/yoo05-seo"><img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white"></a>
    </td>
    <td align="center" width="230" style="vertical-align: top;">
      <img src="setting/static/img/hi4.jpg" width="120" height="150" alt="winter"><br><br>
      <b>박종훈 (winter)</b>
      <div style="width:60%;margin:6px auto;border-bottom:1px solid #aaa;"></div>
      <sub><b>핵심 비즈니스 로직 / DB 설계</b></sub><br>
      <sub>풋살 경기 예약 및 취소 관리,<br>Flatpickr 달력 기반 경기 조회,<br>DB 모델링 및 Flask Blueprint 설계</sub><br><br>
      <a href="https://github.com/dailyhune"><img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white"></a>
    </td>
  </tr>
</table>

</div>

---

## ⚙️ 기술 스택 및 도구
**Front-end:** HTML5, CSS3, Bootstrap5, jQuery, Flatpickr.js  
**Back-end:** Python (Flask)  
**DB:** SQLAlchemy  
**Cloud:** AWS, Docker  
**ETC:** Git, GitHub, Figma  

---

## ⚙️ 핵심 기능

### 👤 일반 회원
- **로그인 / 회원가입** — 계정을 생성하고 개인화된 서비스를 이용  
- **구장 정보 조회** — 등록된 풋살장 정보 및 예약 가능 일정 확인  
- **구장 예약 / 취소** — 원하는 날짜와 시간대에 풋살장 예약 및 취소  
- **이용비 충전/환불** — 원하는 금액을 충전하거나 환불 가능  
- **마이페이지** — 나의 예약 내역, 충전하기, 회원 정보 관리  

### 🛠️ 관리자
- **풋살장 등록 / 수정 / 삭제** — 관리자 권한으로 구장 정보 관리  
- **예약 관리** — 회원들의 예약 현황 확인 및 직접 예약 가능  
- **경기 일정 추가** — 풋살 경기 스케줄 생성 및 관리  

---

## 🧱 프로젝트 설계, 구현
> PPT나 ERD, 플로우차트 이미지 등을 여기에 삽입할 예정  

---

## 📸 주요기능 실행 화면

### 회원가입/로그인
나의 정보를 입력하여 회원가입을 하거나 로그인 할 수 있습니다

### 내 경기 내역  
예약 페이지에서는 나의 예약 정보를 ‘신청한 경기’와 ‘끝난 경기’로 구분하여 확인할 수 있습니다.  
‘예약한 경기’는 결제 취소 버튼을 통해 예약을 취소할 수 있고, ‘끝난 경기’는 자동으로 삭제됩니다.  

### 금액 충전/환불
마이페이지에서 충전하기를 누르면 금액을 충전하거나 환불할 수 있습니다


---

## 📝 소감문

