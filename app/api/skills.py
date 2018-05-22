from app.api import bp
from flask import jsonify, request
from app import db
from app.db_models import Skill
from app.api.errors import *

@bp.route("/skill/<int:id>", methods=["GET"])
def api_get_one_skill(id):
	"""Return one skill targeted by ID"""

	return (jsonify(Skill.query.get_or_404(id).to_dict()))

@bp.route("/skills", methods=["GET"])
def api_get_all_skills():
	"""Return all skills in the database"""

	return (jsonify(Skill.all_to_dict()))

@bp.route("/skills", methods=["POST"])
def api_create_skill():
	"""Create a skill in database with attribute entry"""

	data = request.get_json() or {}
	if "attribute" not in data:
		return (bad_request("POST request should be as follows: 'attribute={skill}'"))
	skill = Skill()
	if (Skill.query.filter_by(attribute=data["attribute"].lower().strip()).first()):
		return (bad_request("Entry already in database, use PUT request to modify it."))
	if (len(data["attribute"].lower().strip()) <= 0):
		return (bad_request("'attribute' field is empty."))
	skill.from_dict(data)
	db.session.add(skill)
	db.session.commit()
	return (jsonify(skill.to_dict()))

@bp.route("/skill/<int:id>", methods=["PUT"])
def api_edit_skill(id):
	"""Edit skill in database targeted by ID"""

	data = request.get_json() or {}
	if "attribute" not in data:
		return (bad_request("PUT request should be as follows: [url]/skill/{id} 'attribute={skill}'"))
	if (len(data["attribute"].lower().strip()) <= 0):
		return (bad_request("'attribute' field is empty."))
	skill = Skill.query.get_or_404(id)
	skill.from_dict(data, edit=True)
	db.session.commit()
	return (jsonify(skill.to_dict()))

@bp.route("/skill/<int:id>", methods=["DELETE"])
def api_del_skill(id):
	"""Delete skill in database targeted by ID"""

	db.session.delete(Skill.query.get_or_404(id))
	db.session.commit()
	return("DELETED SUCCESSFULLY")

@bp.route("/skills", methods=["DELETE"])
def api_del_all_skills():
	"""Delete all database"""
	
	skills = Skill.query.all()
	for s in skills:
		db.session.delete(s)
	db.session.commit()
	return ("ALL DB DELETED SUCCESSFULLY")