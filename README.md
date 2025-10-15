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
      <sub><b>Frontend / Backend</b></sub><br>
      <sub>마이페이지 구현<br>머니페이지 구현</sub><br><br>
      <a href="https://github.com/gangazigood"><img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white"></a>
    </td>
    <td align="center" width="230" style="vertical-align: top;">
      <img src="setting/static/img/hi2.jpg" width="120" height="150" alt="summer"><br><br>
      <b>백기림 (summer)</b>
      <div style="width:60%;margin:6px auto;border-bottom:1px solid #aaa;"></div>
      <sub><b>Frontend / Backend</b></sub><br>
      <sub>DB구현<br>총괄</sub><br><br>
      <a href="https://github.com/girintr"><img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white"></a>
    </td>
    <td align="center" width="230" style="vertical-align: top;">
      <img src="setting/static/img/hi3.jpg" width="120" height="150" alt="autumn"><br><br>
      <b>이윤서 (autumn)</b>
      <div style="width:60%;margin:6px auto;border-bottom:1px solid #aaa;"></div>
      <sub><b>Frontend / Backend</b></sub><br>
      <sub>hreder/footer등 base.html구현<br>매니저 페이지 구현현</sub><br><br>
      <a href="https://github.com/yoo05-seo"><img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white"></a>
    </td>
    <td align="center" width="230" style="vertical-align: top;">
      <img src="setting/static/img/hi4.jpg" width="120" height="150px" alt="winter"><br><br>
      <b>박종훈 (winter)</b>
      <div style="width:60%;margin:6px auto;border-bottom:1px solid #aaa;"></div>
      <sub><b>Frontend / Backend</b></sub><br>
      <sub>Matches페이지 구현<>Flatpickr 달력 기반 경기 조회<br>stadium 페이지 구현br</sub><br><br>
      <a href="https://github.com/dailyhune"><img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white"></a>
    </td>
  </tr>
</table>

</div>

---


## ⚙️ 기술 스택 및 도구

| 영역 | 기술 스택 |
| --- | --- |
| Front-end | <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=fff"/> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=000"/> <img src="https://img.shields.io/badge/bootstrap-7952B3?style=flat-square&logo=bootstrap&logoColor=white"/> <img src="https://img.shields.io/badge/jquery-0769AD?style=flat-square&logo=jquery&logoColor=white"/> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=fff"/> |
| Back-end | <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=Flask&logoColor=white"/> |
| Database | <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white"/> |
| Cloud | <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=white"/> <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=Docker&logoColor=white"/> |
| Others | <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white"/> <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white"/> <img src="https://img.shields.io/badge/Figma-F24E1E?style=flat-square&logo=figma&logoColor=white"/> |


---

## ⚙️ 다이어그램

<details><summary><b>Class Diagram</b></summary>
<img src="readme_img/diagram1.png"/>
</details>


<details><summary>Entity Realationship Diagram</summary>
<img src="readme_img/diagram2.png"/>
</details>

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
<details><summary>PPT</summary>


</details>  

---

## 📸 주요기능 실행 화면

### 회원가입/로그인

<details>
  <summary>나의 정보를 입력하여 회원가입을 하거나 로그인 할 수 있습니다</summary>
  <br>
  <video controls width="720">
  <source src="readme_img/attachment.mp4" type="video/mp4">
  
  
### [Code](#)
</details>

### 경기신청하기

<details>
  <summary>만들어 있는 경기를 신청할 수 있습니다.</summary>
  <br>
  ![경기신청](https://github.com/user-attachments/assets/a15d249a-1935-40c1-b3d3-5e77adba0420)

</details>

### 내 경기 내역  
<details>
  <summary>예약 페이지에서는 나의 예약 정보를 ‘신청한 경기’와 ‘끝난 경기’로 구분하여 확인할 수 있습니다.  
‘예약한 경기’는 결제 취소 버튼을 통해 예약을 취소할 수 있고, ‘끝난 경기’는 자동으로 삭제됩니다.  </summary>


</details>

### 금액 충전/환불

<details><summary>마이페이지에서 충전하기를 누르면 금액을 충전하거나 환불할 수 있습니다</summary>


</details>


---

## 📝 소감문

