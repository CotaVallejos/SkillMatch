from flask import Blueprint, jsonify

# Blueprint de la API
api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/health", methods=["GET"])
def api_health():
    """Endpoint simple para probar que la API funciona."""
    return jsonify({"status": "ok", "message": "API SkillMatch lista ✅"})

from flask import request
from .models import User, Skill, JobOffer, UserSkill
from . import db


# Helper para serializar usuarios
def user_to_dict(user: User):
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "created_at": user.created_at.isoformat() if user.created_at else None,
    }

def skill_to_dict(skill: Skill):
    return {
        "id": skill.id,
        "name": skill.name,
    }

def joboffer_to_dict(offer: JobOffer):
    return {
        "id": offer.id,
        "title": offer.title,
        "company": offer.company,
        "description": offer.description,
        "location": offer.location,
        "seniority": offer.seniority,
        "created_at": offer.created_at.isoformat() if offer.created_at else None,
        "is_active": offer.is_active,
    }

def user_skill_to_dict(us: UserSkill):
    return {
        "id": us.id,
        "user_id": us.user_id,
        "skill_id": us.skill_id,
        "level": us.level,
    }

# =========================
# CRUD de Users
# =========================

# GET /api/users  → lista todos los usuarios
@api_bp.route("/users", methods=["GET"])
def list_users():
    users = User.query.order_by(User.id).all()
    return jsonify([user_to_dict(u) for u in users])


# POST /api/users  → crea un usuario
@api_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json() or {}

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "name y email son obligatorios"}), 400

    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()

    return jsonify(user_to_dict(user)), 201

# GET /api/users/<id>  → obtener usuario por id
@api_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "user not found"}), 404
    return jsonify(user_to_dict(user))


# PUT /api/users/<id>  → actualizar usuario
@api_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "user not found"}), 404

    data = request.get_json() or {}

    # Si no vienen campos, se mantienen los actuales
    name = data.get("name", user.name)
    email = data.get("email", user.email)

    user.name = name
    user.email = email

    db.session.commit()
    return jsonify(user_to_dict(user))


# DELETE /api/users/<id>  → borrar usuario
@api_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "user not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"status": "deleted", "id": user_id})

# =========================
# CRUD de Skills
# =========================

# GET /api/skills → lista todas las skills
@api_bp.route("/skills", methods=["GET"])
def list_skills():
    skills = Skill.query.order_by(Skill.id).all()
    return jsonify([skill_to_dict(s) for s in skills])


# POST /api/skills → crea una skill
@api_bp.route("/skills", methods=["POST"])
def create_skill():
    data = request.get_json() or {}

    name = data.get("name")

    if not name:
        return jsonify({"error": "name es obligatorio"}), 400

    skill = Skill(name=name)
    db.session.add(skill)
    db.session.commit()

    return jsonify(skill_to_dict(skill)), 201


# GET /api/skills/<id> → obtener skill por id
@api_bp.route("/skills/<int:skill_id>", methods=["GET"])
def get_skill(skill_id):
    skill = Skill.query.get(skill_id)
    if skill is None:
        return jsonify({"error": "skill not found"}), 404
    return jsonify(skill_to_dict(skill))


# PUT /api/skills/<id> → actualizar skill
@api_bp.route("/skills/<int:skill_id>", methods=["PUT"])
def update_skill(skill_id):
    skill = Skill.query.get(skill_id)
    if skill is None:
        return jsonify({"error": "skill not found"}), 404

    data = request.get_json() or {}

    skill.name = data.get("name", skill.name)

    db.session.commit()
    return jsonify(skill_to_dict(skill))


# DELETE /api/skills/<id> → borrar skill
@api_bp.route("/skills/<int:skill_id>", methods=["DELETE"])
def delete_skill(skill_id):
    skill = Skill.query.get(skill_id)
    if skill is None:
        return jsonify({"error": "skill not found"}), 404

    db.session.delete(skill)
    db.session.commit()
    return jsonify({"status": "deleted", "id": skill_id})

# =========================
# CRUD de JobOffers
# =========================

# GET /api/job_offers → listar ofertas
@api_bp.route("/job_offers", methods=["GET"])
def list_job_offers():
    offers = JobOffer.query.order_by(JobOffer.id).all()
    return jsonify([joboffer_to_dict(o) for o in offers])


