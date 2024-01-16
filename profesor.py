import time
from persona import persona
from departamento import departamento
from asignatura import asignatura

class profesor(persona):
    def __init__(self, dni:str, name:str, assignature:asignatura, department:departamento, gender:str, age:int, salary:float, stdate:time):
        super().__init__(dni, name, gender, age)
        self._salary = salary
        self._stdate = stdate
        self._assignature = assignature
        self._department = department

#Getters y setters (GRACIAS FIORI, ESTO ERA SUPER NECESARIO)
        
    #GetterSetters del salario
    def get_salary(self):
        return self._salary
    
    def set_salary(self, salary):
        self._salary = salary
    
    #GetterSetters de la fecha de inicio
    def get_stdate(self):
        return self._stdate
    
    def set_stdate(self, stdate):
        self._stdate = stdate
    
    #GetterSetters de la asignatura
    def get_assignature(self):
        return self._assignature
    
    def set_assignature(self, assignature):
        self._assignature =assignature

    #GetterSetters del departamento
    def get_department(self):
        return self._department
    
    def set_department(self, department):
        self._department = department