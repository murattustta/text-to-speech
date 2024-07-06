from gtts import gTTS
from playsound import playsound
import os


voices = [
    ('tr', 'com', 'Hazal'),  # Turkish
    ('en', 'co.uk', 'Emily'),  # English (UK)
    ('en', 'co.in', 'Meera'),  # English (India)
    ('en', 'us', 'Kate'),  # English (US)
    ('es', 'es', 'Carmen'),  # Spanish (Spain)
    ('fr', 'fr', 'Eva'),  # French
    ('de', 'de', 'Sandra'),  # German
    ('it', 'it', 'Giancarlo'),  # Italian
    ('pt', 'pt', 'Cecília'),  # Portuguese
    ('nl', 'nl', 'Thekla')  # Dutch
]
def display_menu():
    print("Available Voice Options:")
    for i, (_, _, name) in enumerate(voices):
        print(f"{i + 1}. {name}")
    print()
def get_user_choice():
    while True:
        try:
            choice = int(input("Select an option number: "))
            if 1 <= choice <= len(voices):
                return choice - 1
            else:
                print(f"Please enter a number between 1 and {len(voices)}.")
        except ValueError:
            print("Please enter a valid number.")
def main():
    while True:
        # Get text input from the user
        text = input("What would you like the robot to say? (Type 'quit', 'exit', 'bye' to exit)\n")
        if text.lower() in ['quit', 'exit', 'bye']:
            print("Exiting...")
            break


        display_menu()


        choice = get_user_choice()


        lang, tld, name = voices[choice]
        tts = gTTS(text=text, lang=lang, tld=tld)
        filename = f"{name}.mp3"
        tts.save(filename)
        print(f"{filename} has been created and is playing.")

        playsound(filename)
        os.remove(filename)

if __name__ == "__main__":
    main()