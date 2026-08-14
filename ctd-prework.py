# This program compliments you if your zodiac sign is Gemini or Scorpio, extra compliments if you are a millennial! >_<

name = input("What is your name? ")
zsign = input("What is your zodiac sign? ").lower()
age = int(input("How old are you? "))

if zsign == "gemini" and age < 40:
    print("Congratulations " + str(name) + "! So glad to have you as part of the Gemini Club!")

elif zsign == "gemini" and age >= 40:
    print("Congratulations " + str(name) + "! So glad to have you as part of the Gemini Club of Beautiful Millennials!")

elif zsign == "scorpio":
    print("Amazing " + str(name) + "! Scorpio is almost as good as Gemini!")

else: 
    print("Interesting...")
