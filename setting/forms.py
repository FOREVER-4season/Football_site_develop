from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SelectField, DateField, RadioField, BooleanField,SelectMultipleField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Email, Regexp, NumberRange


class UserCreateForm(FlaskForm):
    username = StringField('이름', validators=[DataRequired(message='아이디를 입력해 주세요')])
    password1 = PasswordField('비밀번호', validators=[DataRequired(message='비밀번호를 입력해 주세요'), EqualTo('password2', message='비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired(message='비밀번호가 틀립니다')])
    email = EmailField('이메일', validators=[DataRequired(message='이메일을 입력해 주세요'), Email()])
    phone_number =StringField('전화번호', validators=[
        DataRequired(message='전화번호를 입력해 주세요'),
        Length(min=10, max=15, message='전화번호는 10~15자리여야 합니다.'),
        Regexp(r'^\+?[\d\s-]+$', message='유효한 전화번호 형식이 아닙니다.')  # 간단한 정규식 예시
    ])

    birth_year = SelectField('년', choices=[('', '년도')]+[(str(y), str(y)) for y in range(2025, 1940,-1)], validators=[DataRequired()])
    birth_month = SelectField('월', choices=[('', '월')]+[(str(m), str(m)) for m in range(1, 13)], validators=[DataRequired()])
    birth_day = SelectField('일', choices=[('', '일')]+[(str(d), str(d)) for d in range(1, 32)], validators=[DataRequired()])
    gender = RadioField('성별', choices=[('male', '남자'), ('female', '여자')], validators=[DataRequired()])
    agree_all = BooleanField('전체 동의')
    agree_age = BooleanField('만 16세 이상입니다 (필수)', validators=[DataRequired()])
    agree_personal = BooleanField('개인정보 수집 및 이용 동의 (필수)', validators=[DataRequired()])
    agree_terms = BooleanField('이용약관 동의 (필수)', validators=[DataRequired()])
    agree_marketing = BooleanField('개인정보 마케팅 동의 (선택)')
    agree_event = BooleanField('이벤트 및 맞춤 정보 문자 수신 (선택)')



class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(message="아이디를 정확히 입력해주세요"), Length(min=1, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired(message="비밀번호를 정확히 입력해주세요")])



class StadiumForm(FlaskForm):
    name =StringField('구장', validators=[DataRequired(message="구장을 정확히 입력해주세요")])
    location =StringField('지역', validators=[DataRequired(message="지역을 정확히 입력해주세요")])
    photo =StringField('사진')
    headcount =SelectField('인원',choices=[('15', '5vs5vs5'),('18', '6vs6vs6'),('24', '8vs8vs8'),('22', '11vs11')],render_kw={"class": "custom-select"})
    entry_fee =SelectField('금액',choices=[('9000', '9000원'),('10000', '10000원'),('11000', '11000원'),('12000', '12000원')],render_kw={"class": "custom-select"})


class TimeForm(FlaskForm):
    day        =DateField("날짜", format="%Y-%m-%d", validators=[DataRequired()])
    times = SelectMultipleField("시간",choices=[("09:00", "09시"), ("10:00", "10시"), ("11:00", "11시"), ("12:00", "12시"), ("14:00", "14시"), ("16:00", "16시"), ("18:00", "18시"), ("20:00", "20시"), ("22:00", "22시")],validators=[DataRequired()])

class StadiumMatchForm(FlaskForm):
    stadium_id = SelectField("경기장 선택", coerce=int, validators=[DataRequired()])
    matchtime_id = SelectField("경기 시간 선택", coerce=int, validators=[DataRequired()])
    pay = IntegerField("결제 금액", validators=[DataRequired(), NumberRange(min=0)])


class M_loginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(message="아이디를 정확히 입력해주세요"), Length(min=1, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired(message="비밀번호를 정확히 입력해주세요")])