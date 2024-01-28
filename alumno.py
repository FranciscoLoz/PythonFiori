from curso import curso
from asignatura import asignatura
from persona import persona

class alumno(persona):
    def __init__(self, dni:str, name:str, gender:str, age:int, course:curso, assignature:asignatura, email:str):
        super().__init__(dni, name, gender, age)
        self._course=course
        self._assignature=assignature
        self._email=email

#Getters y Setters
    
    #GetterSetters del curso
    def get_course(self):
        return self._course
    
    def set_course(self, course):
        self._course=course
    
    #GetterSetters de la asignatura
    def get_assignature(self):
        return self._assignature
    
    def set_assignature(self, assignature):
        self._assignature=assignature
    
    #GetterSetters del Email
    def get_email(self):
        return self._email
    
    def set_email(self, email):
        self._email=email