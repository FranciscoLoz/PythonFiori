class curso:
    def __init__(self, type:str, desc:str, code:int):
        self._type=type
        self._desc=desc
        self._code=code

#Getters y setters
        
    #GetterSetters del tipo
    def get_type(self):
        return self._type
    
    def set_type(self, type):
        self._type = type

    #GetterSetters de la descripción
    def get_desc(self):
        return self._desc
    
    def set_desc(self, desc):
        self._desc = desc

    #GetterSetters del código
    def get_code(self):
        return self._code
    
    def set_code(self, code):
        self._code = code