from alumno import alumno
from asignatura import asignatura
from curso import curso

class matricula:
    def __init__(self, alumn:alumno, assignature:asignatura, course:curso):
        self._alumn=alumn
        self._assignature=assignature
        self._course=course

#Getters y Setters
    
    #GetterSetters del alumnado
    def get_alumn(self):
        return self._alumn
    
    def set_alumn(self, alumn):
        self._alumn=alumn

    #GetterSetters de la asignatura
    def get_assignature(self):
        return self._assignature
    
    def set_assignature(self, assignature):
        self._assignature=assignature
    
    #GetterSetters del curso
    def get_course(self):
        return self._course
    
    def set_course(self, course):
        self._course=course