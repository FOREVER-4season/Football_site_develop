from datetime import datetime, timedelta

from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from werkzeug.security import check_password_hash

from setting import db
from setting.forms import StadiumForm, TimeForm, StadiumMatchForm, M_loginForm
from setting.models import Stadium, MatchTime, StadiumMatch, Manager

bp=Blueprint('manager',__name__,url_prefix='/manager')

#구장추가 라우트
@bp.route('/stadium', methods=['GET', 'POST'])
def add_stadium():
    form = StadiumForm()
    if form.validate_on_submit():
        # 구장 중복체크
        name = Stadium.query.filter_by(name=form.name.data).first()
        if name:
            flash('이미 존재하는 구장입니다.')
            return render_template('manager/m_stadium.html', form=form)

        new_stadium = Stadium(
            name=form.name.data,
            location=form.location.data,
            photo=form.photo.data,
            headcount=form.headcount.data,
            entry_fee=form.entry_fee.data
        )
        db.session.add(new_stadium)
        db.session.commit()
        flash('구장등록 완료.')
        return render_template('manager/m_stadium.html', form=form)
    return render_template('manager/m_stadium.html', form=form)

#시간추가 라우트
@bp.route('/time', methods=['GET', 'POST'])
def add_time():
    form = TimeForm()
    if form.validate_on_submit():
        day = form.day.data
        times = form.times.data

        for t in times:
            # 날짜와 시간 합치기
            datetime_str = f"{day} {t}:00.000000"
            start_dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S.%f")
            end_dt = start_dt + timedelta(hours=2)

            # 중복 체크 (start_time 기준)
            exist = MatchTime.query.filter_by(start_time=start_dt).first()
            if exist:
                flash(f'{start_dt}에 이미 등록된 시간입니다.')
                return render_template('manager/m_time.html', form=form)

            # DB에 추가
            matchtime = MatchTime(start_time=start_dt, end_time=end_dt)
            db.session.add(matchtime)

        db.session.commit()
        flash('타임 등록 완료.')
        return render_template('manager/m_time.html', form=form)
    return render_template('manager/m_time.html', form=form)

#경기추가 라우트
@bp.route('/stadium_match/add', methods=['GET', 'POST'])
def add_stadiummatch():
    form = StadiumMatchForm()
    form.stadium_id.choices = [(s.stadium_id, s.name) for s in Stadium.query.order_by(Stadium.name).all()]
    form.matchtime_id.choices = [(m.matchtime_id, f"{m.start_time.strftime('%Y-%m-%d %H:%M')} ~ {m.end_time.strftime('%H:%M')}") for m in MatchTime.query.order_by(MatchTime.start_time).all()]

    if form.validate_on_submit():
        stadium_match = StadiumMatch(
            stadium_id=form.stadium_id.data,
            matchtime_id=form.matchtime_id.data,
            pay=form.pay.data,
            manager_id=1
        )
        db.session.add(stadium_match)
        db.session.commit()
        flash('등록 완료.')
        return redirect(url_for('manager.add_stadiummatch'))

    return render_template('manager/m_stadiummatch.html', form=form)


#매니저 로그인
@bp.route('/login/', methods=['GET', 'POST'])
def m_login():
    form = M_loginForm()
    if request.method == 'POST' and form.validate_on_submit():
        errormsg = None
        user = Manager.query.filter_by(nickname=form.username.data).first()
        if not user:
            errormsg = '존재하지 않는 사용자입니다.'
        elif not check_password_hash(user.password, form.password.data):
            errormsg = '비밀번호가 올바르지 않습니다.'
        if errormsg is None:
            session.clear()
            session['user_id'] = user.user_id
            _next = request.args.get('next', '')
            if _next:
                return redirect(_next)
            else:
                return redirect(url_for('main.index'))
        flash(errormsg)

    return render_template('manager/m_login.html', form=form)