# POST /api/job_offers → crear oferta
@api_bp.route("/job_offers", methods=["POST"])
def create_job_offer():
    data = request.get_json() or {}

    required_fields = ["title", "company"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} es obligatorio"}), 400

    offer = JobOffer(
        title=data["title"],
        company=data["company"],
        description=data.get("description"),
        location=data.get("location"),
        seniority=data.get("seniority"),
    )
    db.session.add(offer)
    db.session.commit()
    return jsonify(joboffer_to_dict(offer)), 201


# GET /api/job_offers/<id> → obtener oferta por id
@api_bp.route("/job_offers/<int:offer_id>", methods=["GET"])
def get_job_offer(offer_id):
    offer = JobOffer.query.get(offer_id)
    if offer is None:
        return jsonify({"error": "job offer not found"}), 404
    return jsonify(joboffer_to_dict(offer))


# PUT /api/job_offers/<id> → actualizar oferta
@api_bp.route("/job_offers/<int:offer_id>", methods=["PUT"])
def update_job_offer(offer_id):
    offer = JobOffer.query.get(offer_id)
    if offer is None:
        return jsonify({"error": "job offer not found"}), 404

    data = request.get_json() or {}

    offer.title = data.get("title", offer.title)
    offer.company = data.get("company", offer.company)
    offer.description = data.get("description", offer.description)
    offer.location = data.get("location", offer.location)
    offer.seniority = data.get("seniority", offer.seniority)
    offer.is_active = data.get("is_active", offer.is_active)

    db.session.commit()
    return jsonify(joboffer_to_dict(offer))


# DELETE /api/job_offers/<id> → borrar oferta
@api_bp.route("/job_offers/<int:offer_id>", methods=["DELETE"])
def delete_job_offer(offer_id):
    offer = JobOffer.query.get(offer_id)
    if offer is None:
        return jsonify({"error": "job offer not found"}), 404

    db.session.delete(offer)
    db.session.commit()
    return jsonify({"status": "deleted", "id": offer_id})

# =========================
# CRUD de UserSkills
# =========================

# GET /api/user_skills → lista todas las relaciones usuario-skill
@api_bp.route("/user_skills", methods=["GET"])
def list_user_skills():
    items = UserSkill.query.order_by(UserSkill.id).all()
    return jsonify([user_skill_to_dict(us) for us in items])


# POST /api/user_skills → asignar una skill a un usuario
@api_bp.route("/user_skills", methods=["POST"])
def create_user_skill():
    data = request.get_json() or {}

    user_id = data.get("user_id")
    skill_id = data.get("skill_id")
    level = data.get("level")

    if not user_id or not skill_id or not level:
        return jsonify({"error": "user_id, skill_id y level son obligatorios"}), 400

    us = UserSkill(user_id=user_id, skill_id=skill_id, level=level)
    db.session.add(us)
    db.session.commit()

    return jsonify(user_skill_to_dict(us)), 201


# GET /api/user_skills/<id> → ver una relación
@api_bp.route("/user_skills/<int:user_skill_id>", methods=["GET"])
def get_user_skill(user_skill_id):
    us = UserSkill.query.get(user_skill_id)
    if us is None:
        return jsonify({"error": "user_skill not found"}), 404
    return jsonify(user_skill_to_dict(us))


# PUT /api/user_skills/<id> → actualizar nivel de una skill de usuario
@api_bp.route("/user_skills/<int:user_skill_id>", methods=["PUT"])
def update_user_skill(user_skill_id):
    us = UserSkill.query.get(user_skill_id)
    if us is None:
        return jsonify({"error": "user_skill not found"}), 404

    data = request.get_json() or {}

    us.level = data.get("level", us.level)
    db.session.commit()
    return jsonify(user_skill_to_dict(us))


# DELETE /api/user_skills/<id> → borrar relación usuario-skill
@api_bp.route("/user_skills/<int:user_skill_id>", methods=["DELETE"])
def delete_user_skill(user_skill_id):
    us = UserSkill.query.get(user_skill_id)
    if us is None:
        return jsonify({"error": "user_skill not found"}), 404

    db.session.delete(us)
    db.session.commit()
    return jsonify({"status": "deleted", "id": user_skill_id})
