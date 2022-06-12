#INTRODUCTION
import time
    
print('               Hello!! ')
time.sleep(1)

print('       Welcome To Game Arcade!!       ')               
print()
time.sleep(1.5)
print('We create the best-in-class games for our esteemed users. Happy to have you join us!!')
print()
time.sleep(1.5)
print('Umm, mind sharing some essential information?')
print('P.S. Just for leaderboard and all that stuff...:-')
print()

time.sleep(1.5)
z=input('Please tell us, Are you a part of our community(i.e. Do you have an account here)?? (If yes: Y or If no: N): ')

#CONNECTION TO MYSQL
import mysql.connector as mc
c=mc.connect(host='localhost',user='root',password='',database='gamesinfo')
if c.is_connected():
    print()
    
ct=c.cursor()
ct.execute('select * from user')
st=ct.fetchall()
count=ct.rowcount
c.close()
f='n'

if(z=='y'):
    t=input('Username: ')
    user_name=t
else:
    print('Please create your account.')
    i=input('Username: ')
    o=input('Password: ')
    e=mc.connect(host='localhost',user='root',password='',database='gamesinfo')
    if e.is_connected():
        print()
        print('Hey',i,', WELCOME!!!')
    r=e.cursor()
    r.execute("insert into user values(%s,%s,%s,%s)",(count+1,i,o,0))
    e.commit()
    e.close()
    f='m'
    user_name=i
    pass_word=o
    
k=mc.connect(host='localhost',user='root',password='',database='gamesinfo')
if k.is_connected():
    print()
    
q=k.cursor()
q.execute('select username from user')
m=q.fetchall()
k.close()


n=mc.connect(host='localhost',user='root',password='',database='gamesinfo')
if n.is_connected():
    print('Successfully connected to the server!!')

w=n.cursor()
w.execute('select passwd from user')
u=w.fetchall()
n.close()



if(z=='y'):
    for l in m:
        if t in l:
        
            pas=input('Password:')
            for lw in u:
                if pas in lw:
                    time.sleep(1.5)
                    print('Logged in')
                    f='m'
                    break
            else:
                while(f=='n'):
                    pas=input('Please enter your password again: ')
                    for lw in u:
                        if pas in lw:
                            print('Logged in')
                            f='m'
    pass_word=pas

