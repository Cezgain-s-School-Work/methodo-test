import datetime
import sys

translations = {
    "fr": {
        "greeting_morning": "Bonjour",
        "greeting_afternoon": "Bon après-midi",
        "greeting_evening": "Bonsoir",
        "farewell_morning": "Au revoir, passez une bonne matinée",
        "farewell_afternoon": "Au revoir, passez une bonne après-midi",
        "farewell_evening": "Au revoir, passez une bonne soirée",
        "prompt": "Écrivez un truc ici : ",
        "palindrome": "Bien dit !",
    },
    "en": {
        "greeting_morning": "Good morning",
        "greeting_afternoon": "Good afternoon",
        "greeting_evening": "Good evening",
        "farewell_morning": "Goodbye, have a nice morning",
        "farewell_afternoon": "Goodbye, have a nice afternoon",
        "farewell_evening": "Goodbye, have a nice evening",
        "prompt": "Type something here: ",
        "palindrome": "Well said!",
    },
}


def greeting(lang):
    hour = datetime.datetime.now().hour
    if hour < 12:
        print(translations[lang]["greeting_morning"])
    elif hour < 18:
        print(translations[lang]["greeting_afternoon"])
    else:
        print(translations[lang]["greeting_evening"])


def farewell(lang):
    hour = datetime.datetime.now().hour
    if hour < 12:
        print(translations[lang]["farewell_morning"])
    elif hour < 18:
        print(translations[lang]["farewell_afternoon"])
    else:
        print(translations[lang]["farewell_evening"])


def is_palindrome(s):
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def main():
    lang = "fr"
    if len(sys.argv) > 1 and sys.argv[1] in translations:
        lang = sys.argv[1]
    else:
        print("Vous pouvez choisir votre langue en ajoutant le paramètre : fr ou en")

    greeting(lang)
    try:
        while True:
            user_input = input(translations[lang]["prompt"])
            if is_palindrome(user_input):
                print(translations[lang]["palindrome"])
            else:
                print(user_input)
    except (KeyboardInterrupt, EOFError):
        print()
        farewell(lang)


if __name__ == "__main__":
    main()
