class departamento:
    def __init__(self, department_id:int, name:str):
        self._department_id=department_id
        self._name=name

#Getters y Setters
    
    #GetterSetters del ID del departamento
    def get_department_id(self):
        return self._department_id
    
    def set_department_id(self, department_id):
        self._department_id = department_id

    #GetterSetters del nombre
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name=name