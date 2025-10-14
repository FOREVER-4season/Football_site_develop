from flask import Blueprint, redirect, url_for, render_template, request, flash, jsonify
from datetime import datetime, timedelta   # ✅ datetime, timedelta import
from setting.models import StadiumMatch, MatchTime
# -----------------------------
# 메인 페이지용 Blueprint 생성
# -----------------------------
# name: 'main' → 블루프린트 이름
# __name__: 현재 모듈 이름
# url_prefix='/' → 모든 라우트 경로 앞에 '/'가 붙음 (즉, 루트 경로)
bp = Blueprint('main', __name__, url_prefix='/')


# -----------------------------
# 루트 경로 ('/') 라우트
# -----------------------------
@bp.route('/')
def index():
    # 요청 URL에서 "date" 파라미터를 가져옵니다 (YYYY-MM-DD 형식 예상)
    date_str = request.args.get("date")

    if date_str:
        # date_str이 있다면 문자열을 datetime 객체로 변환
        start_day = datetime.strptime(date_str, "%Y-%m-%d")
    else:
        # 없으면 기본값으로 오늘 날짜 사용
        start_day = datetime.today()

    # 날짜는 자정(00:00:00)부터 시작하도록 시간 초기화
    start_day = start_day.replace(hour=0, minute=0, second=0, microsecond=0)
    # 하루 뒤 자정을 end_day로 설정 (하루 범위 지정)
    end_day = start_day + timedelta(days=1)

    # StadiumMatch와 MatchTime 테이블 조인
    # MatchTime.start_time이 지정한 날짜 범위 내에 있는 경기들만 조회
    stadium_matches = (
        StadiumMatch.query
        .join(MatchTime)
        .filter(MatchTime.start_time >= start_day, MatchTime.start_time < end_day)
        .order_by(MatchTime.start_time)  # 경기 시작 시각 기준 정렬
        .all()
    )

    result = []
    for sm in stadium_matches:
        # 예약된 인원 수 (UserMatch 테이블 관계에서 count)
        reserved = len(sm.user_matches)
        # 경기장 최대 수용 인원
        capacity = sm.stadium.headcount

        # 기본 상태는 "신청가능"
        status = "신청가능"
        # 예약 인원이 전체 수용의 2/3 이상이면 "마감임박" 상태로 변경
        if reserved >= capacity / 3 * 2 and reserved < capacity :
            status = "마감임박"
        elif reserved == capacity:
            status = "신청마감"

        # 경기 정보를 딕셔너리로 구성하여 리스트에 추가
        result.append({
            "id": sm.id,                                 # 경기 고유 ID
            "stadium_name": sm.stadium.name,             # 경기장 이름
            "start_time": sm.matchtime.start_time.strftime("%H:%M"),  # 시작 시간 (HH:MM)
            "end_time": sm.matchtime.end_time.strftime("%H:%M"),      # 종료 시간 (HH:MM)
            "reserved": reserved,                        # 예약 인원
            "capacity": capacity,                        # 최대 수용 인원
            "status": status                             # 신청 상태
        })

    # 완성된 경기 리스트를 main.html 템플릿에 전달하여 렌더링
    return render_template("main.html", matches=result)


# -----------------------------
# Ajax API: 날짜별 경기 JSON 반환
# -----------------------------
@bp.route('/api/matches')
def api_matches():
    date_str = request.args.get("date")
    if not date_str:
        return jsonify([])

    try:
        start_day = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return jsonify([])

    start_day = start_day.replace(hour=0, minute=0, second=0, microsecond=0)
    end_day = start_day + timedelta(days=1)

    stadium_matches = (
        StadiumMatch.query
        .join(MatchTime)
        .filter(MatchTime.start_time >= start_day, MatchTime.start_time < end_day)
        .order_by(MatchTime.start_time)
        .all()
    )

    result = []
    for sm in stadium_matches:
        reserved = len(sm.user_matches)
        capacity = sm.stadium.headcount

        status = "신청가능"
        if reserved >= capacity / 3 * 2 and reserved < capacity:
            status = "마감임박"
        elif reserved == capacity:
            status = "신청마감"

        result.append({
            "id": sm.id,
            "stadium_name": sm.stadium.name,
            "start_time": sm.matchtime.start_time.strftime("%H:%M"),
            "status": status
        })

    return jsonify(result)
