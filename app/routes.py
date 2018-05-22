from app import *
from app.db_models import *
from flask import request, jsonify

class SkillForm(Form):
	"""Skill website form"""

	skill = StringField("Add Skill :", validators=[DataRequired()])

@application.route("/", methods=["GET", "POST"])
def index():
	skill_form = SkillForm()
	skill_list = Skill.query.all()
	return render_template("index.html", form=skill_form, skill_list=skill_list)

@application.route("/add", methods=["GET", "POST"])
def add_skill():
	"""Add a skill from website"""

	skill_form = SkillForm()
	skill_to_add = skill_form.skill.data
	if (skill_to_add is None):
		return redirect("/")
	skill_to_add = skill_to_add.lower()
	skill_to_add = skill_to_add.strip()
	skill_to_add = skill_to_add.replace(" ","")

	if (len(skill_to_add) <= 0):
		flash("Empty field.")
	elif (Skill.query.filter_by(attribute=skill_to_add).first()):
		flash("Skill already in database.")
	else:
		db.session.add(Skill(type="String", attribute=skill_to_add))
		db.session.commit()
	return redirect("/")

@application.route("/delete", methods=["GET", "POST"])
def del_skill():
	"""Delete a skill from website"""

	skill_form = SkillForm()
	if (skill_form.skill.data is None):
		return redirect("/")
	skill_to_del = Skill.query.filter_by(attribute=request.form.get("delete")).first()
	db.session.delete(skill_to_del)
	db.session.commit()
	return redirect("/")

@application.route("/edit", methods=["GET", "POST"])
def edit_skill():
	"""Edit a skill from website"""

	skill_form = SkillForm()
	if (skill_form.skill.data is None):
		return redirect("/")
	skill_to_edit = Skill.query.filter_by(attribute=request.form.get("edit")).first()
	skill_new_attr = skill_form.skill.data
	skill_new_attr = skill_new_attr.lower()
	skill_new_attr = skill_new_attr.strip()
	skill_new_attr = skill_new_attr.replace(" ","")
	if (len(skill_new_attr) <= 0):
		flash("Empty field.")
	elif (Skill.query.filter_by(attribute=skill_new_attr).first()):
		flash("Skill already in database.")
	else:
		skill_to_edit.attribute = skill_new_attr
		db.session.commit()
	return redirect("/")

@application.route("/delete_db")
def delete_db():
	"""Delete database from website"""

	skills = Skill.query.all()
	for s in skills:
		db.session.delete(s)
	db.session.commit()
	return redirect("/")

# ---- json test ----
# Was used only to test jsonify module

@application.route("/json/<int:id>")
def json_one(id):
	skill = Skill.query.get(id)
	return jsonify(skill.to_dict())

@application.route("/json_all")
def json_all():
	return jsonify(Skill.all_to_dict())