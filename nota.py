from alumno import alumno
from asignatura import asignatura

class nota:
    def __init__(self, alumn:alumno, assignature:asignatura, califications:str):
        self._alumn=alumn
        self._assignature=assignature
        self._califications=califications

#Getters Y Setters
        
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

    #GetterSetters de las notas
    def get_califications(self):
        return self._califications
    
    def set_califications(self, califications):
        self._califications=califications