from datetime import datetime

from . import db


class Ping(db.Model):
    __tablename__ = "pings"

    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(50))

    def __repr__(self) -> str:
        return f"<Ping {self.id}: {self.note}>"

#
# 👤 Usuarios
#
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relación con las skills del usuario
    skills = db.relationship(
        "UserSkill",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<User {self.id}: {self.email}>"


#
# 🧩 Skills
#
class Skill(db.Model):
    __tablename__ = "skills"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    # Usuarios que tienen esta skill
    users = db.relationship(
        "UserSkill",
        back_populates="skill",
        cascade="all, delete-orphan",
    )

    # Ofertas que requieren esta skill
    job_requirements = db.relationship(
        "JobSkillRequirement",
        back_populates="skill",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<Skill {self.id}: {self.name}>"


#
# 👤🧩 Relación User-Skill
#
class UserSkill(db.Model):
    __tablename__ = "user_skills"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
    )
    skill_id = db.Column(
        db.Integer,
        db.ForeignKey("skills.id"),
        nullable=False,
    )
    # Ej: "beginner", "intermediate", "advanced"
    level = db.Column(db.String(20), nullable=False)

    user = db.relationship("User", back_populates="skills")
    skill = db.relationship("Skill", back_populates="users")

    def __repr__(self) -> str:
        return f"<UserSkill user={self.user_id} skill={self.skill_id} level={self.level}>"


#
# 💼 Ofertas de trabajo
#
class JobOffer(db.Model):
    __tablename__ = "job_offers"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    company = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(100))  # "Remote", "Santiago", etc.
    seniority = db.Column(db.String(50))  # "junior", "mid", "senior"
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    # Skills requeridas por esta oferta
    skill_requirements = db.relationship(
        "JobSkillRequirement",
        back_populates="job_offer",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<JobOffer {self.id}: {self.title} @ {self.company}>"


#
# 💼🧩 Skills requeridas por oferta
#
class JobSkillRequirement(db.Model):
    __tablename__ = "job_skill_requirements"

    id = db.Column(db.Integer, primary_key=True)
    job_offer_id = db.Column(
        db.Integer,
        db.ForeignKey("job_offers.id"),
        nullable=False,
    )
    skill_id = db.Column(
        db.Integer,
        db.ForeignKey("skills.id"),
        nullable=False,
    )
    # Ej: "beginner", "intermediate", "advanced"
    level_required = db.Column(db.String(20), nullable=False)
    # 1–5 qué tan importante es esta skill
    importance = db.Column(db.Integer, default=3)

    job_offer = db.relationship("JobOffer", back_populates="skill_requirements")
    skill = db.relationship("Skill", back_populates="job_requirements")

    def __repr__(self) -> str:
        return (
            f"<JobSkillRequirement job={self.job_offer_id} "
            f"skill={self.skill_id} level={self.level_required} importance={self.importance}>"
        )
