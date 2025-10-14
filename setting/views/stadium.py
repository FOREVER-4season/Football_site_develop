from flask import Blueprint, request, render_template, redirect, url_for, flash, g, jsonify
from setting import db
from setting.models import MatchTime, StadiumMatch, UserMatch
from datetime import datetime, timedelta

bp = Blueprint('stadium', __name__, url_prefix='/stadium')


# ============================================
# ✅ 경기 목록 조회 (특정 날짜 기준)
# ============================================
@bp.route("/", methods=["GET"])
def get_matches():
    date_str = request.args.get("date")

    if date_str:
        start_day = datetime.strptime(date_str, "%Y-%m-%d")
    else:
        start_day = datetime.today()

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

        # 기본 상태
        status = "신청가능"
        if reserved >= capacity / 3 * 2 and reserved < capacity:
            status = "마감임박"
        elif reserved == capacity:
            status = "신청마감"

        # ✅ 로그인 유저가 이미 신청한 경우 → 신청완료
        if g.user:
            if any(um.user_id == g.user.user_id for um in sm.user_matches):
                status = "신청완료"

        result.append({
            "id": sm.id,
            "stadium_name": sm.stadium.name,
            "start_time": sm.matchtime.start_time.strftime("%H:%M"),
            "end_time": sm.matchtime.end_time.strftime("%H:%M"),
            "reserved": reserved,
            "capacity": capacity,
            "status": status
        })

    return render_template("stadium/stadium_list.html", matches=result)


# ============================================
# ✅ 경기 상세 페이지
# ============================================
@bp.route("/<int:match_id>", methods=["GET"])
def match_detail(match_id):
    match = StadiumMatch.query.get_or_404(match_id)

    reserved = len(match.user_matches)
    capacity = match.stadium.headcount

    # 기본 상태
    status = "신청가능"
    if reserved >= capacity / 3 * 2 and reserved < capacity:
        status = "마감임박"
    elif reserved == capacity:
        status = "신청마감"

    # ✅ 로그인 유저가 이미 신청한 경우 → 신청완료
    if g.user:
        if any(um.user_id == g.user.user_id for um in match.user_matches):
            status = "신청완료"

    return render_template(
        "stadium/stadium_detail.html",
        match=match,
        stadium=match.stadium,
        reserved=reserved,
        capacity=capacity,
        status=status
    )


# ============================================
# ✅ 경기 신청하기
# ============================================
@bp.route("/apply/<int:match_id>", methods=["POST"])
def apply_match(match_id):
    match = StadiumMatch.query.get_or_404(match_id)

    # 로그인 확인
    if not g.user:
        flash("로그인이 필요합니다.", "warning")
        return redirect(url_for("auth.login"))

    # 정원 마감 확인
    if len(match.user_matches) >= match.stadium.headcount:
        flash("정원이 마감되었습니다!", "danger")
        return redirect(url_for("stadium.match_detail", match_id=match.id))

    # 중복 신청 확인
    existing = UserMatch.query.filter_by(user_id=g.user.user_id, stadium_match_id=match.id).first()
    if existing:
        flash("이미 신청한 경기입니다!", "info")
        return redirect(url_for("stadium.match_detail", match_id=match.id))

    # 신청 저장
    booking = UserMatch(user_id=g.user.user_id, stadium_match_id=match.id)
    db.session.add(booking)
    db.session.commit()

    flash("신청이 완료되었습니다!", "success")
    return redirect(url_for("stadium.match_detail", match_id=match.id))
