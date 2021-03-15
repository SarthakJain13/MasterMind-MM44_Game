from CodeBreaker import CodeBreaker
from CodeValidation import CodeValidator
from Computer import ComputerMode
class TurnTracker():
    """
    To keep the track of number of attempts attempted by the player to crack the code.
    """
    def __init__(self,option):
        """
        Initialises the variable
        """
        self.option = option 
    def turnTrack(self,Scode) -> int:
        """
        Keeps the track of the turns according to the game selected.
        """
        round = 1
        victory = False
        if self.option.upper() == 'A' and not victory or self.option.upper() == 'B' and not victory:
            while round <= 12:
                if round == 12:
                    print('Maximum limit crossed. Actual code is',Scode)
                    return
                else:
                    round += 1
                    print()
                    print('Attempt #',round)
                   
                    CB = CodeBreaker()
                    Gcode = CB.guessCode()
                    while Gcode == '':
                        Gcode = CB.guessCode()
                    
                    com = ComputerMode('A')
                    codeF = com.giveFeedback(Scode, Gcode)
                    vic = 'Congratulations!! You won.'
                    if codeF == vic :
                        print('Congratulations!! You won in', round ,'turns.')
                        return
                    else:
                        print(codeF)  