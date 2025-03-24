import getpass as gp
import random
import pyttsx3

# Initialize text-to-speech engine
spech = pyttsx3.init()
spech.setProperty("rate", 130)

print("Welcome to the guessing game!")
print("Loading.....")
spech.say("Welcome to the **Guessing Game!** In this fun and interactive challenge, two players participate—one as the **Typer** and the other as the **Guesser**. The Typer secretly enters a word, which is then scrambled to make guessing more exciting. The Guesser must carefully analyze the jumbled letters and try to figure out the original word. With each correct guess, the game becomes more thrilling! Are you ready to test your word skills and have some fun? Let’s begin!")
spech.runAndWait()
print("One person types a word, and the other guesses.")

# Taking names of the participants
spech.say("Enter the typer's name")
spech.runAndWait()
wrName = input(":: Enter the typer's name: ").strip()

spech.say("Enter the guesser's name")
spech.runAndWait()
gsName = input(":: Enter the guesser's name: ").strip()

while True:
    spech.say(f"{wrName}, if you are the typer, say yes. Otherwise, say no.")
    spech.runAndWait()
    whoAreYou = input(f"If you are {wrName}, say 'yes'. Otherwise, say 'no': ").lower().strip()

    if whoAreYou == "yes":
        while True:
            # Taking input secretly
            spech.say(f"{wrName}, enter a word for {gsName} to guess.")
            spech.runAndWait()
            word = gp.getpass("Enter the word (hidden input): ").lower().strip()

            # Shuffle the word
            li = list(word)
            random.shuffle(li)
            scrambled_word = "".join(li)

            print(f"Scrambled word: {scrambled_word}")

            # Guessing part
            spech.say(f"{gsName}, enter your guess.")
            spech.runAndWait()
            ansgss = input("Enter your guess: ").lower().strip()

            if ansgss == word:
                spech.say(f"Congratulations! {gsName} !! You nailed it!")
                spech.runAndWait()
                print(f"Congratulations! {gsName} 🎉 You guessed it right!")
                break
            else:
                spech.say("Oops, wrong guess. Try again!")
                spech.runAndWait()
                print("Oops! Wrong guess. Try again!")

        # Ask to continue or exit
        spech.say("Do you want to continue playing?")
        spech.runAndWait()
        continuOrNO = input("Do you want to continue? (Yes/No): ").lower().strip()

        if continuOrNO != "yes":
            print("Thanks for playing! Goodbye. 👋")
            spech.say(f"Thank you for playing!!,{wrName} and {gsName} have the grate day.....")
            spech.runAndWait()
            break
    else:
        print(f"Only {wrName} should start the game.")