#================================================GAMES========================================================================
#HANGMAN
def Hangman():
    import random
    import time
    HANGMANPICS = ['''

      +---+
      |   |
          |
          |
          |
          |
    =========''', '''

      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''

      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''

      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''

      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''

      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''

      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    words = 'ant bat bull bear camel cat cobra cow crow deer dog fox goat lion lizard monkey mouse panda parrot python rabbit rat shark sheep snake spider tiger turtle whale wolf zebra'.split()

    win_pts=0
    lose_pts=0

    def getRandomWord(wordList):
        # This function returns a random string from the passed list of strings.
        wordIndex = random.randint(0, len(wordList) - 1)
        return wordList[wordIndex]

    def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
        print(HANGMANPICS[len(missedLetters)])
        print()

        print('Missed letters:', end=' ')
        for letter in missedLetters:
            print(letter, end=' ')
        print()

        blanks = '_' * len(secretWord)

        for i in range(len(secretWord)): # replace blanks with correctly guessed letters
            if secretWord[i] in correctLetters:
                blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

        for letter in blanks: # show the secret word with spaces in between each letter
            print(letter, end=' ')
        print()

    def getGuess(alreadyGuessed):
        # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
        while True:
            print('Guess a letter.')
            guess = input()
            guess = guess.lower()
            if len(guess) != 1:
                print('Please enter a single letter.')
            elif guess in alreadyGuessed:
                print('You have already guessed that letter. Choose again.')
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please enter a LETTER.')
            else:
                return guess

    def playAgain():
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')


    print('H A N G M A N')
    missedLetters = ''
    correctLetters = ''
    secretWord = getRandomWord(words)
    gameIsDone = False

    while True:
        displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

        # Let the player type in a letter.
        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters = correctLetters + guess

            # Check if the player has won
            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! The secret word is "' + secretWord + '"! You have won!')
                print('Congratulations!! You have won the game. you have been awarded 10 points.')
                win_pts+=10
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess

            # Check if player has guessed too many times and lost
            if len(missedLetters) == len(HANGMANPICS) - 1:
                displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
                print("You have lost the game. You have been awarded -5 points!")
                lose_pts-=5
                gameIsDone = True

        # Ask the player if they want to play again (but only if the game is done).
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break

    z=input("Do you want to know your win and loss points? (y/n)")
    if z=="y":
        print("Win points:",win_pts)
        print("Loss points:",lose_pts)
        print("Total points:",win_pts+lose_pts)
        return win_pts+lose_pts
        time.sleep(2)
    else:
        return win_pts+lose_pts
        time.sleep(2)
        exit
   
#=============================================================================================================================
#GUESS THE NUMBER
def Guess_Game():
    
    import random
    import time

    guessesTaken = 0

    win_pts=0
    lose_pts=0

    number = random.randint(0, 20)
    print('Well, I am thinking of a number between 0 and 20.')

    while guessesTaken < 10:
        print('Take a guess.') 
        guess = input()
        guess = int(guess)

        guessesTaken = guessesTaken + 1

        if guess < number:
            print('Your guess is low.') 

        elif guess > number:
            print('Your guess is high.')

        elif guess == number:
            break
        
    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job! You guessed my number in ' + guessesTaken + ' guesses!')
        print("You have been awarded 10 points for winning the game.")
        win_pts+=10

    if guess != number:
        number = str(number)
        print('Nope. The number I was thinking of was ' + number)
        print("You have lost the game. You have been awarded -5 points!")
        lose_pts-=5

    z=input("Do you want to know your win and loss points? (y/n)")
    if z=="y":
        print("Win points:",win_pts)
        print("Loss points:",lose_pts)
        print("Total points:",win_pts+lose_pts)
        return win_pts+lose_pts
    else:
         return win_pts+lose_pts
         time.sleep(2)
         exit

# =============================================================================
def Blackjack():

        from random import randrange
        
        ts=0
        
        def printIntro():
                    print("Blackjack (twenty-one) is a casino game played with cards.")
                    print("The goal of game is to draw cards that total as close to 21 points, as possible")
                    print("without going over( whose hand > 21 will bust). All face cards count as 10 points,")
                    print("aces count as 1 or 11, and all other cards count their numeric value.")
                    print("\nFirstly, your turn:")


        def player():
                    hand = []
                    ans = "hit"
                    hand.append(card())
                    # Ask user whether Hit or Stand?
                    # Condition True, if user wants to Hit.
                    while ans[0] == "h" or ans[0] == "H":
                        hand.append(card())
                        hand = eval_ace(hand)
                        print("Your hand: {0} total = {1}".format(hand, sum(hand)))
                        if bust(hand):
                            break
                        if blackjack(hand):
                            break
                        ans = input("Do you want to Hit or Stand (H or S)? ")
                    return hand


        def card():
                    # get arbitrary card from 2 to 11.
                    shuffle_card = randrange(2, 11 + 1)
                    return shuffle_card


        def eval_ace(hand):
                    # Determine Ace = 1 or 11, relying on total hand. 
                    total = sum(hand)
                    for ace in hand:
                        if ace == 11 and total > 21:
                            # at position where Ace == 11, replace by Ace == 1.
                            position_ace = hand.index(11)
                            hand[position_ace] = 1
                    return hand


        def bust(hand):
                    # Condition True: if the hand of player (or dealer) > 21.
                    total = sum(hand)
                    if total > 21:
                        return True


        def blackjack(hand):
                    # Condition True: if the hand of player (or dealer) == 21.
                    total = sum(hand)
                    if total == 21:
                        return True


        def dealer():
                    hand = []
                    hand.append(card())
                    while sum(hand) < 18:
                        hand.append(card())
                        hand = eval_ace(hand)
                    return hand


        def compare_between(player, dealer):    
                    total_player = sum(player)
                    total_dealer = sum(dealer)
                    player_bust = bust(player)
                    dealer_bust = bust(dealer)
                    player_blackjack = blackjack(player)
                    dealer_blackjack = blackjack(dealer)
                    player_win = 0
                    dealer_win = 0
                    # when player (dealer) bust.
                    if player_bust:
                        if not dealer_blackjack and total_dealer < 21:
                            dealer_win += 1
                    if dealer_bust:
                        if not player_blackjack and total_player < 21:
                            player_win += 1
                    if player_bust and dealer_bust:
                        if total_player > total_dealer:
                            player_win += 1
                        elif total_dealer > total_player:
                            dealer_win += 1
                        else:
                            player_win == dealer_win
                    # when player (dealer) get blackjack.
                    if player_blackjack:
                        player_win += 1
                    if dealer_blackjack:
                        dealer_win += 1
                    if player_blackjack and dealer_blackjack:
                        player_win == dealer_win
                    # when total hand of player (dealer) < 21.
                    if total_player < 21 and total_dealer < 21:
                        if total_player > total_dealer:
                            player_win += 1
                        elif total_dealer > total_player:
                            dealer_win += 1
                        else:
                            player_win == dealer_win
                    return player_win, dealer_win

                
                
        def printResult(player_hand, dealer_hand, player_win, dealer_win):
                    print("\nWe have the result: ")
                    print("Player has: {0} total = {1}".format(player_hand, sum(player_hand)))    
                    print("Dealer has: {0} total = {1}".format(dealer_hand, sum(dealer_hand)))
                    print("player: {} | dealer: {}".format(player_win, dealer_win))
                    if player_win==1:
                        return ts+10
                    elif dealer_win==1:
                        return ts-5
                    
        def main():
                    printIntro()
                    player_hand = player()
                    dealer_hand = dealer()
                    player_win, dealer_win = compare_between(player_hand, dealer_hand)
                    d=printResult(player_hand, dealer_hand, player_win, dealer_win)
                    return d
                
        if __name__ == "__main__": 
                    c=main()
                    return c
                
                    
#=============================================================================================================================
#CHOOSING A GAME
print()
print()

cont="y"

yui=sc_g=sc_b=0

while cont=="y":
    print("You can play the following from the Game Arcade Premium Collection:")
    print("1.Hangman\n2.Guess The Number\n3.Blackjack Casino Game")

    choice=int(input("Which game would you like to play from the ones mentioned above? "))
    
    if choice==1:
        yui=Hangman()
    elif choice==2:
        sc_g=Guess_Game()
    elif choice==3:
       sc_b=Blackjack()
    else:
        print("Invalid Choice. Please select a valid response.")
        continue
    cont=input("Do you wish to continue playing the games? (y/n)")
    
    print("Hangman Score:",yui," Guess Game Score:",sc_g," Blackjack Score:",sc_b)
    
    sph=yui+sc_g+sc_b
    print("Total score=",sph)        
    if cont=="n":
        print("Thank you for playing ! We hope that you enjoyed playing our games!!") 
        time.sleep(0.75)
        print("See you soon!!")
        time.sleep(0.75)
        print("Felicia!!!!!")
        time.sleep(1.25)
        exit
 
kqqb=mc.connect(host='localhost',user='root',password='',database='gamesinfo')
if kqqb.is_connected():
    print()
        
    qqcb=kqqb.cursor()    
    if(z=='y'):
        amk=t
    else:
        amk=i            
    qqcb.execute('update user set total=total+%s where username=%s',(sph,amk))
    kqqb.commit()
    kqqb.close()
kqqc=mc.connect(host='localhost',user='root',password='',database='gamesinfo')
if kqqc.is_connected():
    print()
    
    qqcc=kqqc.cursor()    
    qqcc.execute('select username,total from user order by total desc')
    zxy=qqcc.fetchall()
    kqqb.close()
       
    print("-----------------LEADERBOARD------------------")
    print(" Username           |             Total Score ")
    for i in zxy:
        for j in i:
            print(j," "*(35-len(str(j))),end=" ")
        print()
           
    print()
     