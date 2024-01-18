from curso import curso

class instituto:
    def __init__(self, name:str, cif:str, address:str, courses:curso):
        self._name=name
        self._cif=cif
        self._address=address
        self._courses=courses

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