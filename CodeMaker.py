import getpass
from CodeValidation import CodeValidator
class CodeMaker():
    """
    Plays the role to set the initial code
    """
    def setCode(self) -> list:
        """
        Function used by the player to set the code.
        """
        validCode = CodeValidator()
        setCodeList = []
        Code1 = getpass.getpass(prompt='Enter the code now: \n').upper()
        if validCode.codeLengthValidation(Code1) == True:
            if validCode.codeColorValidation(Code1) == True:
                Code2 = getpass.getpass(prompt='Enter the same code again: \n').upper()
                if Code1 == Code2:
                    for a in Code1:
                        setCodeList.append(a.upper())
                    print('Code has been stored.')
                    return setCodeList
                else:
                    print("Both the codes doesn't match.")
                    return None
            else:
                print('Invalid choice!! Color can only be from the provided options.')
                return None
        else:
            print('Allowed code length is 4, Please enter the code of the specified code length only ')
            return None
    def codeSet(self):
        """
        Calling the setCode function.
        """
        self.setCode()