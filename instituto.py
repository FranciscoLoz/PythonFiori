from curso import curso
from direccion import direccion
from departamento import departamento

class instituto:
    def __init__(self, name:str, cif:str, address:direccion, courses:curso, department: departamento):
        self._name=name
        self._cif=cif
        self._address=address
        self._courses=courses
        self._department=department

#Getters y setters
        
    #GetterSetters del nombre
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name=name
    
    #GetterSetters del CIF
    def get_cif(self):
        return self._cif
    
    def set_cif(self, cif):
        self._cif=cif

    #GetterSetters de la dirección
    def get_address(self):
        return self._address
    
    def set_address(self, address):
        self._address=address
    
    #GetterSetters de los cursos disponibles
    def get_courses(self):
        return self._courses
    
    def set_courses(self, courses):
        self._courses=courses

    #GetterSetters de los departamentos
    def get_department(self):
        return self._department
    
    def set_department(self, department):
        self._department=department