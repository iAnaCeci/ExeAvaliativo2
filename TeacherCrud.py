class TeacherCrud:
    def __init__(self, db):
        self.db = db


    def create_teacher(self,name,ano_nasc,cpf):
        query = "CREATE (:Teacher {name: $name, ano_nasc:$ano_nasc, cpf: $cpf})"
        self.db.execute_query(query, {"name":name, "ano_nasc":ano_nasc, "cpf":cpf})


    def read_teacher(self,name):
        query = "MATCH (t:Teacher{name:$name}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        results = self.db.execute_query(query,{"name":name})
        return {result ["ano_nasc"]: result["cpf"] for result in results}


    def update_player(self, name,NewCpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $NewCpf"
        self.db.execute_query(query, {"name": name, "NewCpf":NewCpf})


    def delete_player(self, name):
        query = "MATCH (t:Teacher {name: $name}) DETACH DELETE t"
        self.db.execute_query(query, {"name":name})



