# money.py
from flask import Blueprint, render_template, request, jsonify, g, current_app, url_for, redirect
from setting import db
from pathlib import Path
TEMPLATES_DIR = Path(__file__).resolve().parents[2] / 'templates'

bp = Blueprint('money', __name__, url_prefix='/money')

@bp.route('/', methods=['GET'])
def view():
    if g.user is None:
        return redirect(url_for('auth.login'))
    money = int(g.user.money or 0)
    return render_template('mypage/money.html',
                           money=money,
                           formatted_money=f"{money:,}")

@bp.route('/balance', methods=['GET'])
def balance():
    if g.user is None:
        return jsonify(ok=False, msg='로그인이 필요합니다'), 401
    money = int(g.user.money or 0)
    return jsonify(ok=True, money=money, formatted_money=f"{money:,}")

@bp.route('/fake_pay', methods=['POST'])
def fake_pay():
    if g.user is None:
        return jsonify(ok=False, msg='로그인이 필요합니다'), 401
    data = request.get_json(silent=True) or {}
    try:
        amount = int(str(data.get('amount', 0)))
    except Exception:
        return jsonify(ok=False, msg='금액 오류'), 400
    if amount < 100:
        return jsonify(ok=False, msg='최소 100원'), 400
    g.user.money = (g.user.money or 0) + amount
    db.session.commit()
    money = int(g.user.money or 0)
    return jsonify(ok=True, money=money, formatted_money=f"{money:,}")

@bp.route('/refund', methods=['POST'])
def refund():
    if g.user is None:
        return jsonify(ok=False, msg='로그인이 필요합니다'), 401

    data = request.get_json(silent=True) or {}
    try:
        amount = int(str(data.get('amount', 0)))
    except Exception:
        return jsonify(ok=False, msg='금액 오류'), 400

    if amount < 100:
        return jsonify(ok=False, msg='최소 100원'), 400

    cur = int(g.user.money or 0)
    if amount > cur:
        return jsonify(ok=False, msg='잔액 부족'), 400

    g.user.money = cur - amount
    db.session.commit()
    money = int(g.user.money or 0)
    return jsonify(ok=True, money=money, formatted_money=f"{money:,}")
