from app import *
from app.db_models import *

@application.shell_context_processor
def make_shell_context():
	return ({"db":db, "Skill":Skill})

if __name__ == "__main__":
	application.run(host="0.0.0.0")