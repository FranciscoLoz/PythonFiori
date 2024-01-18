import datetime
from persona import persona

class administrativo(persona):
    def __init__(self, dni:str, name:str, gender:str, age:int, salary:float, stdate:datetime):
        super().__init__(dni, name, gender, age)
        self._salary = salary
        self._stdate = stdate

#Getters y setters
        
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