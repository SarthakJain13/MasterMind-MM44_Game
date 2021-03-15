from CodeValidation import CodeValidator
class CodeBreaker():
    """
    Plays the role to guess the code set by the code maker
    """
    def guessCode(self):
        """
        Function used by the players to guess the codes
        """
        validCode = CodeValidator()
        guessCodeList = []
        guessCode = str(input(""))
        if validCode.codeLengthValidation(guessCode) == True:
            if validCode.codeColorValidation(guessCode) == True:
                for b in guessCode:
                    guessCodeList.append(b.upper())
                return guessCodeList
            else:
                print('Invalid choice!! Color can only be from the provided options.')
                return ''
        else:
            print('Allowed code length is 4, Please enter the code of the specified code length only.')
            return ''
    def breakCode(self):
        """
        Calling the guessCode 
        """
        print(self.guessCode())