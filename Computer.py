from MasterMind44Player import Mastermind44Player
import random
import os
class ComputerMode():
    """
    Computer support for single player Original MasterMind game and 4 player MM44 game.
    """
    def __init__(self,option):
        """
        Initialises the variable
        """
        self.option = option
    def randomCode(self) -> list:
        """
        Function to generate a random code.
        """
        index = 0
        codeChoice = ['R','G','Y','B','L','W']
        if self.option.upper() == 'B':
            randomCodeGenerated = []
            while index < 4:
                randomCodeGenerated.append(random.choice(codeChoice))
                index += 1
            return randomCodeGenerated
        elif self.option.upper() == 'C':
            randomCodeGenerated44 = []
            while index < 4:
                randomCodeGenerated44.append(random.choice(codeChoice))
                index += 1
            for _ in range(1):
                randomCodeGenerated44.insert(random.randrange(0,len(randomCodeGenerated44)-1),'_')
            return randomCodeGenerated44
    def displayCodes(self,code) -> list:
        """
        Displays the MM44 hidden code to the player.
        """
        playerNum = ['A','B','C','D']
        codePosition = [0,1,2,3,4]
        players = []
        for k in playerNum:
            print('Player Mastermind', k,': When you are ready for one position of the code to be\n'
                  'revealed on the screen press <enter>.')
            input()
            showCodePosition = random.choice (codePosition)
            codePosition.remove(showCodePosition)
            print('Postion: ', showCodePosition + 1,' Colour: ',code[showCodePosition])
            players.append(Mastermind44Player(k, showCodePosition + 1, code[showCodePosition]))
            input()
            os.system('cls')
        return players
    def giveFeedback(self,codeA,codeB):
        """
        Gives feedback for Original MasterMind game.
        """
        index = 0
        feedback = ''
        if codeA == '' or codeB == '':
            return feedback
        if self.option.upper() == 'A' or 'B':
            if codeB == codeA:
                return('Congratulations!! You won.')
            else:
                while index < 4:
                    if codeB[index] == codeA[index]:
                        feedback += 'B'
                    elif codeB[index] in codeA:
                        feedback += 'W'   
                    index += 1
                return feedback
    def giveFeedbackMM44(self,code1,code2):
        """
        Gives feedback for MasterMind44 game.
        """
        index = 0
        feedback = ''
        if code1 == '' or code2 == '':
            return feedback
        if code2 == code1:
            return('Congratulations!! You won.')
        else:
            while index < 5:
                if code1[index] == code2[index]:
                    feedback += 'B'
                elif code2[index] in code1:
                    feedback += 'W'   
                index += 1
            return feedback