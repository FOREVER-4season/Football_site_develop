from flask import (
    Blueprint, render_template, redirect, url_for,
    request, flash, g
)
from setting.models import UserMatch, StadiumMatch, MatchTime
from setting import db
from datetime import datetime

bp = Blueprint("matches", __name__, url_prefix="/matches")

#----------------------------------------------------------
#✅ 아래 모든 함수들은 전부 g.user이 있어야 가능하도록 설정
#----------------------------------------------------------
@bp.before_request
def check_login():
    if not g.user:
        return redirect(url_for("auth.login"))



#----------------------------------------------------------
# ✅ 내 신청 내역 (날짜별 필터 + 캘린더)
#----------------------------------------------------------
@bp.route("/mylist/<int:user_id>")
def my_match_list(user_id: int):
    date_str = request.args.get("date")
    query = UserMatch.query.filter_by(user_id=user_id).join(StadiumMatch).join(MatchTime)

    if date_str:
        try:
            selected_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            query = query.filter(db.func.date(MatchTime.start_time) == selected_date)
        except ValueError:
            selected_date = datetime.today().date()
    else:
        selected_date = datetime.today().date()

    my_matches = query.order_by(MatchTime.start_time).all()

    return render_template(
        "matches/match_list.html",
        my_matches=my_matches,
        selected_date=selected_date
    )

#----------------------------------------------------------
# ✅ 상세페이지
#----------------------------------------------------------
@bp.route("/detail/<int:usermatch_id>")
def my_match_detail(usermatch_id):
    user_match = UserMatch.query.get_or_404(usermatch_id)
    stadium_match = user_match.stadium_match
    return render_template(
        "matches/match_detail.html",
        stadium_match=stadium_match,
        usermatch_id=usermatch_id)


#----------------------------------------------------------
# ✅ 신청 취소
#----------------------------------------------------------
@bp.route("/cancel", methods=["POST"])
def cancel_match():
    match_id = request.form.get("match_id")
    if not match_id:
        flash("잘못된 요청입니다.")
        return redirect(url_for("matches.my_match_list", user_id=g.user.user_id))

    try:
        match_id = int(match_id)
    except ValueError:
        flash("잘못된 경기 아이디입니다.")
        return redirect(url_for("matches.my_match_list", user_id=g.user.user_id))

    user_match = UserMatch.query.filter_by(usermatch_id=match_id).first()
    if not user_match:
        flash("해당 경기 신청을 찾을 수 없습니다.")
        return redirect(url_for("matches.my_match_list", user_id=g.user.user_id))

    try:
        db.session.delete(user_match)
        db.session.commit()
        flash("경기 신청이 취소되었습니다.")
    except Exception as e:
        db.session.rollback()
        flash(f"삭제 중 오류 발생: {str(e)}")

    return redirect(url_for("matches.my_match_list", user_id=g.user.user_id))



