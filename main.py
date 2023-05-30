from database import Database
from TeacherCrud import TeacherCrud

db = Database("bolt://44.200.241.42:7687", user="neo4j", password="advertisements-operand-second")

teacher_db = TeacherCrud(db)
teacher_db.create_teacher("Chris Lima","1956","189.052.396-66")

teacher_db.read_teacher("Chris Lima")

teacher_db.update_player("Chris Lima","162.052.777-77")

