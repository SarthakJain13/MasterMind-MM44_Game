from CodeMaker import CodeMaker
from CodeBreaker import CodeBreaker
from TurnTracker import TurnTracker
from Computer import ComputerMode
from CodeValidation import CodeValidator
from MasterMind44Player import Mastermind44Player
class Mastermind():
    """
    Displaying the basic banner and getting user inputs related to specific entities.
    """ 
    def __init__(self,menuChoice,gameChoices,nameList):
        """
        Initialises the variable.
        """
        self.menuChoice = menuChoice
        self.gameChoices = gameChoices
        self.nameList = nameList
    def displayInformation(self, displayCopyright) -> str:
        """
        Displays a welcome message to the screen including necessary information.
        """
        if displayCopyright:
            print('')
            print('')
            print('Welcome to Mastermind!\n' 
                  'Developed by Sarthak Jain.\n'
                  'COMP 1046 Object-Oriented Programming\n\n')
        while(True):
            print('Select which game you want to play:\n'
            '    (A) Original Mastermind for 2 Players\n'
            '    (B) Original Mastermind for 1 Player\n'
            '    (C) Mastermind44 for 4 Players\n'
            '*Enter A, B, or C to continue*')
            self.menuChoice = str(input(""))
            if self.menuChoiceValidation(self.menuChoice) == True:
                return self.menuChoice
            else:
                print("Invalid Choice!! Please select valid choice from the given options\n")
    def gameChoice(self) -> str:
        """ Once the user has selected a game this particular class asks the user whether to\n """
        """ actually play it or rather quit """
        while(1):
            print("What would you like to do?\n"
                  "(P)lay the game\n"
                  "(Q)uit")
            self.gameChoices = str(input(""))
            if self.gameChoiceVaidation(self.gameChoices) == True:
                return self.gameChoices
            else:
                print("\nInvalid Choice!! Please select valid choice from the given options\n")
    def menuChoiceValidation(self,choice) -> bool:
        """
        Validate the game option.
        """
        if choice.lower() == "a" or choice.lower() == "b" or choice.lower() == "c":
            return True
        return False
    def gameChoiceVaidation(self,choice) -> bool:
        """
        Validate user choice of whether to play the game or not.
        """
        if choice.lower() == "p" or choice.lower() == "q":
            return True
        return False
    def getPlayerName(self,choice) -> list:
        """
        On the basis of what game user wants to play this class ask the user/s' input for their name.
        """
        self.nameList = list()
        if choice.lower() == "a" or choice.lower() == "b" or choice.lower() == "c":
            self.nameList.append(input("Player 1: What is your name? \n"))
            print()
        if choice.lower() == "a" or choice.lower() == "c":
            self.nameList.append(input('Player 2: What is your name? \n'))
            print()
        if choice.lower() == "c":
            self.nameList.append(input('Player 3: What is your name? \n')) 
            print()
            self.nameList.append(input('Player 4: What is your name? \n'))
            print()
        return self.nameList

    def play(self, displayCopyright):
        """
        It is to initiate the working of the game.
        """
        self.displayInformation(displayCopyright)
        print()
        GC = self.gameChoice()
        if GC.upper() == 'P':
            print()
            names = self.getPlayerName(self.menuChoice)
            if self.menuChoice.upper() == 'A':
                print('Welcome', names[0],'. You need to create a code that consists of four pegs.\n'
                    'each peg can be of the colour (R)ed, B(L)ue, (G)reen, (Y)ellow, (W)hite,\n'
                    'or (B)lack. Specify the code by specifying four characters where each\n'
                    'character indicates a colour as above. For example, WWRG represents the\n'
                    'code White-White-Red-Green. You need to enter the code twice. No character\n'
                    'is shown on the screen so', names[1],'cannot see it.\n')
                setC = CodeMaker()
                a = None
                while a == None:
                    a = setC.setCode()
                print()
                print('Welcome', names[1],'.','You can now start to play by guessing the code.\n'
                    'Enter a guess by providing four characters and press Enter.\n\n'
                    'Attempt #1:')
                CB = CodeBreaker()
                b = CB.guessCode()
                while b == '':
                    b = CB.guessCode()
                if a == b:
                    print('Congratulations!! You won.')
                    againPlay = input('Would you like to play again, Y/N? ')
                    if againPlay.upper() == 'Y':
                        self.play(False)
                    elif againPlay.upper() == 'N':
                        print('Goodbye!!')
                    else:
                        againPlay = input('Would you like to play again, Y/N? ')
                else:
                    self.PlayAgainA(a, b)
            
            elif self.menuChoice.upper() == 'B':
                print("\nWelcome",names[0],". Computer will generate a random code that will not be displayed to you.\n"
                    "You are supposed to guess the code in not more than 12 turns\n")
                setc = ComputerMode(self.menuChoice)
                SetCode = setc.randomCode()
                print()
                print('Attempt #1')
                CB = CodeBreaker()
                BreakCode = CB.guessCode()
                while BreakCode == '':
                    BreakCode = CB.guessCode()
                if SetCode == BreakCode:
                    print('Congratulations!! You won.')
                    againPlay = input('Would you like to play again, Y/N? ')
                    if againPlay.upper() == 'Y':
                        self.play(False)
                    elif againPlay.upper() == 'N':
                        print('Goodbye!!')
                    else:
                        againPlay = input('Would you like to play again, Y/N? ')
                else:
                    self.PlayAgainB(SetCode,BreakCode)

            elif self.menuChoice.upper() == 'C':
                print('Welcome to Masermind44! The computer will create the secret code and reveal\n'
                    'four of the five positions one-by-one individually to each player. During\n'
                    'revealing each position only the requested player should look at the screen.\n'
                    '(R)ed, b(L)ue, (G)reen, (Y)ellow, (W)hite, or (B)lack\n')
                setc = ComputerMode(self.menuChoice)
                randomCode = setc.randomCode()
                comp = ComputerMode(self.menuChoice)
                players = comp.displayCodes(randomCode)
                print()
                for player in players:
                    print ('Player Name: ', player.playerName, ' | Position: ', player.position, ' | Color: ', player.color)
                    print ()
                # print(randomCode)
                print()
                print('Each player can now start to guess the code.\n')
                print()
                attempt = 0 
                while attempt < 5:
                    attempt = attempt + 1
                    for player in players:
                        isCodeValid = False
                        while isCodeValid == False:
                            print('Mastermind ', player.playerName, 'Attempt #', attempt , ': Enter five colours using (R)ed, b(L)ue,\n'
                            '(G)reen,(Y)ellow, (W)hite, or (B)lack:\n')
                            attemptValue = input()
                            codeValid = CodeValidator()
                            isCodeValid = codeValid.MM44codeLengthValidator(attemptValue)
                            if isCodeValid:
                                isCodeValid = codeValid.MM44codeColorValidator(attemptValue)
                                if isCodeValid:
                                    attemptValueList = []
                                    for k in attemptValue:
                                        attemptValueList.append(k.upper())
                                    # print(attemptValueList)
                                    if randomCode == attemptValueList:
                                        print('Congratulations MasterMind',player.playerName,', You Won in', attempt,'turns')
                                        return
                                    else:
                                        feed = comp.giveFeedbackMM44(randomCode,attemptValueList)
                                        print(feed)
                                        print()
                                    player.attempts.append(attemptValue)                                   
                                else:
                                    print('Invalid color')
                            else:
                                print('Invalid length')
        else:
            print('GoodBye!!')

    def PlayAgainA(self,a,b):
        """
        Review the 1st attempt and progress the game accordingly for MasterMind with 2 Players.
        """
        com = ComputerMode(self.menuChoice)
        c = com.giveFeedback(a, b)
        if c != '':
            print(c)
        t = TurnTracker(self.menuChoice)
        t.turnTrack(a)
        againPlay = input('Would you like to play again, Y/N? ')
        if againPlay.upper() == 'Y':
            self.play(False)
        elif againPlay.upper() == 'N':
            print('Goodbye!!')
        else:
            againPlay = input('Would you like to play again, Y/N? ')    

    def PlayAgainB(self,SetCode,BreakCode):
        """
        Review the 1st attempt and progress the game accordingly for MasterMind with 1 Player.
        """
        com = ComputerMode(self.menuChoice)
        ReCode = com.giveFeedback(SetCode,BreakCode)
        if ReCode != '':
            print(ReCode)
        t = TurnTracker(self.menuChoice)
        t.turnTrack(SetCode)
        againPlay = input('Would you like to play again, Y/N? ')
        if againPlay.upper() == 'Y':
            self.play(False)
        elif againPlay.upper() == 'N':
            print('Goodbye!!')
        else:
            againPlay = input('Would you like to play again, Y/N? ')
