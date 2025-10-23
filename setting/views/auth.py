from flask import Blueprint, render_template, redirect,  url_for, flash,request,session,g
from werkzeug.security import generate_password_hash, check_password_hash
import functools

bp=Blueprint('auth',__name__,url_prefix='/auth')

from setting import db
from setting.forms import UserCreateForm, UserLoginForm
from setting.models import User

#회원가입 라우트
@bp.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = UserCreateForm()
    if form.validate_on_submit():
        # 닉네임 중복 체크
        user = User.query.filter_by(nickname=form.username.data).first()
        if user:
            flash('이미 존재하는 사용자입니다.')
            return render_template('auth/register.html', form=form)

        new_user = User(
            nickname=form.username.data,
            password=generate_password_hash(form.password1.data),
            email=form.email.data,
            photo_number=form.phone_number.data,
            money=0
        )
        db.session.add(new_user)
        db.session.commit()
        flash('회원가입이 완료되었습니다.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


#로그인 라우트
@bp.route('/login/', methods=['GET', 'POST'])
def login():
    form=UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        errormsg = None
        user = User.query.filter_by(nickname=form.username.data).first()
        if not user:
            errormsg = '존재하지 않는 사용자입니다.'
        elif not check_password_hash(user.password, form.password.data):
            errormsg = '비밀번호가 올바르지 않습니다.'
        if errormsg is None:
            session.clear()
            session['user_id'] = user.user_id
            _next = request.args.get('next','')
            if _next:
                return redirect(_next)
            else:
                return redirect(url_for('main.index'))
        flash(errormsg)

    return render_template('auth/login.html',form=form)

#유저제한 함수
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(int(user_id))

#로그아웃 함수
@bp.route('logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))

#이거 굉장히 중요함 뭔가 링크 연결시켜주는 코드이므로 잘 분석해보기
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.user is None:
            _next=request.url if request.method == 'GET' else ''
            return redirect(url_for('auth.login', next=_next))
        return view(*args, **kwargs)
    return wrapped_view