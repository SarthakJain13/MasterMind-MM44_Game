class CodeValidator():
    """
    For validation of the codes
    """
    def codeLengthValidation(self,code) -> bool:
        """
        Checks the validity of code length.
        """
        if len(code) == 4: 
            return True
        return False
    def codeColorValidation(self,code) -> bool:
        """
        Checks the validity of code colour.
        """
        colorChoice = ['R','G','Y','B','L','W']
        for k in code:
            if k.upper() not in colorChoice:
                return False
        return True      
    def MM44codeLengthValidator(self,code) -> bool:
        """
        Checks the validity of MM44 code length.
        """
        if len(code) == 5:
            return True
        return False
    def MM44codeColorValidator(self,code) -> bool:
        """
        Checks the validity of MM44 code colour.
        """
        MM44codeChoice1 = ['R','G','B','Y','W','L','_']
        for p in code:
            if p.upper() not in MM44codeChoice1:
                return False
        return True