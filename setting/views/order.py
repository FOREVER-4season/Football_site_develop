from flask import Blueprint, request, render_template, redirect, url_for, flash, g, abort
from setting import db, models
from setting.models import  StadiumMatch, UserMatch


bp = Blueprint('order', __name__, url_prefix='/order')

@bp.route('/<int:order_id>',methods=["GET"])
def order(order_id):
    stadiummatch_id = models.StadiumMatch.query.get_or_404(order_id)
    if stadiummatch_id is None:
        abort(404)
    else:

        return render_template("matches/match_pay.html",stadiummatch_id=stadiummatch_id)






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
