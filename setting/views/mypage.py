from datetime import datetime
from flask import Blueprint, render_template, request, jsonify, abort,session
from setting import db
from setting.models import User, Stadium, MatchTime, StadiumMatch, UserMatch   # Manager 제거
from setting.views.auth import login_required

bp = Blueprint('mypage', __name__, url_prefix='/mypage')

# 페이지: 나의 플랩
@bp.get("/users/<int:user_id>")
@login_required
def my_page(user_id: int):
    logged_in_user_id = session.get('user_id')
    if user_id != logged_in_user_id:
        abort(403)  # from flask import abort

    user = User.query.get_or_404(user_id)
    match_count = UserMatch.query.filter_by(user_id=user_id).count()
    return render_template(
        "mypage/mypage.html",
        user=user,
        match_count=match_count,
    )

# API: 사용자 조회
# @bp.get("/api/users/<int:user_id>")
# def api_user(user_id: int):
#     u = User.query.get_or_404(user_id)
#     return jsonify({
#         "user_id": u.user_id,
#         "email": u.email,
#         "nickname": u.nickname,
#         "money": u.money,
#         "photo_number": u.photo_number,
#         "matches": [um.usermatch_id for um in u.match_list],
#     })
#
# # API: 매치 목록
# @bp.get("/api/stadium-matches")
# def api_stadium_matches():
#     items = StadiumMatch.query.all()
#
#     def row(sm: StadiumMatch):
#         return {
#             "id": sm.id,
#             "pay": sm.pay,
#             "stadium": {
#                 "id": sm.stadium.stadium_id,
#                 "name": sm.stadium.name,
#                 "location": sm.stadium.location,
#                 "headcount": sm.stadium.headcount,
#                 "entry_fee": sm.stadium.entry_fee,
#             },
#             "time": {
#                 "start": sm.matchtime.start_time.isoformat(),
#                 "end": sm.matchtime.end_time.isoformat(),
#             },
#             # Manager 제거 → stadium_match에서 manager 접근 안 함
#             "applied_users": [um.user_id for um in sm.user_matches],
#         }
#
#     return jsonify([row(sm) for sm in items])
#
# # API: 매치 신청
# @bp.post("/api/apply")
# def api_apply():
#     data = request.get_json(silent=True) or {}
#     user_id = data.get("user_id")
#     stadium_match_id = data.get("stadium_match_id")
#
#     if not user_id or not stadium_match_id:
#         abort(400, "user_id and stadium_match_id required")
#
#     user = User.query.get_or_404(user_id)
#     sm = StadiumMatch.query.get_or_404(stadium_match_id)
#
#     exists = UserMatch.query.filter_by(user_id=user.user_id, stadium_match_id=sm.id).first()
#     if exists:
#         return jsonify({"ok": False, "message": "already applied"}), 200
#
#     um = UserMatch(user_id=user.user_id, stadium_match_id=sm.id)
#     db.session.add(um)
#     db.session.commit()
#     return jsonify({"ok": True, "usermatch_id": um.usermatch_id})
#
# # 초기 샘플 데이터 생성용 라우트
# @bp.post("/dev/seed")
# def dev_seed():
#     if User.query.first():
#         return jsonify({"ok": True, "message": "already seeded"})
#
#     u = User(password="hashed", email="spring@gmail.com", money=0, nickname="혜영이", photo_number="KAKAO")
#     s = Stadium(name="플랩 아레나", location="서울 성동구", photo=None, headcount=10, entry_fee=5000)
#     t = MatchTime(start_time=datetime(2025, 10, 1, 19, 0), end_time=datetime(2025, 10, 1, 21, 0))
#     sm = StadiumMatch(stadium=s, matchtime=t, pay=12000)   # Manager 제거
#
#     db.session.add_all([u, s, t, sm])
#     db.session.commit()
#     return jsonify({"ok": True})
