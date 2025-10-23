from setting import db

# User 모델
class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    money = db.Column(db.Integer, nullable=True, default=0)
    nickname = db.Column(db.String(10), nullable=False)
    photo_number = db.Column(db.String(15),nullable=False)

    match_list = db.relationship("UserMatch", back_populates="user", cascade="all, delete-orphan")

# Stadium 모델
class Stadium(db.Model):
    __tablename__ = "stadium"
    stadium_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    photo = db.Column(db.String(300))
    headcount = db.Column(db.Integer, nullable=False)
    entry_fee = db.Column(db.Integer, nullable=False)

    stadium_match = db.relationship("StadiumMatch", back_populates="stadium")

# MatchTime 모델
class MatchTime(db.Model):
    __tablename__     = "matchtime"
    matchtime_id      = db.Column(db.Integer, primary_key=True)
    start_time        = db.Column(db.DateTime, nullable=False)
    end_time          = db.Column(db.DateTime, nullable=False)

    stadium_match     = db.relationship("StadiumMatch", back_populates="matchtime")

# StadiumMatch 모델
class StadiumMatch(db.Model):
    __tablename__   = "stadium_match"
    id              = db.Column(db.Integer, primary_key=True)
    stadium_id      = db.Column(db.Integer, db.ForeignKey("stadium.stadium_id"), nullable=False)
    matchtime_id    = db.Column(db.Integer, db.ForeignKey("matchtime.matchtime_id"), nullable=False)
    manager_id      = db.Column(db.Integer, db.ForeignKey("manager.manager_id"), nullable=True, default=1)
    pay             = db.Column(db.Integer, nullable=False)

    stadium         = db.relationship("Stadium", back_populates="stadium_match")
    matchtime       = db.relationship("MatchTime", back_populates="stadium_match")
    manager         = db.relationship("Manager", back_populates="stadium_match")

    user_matches = db.relationship("UserMatch", back_populates="stadium_match", cascade="all, delete-orphan")


# UserMatch 모델
class UserMatch(db.Model):
    __tablename__    = "usermatch"
    usermatch_id     = db.Column(db.Integer, primary_key=True)

    user_id          = db.Column(db.Integer, db.ForeignKey("user.user_id", ondelete="CASCADE"), nullable=False)
    stadium_match_id = db.Column(db.Integer, db.ForeignKey("stadium_match.id", ondelete="CASCADE"), nullable=False)

    user             = db.relationship("User", back_populates="match_list")
    stadium_match    = db.relationship("StadiumMatch", back_populates="user_matches")


# Manager 모델
class Manager(db.Model):
    __tablename__   = "manager"
    manager_id      = db.Column(db.Integer, primary_key=True)
    password        = db.Column(db.String(20), nullable=False)
    email           = db.Column(db.String(200), nullable=False)
    nickname        = db.Column(db.String(10), nullable=False)
    number          = db.Column(db.String(15))

    stadium_match   = db.relationship("StadiumMatch", back_populates="manager")







