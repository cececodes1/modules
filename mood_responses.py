'''
Task 1: Your Mood Today - Problem Statement: Create a Python program using a custom module that asks the user how they are feeling today and responds with a custom message based on the mood entered. - Code Example:

    # mood_responses.py
    def mood_response(mood):
        # Implement your response logic here

    # main.py
    import mood_responses
    mood = input("How are you feeling today? ")
    print(mood_responses.mood_response(mood))
'''

def mood_response(mood):
    mood = mood.lower()
    if mood == "happy":
        print("That's awesome!")
    elif mood == "sad":
        print("Don't worry, things will get better!")
    elif mood == "angry":
        print("Take a deep breath and calm down!")
    elif mood == "excited":
        print("I can tell you're pumped up!")
    else:
        print("I'm not sure how you're feeling, but I'm here to listen!")