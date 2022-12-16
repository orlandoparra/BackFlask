from main import db

class Estudiante2(db.Model):
    __tablename__ = "Estudiante"

    id = db.column(db.Integer,primary_key=True)
    cedula = db.Column(db.String())
    nombre = db.Column(db.String())
    apellido = db.Column(db.String())

    def __int__(self, cedula, nombre, apellido):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido

    def __repr__(self):
        return f" Cedula : {self.cedula} , Nombre :{self.nombre} , Apellido{self.apellido}
