class Item:
    name = ""
    description = ""
    expiration = ""

    def __init__(self, sql="", json=""):
        if sql:
            self.name = sql.name
            self.description = sql.description
            self.expiration = sql.expiration
        elif json:
            self.name = json.get('name')
            self.description = json.get('description')
            self.expiration = json.get('expiration')
        else:
            raise Exception("no source data supplied")
            
    def sql_list(self):
        list = "("
        if self.name:
            list = list + "name,"
        if self.description:
            list = list + "description,"
        if self.expiration:
            list = list + "expiration,"
        list = list[0:-1] + ")"
        return list

    def sql_values(self):
        list = "("
        if self.name:
            list = list + "'" + self.name + "',"
        if self.description:
            list = list + "'" + self.description + "',"
        if self.expiration:
            list = list + "'" + self.expiration + "',"
        list = list[0:-1] + ")"
        return list