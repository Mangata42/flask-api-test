from app import *

class Skill(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	type = db.Column(db.String(32))
	attribute = db.Column(db.String(32), index=True, unique=True)

	def __repr__(self):
		return (str("{}".format(self.attribute)))
	
	def to_dict(self):
		"""Will return a dictionnary of the skill that can be JSONified"""

		data = {
			"id": self.id,
			"type": self.type,
			"attribute": self.attribute,
		}
		return (data)

	def all_to_dict():
		"""Same as self.to_dict(), but for all the skills"""

		skills = Skill.query.all()
		data = {}
		i = 0
		for s in skills:
			data.update({"item" + str(i):s.to_dict()})
			i+=1
		return (data)

	def from_dict(self, data, edit=False):
		"""Will turn a JSON into a usable dict to add or a delete a skill entry"""
		
		if (edit == False):
			for field in data:
				if field == "attribute":
					setattr(self, "type", "String")
					setattr(self, field, data[field].lower().strip().replace(" ", ""))
		else:
			for field in data:
				if field == "attribute":
					setattr(self, field, data[field].lower().strip().replace(" ", ""))
