print("Hello, how are you?")
user_mood = input()
print(f"Great, that you are {user_mood}! What is your name?")
user_name = input()
print(f"Hello, {user_name}! How old are you?")
user_age = int(input())
birth_year_guess = 2024 - user_age
print(f"I see, you were born in year {birth_year_guess}? Let me know if it is True or False.")
is_correct = input().lower() == 'true'
if is_correct:
    print(f"Great, then {birth_year_guess} is your birth year!")
else:
    print("Please double-check your information.")
