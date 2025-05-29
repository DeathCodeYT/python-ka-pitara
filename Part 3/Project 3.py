# /// Scritp
# dependecies = ['colorama']
# ///

# Typing Speed Tester

from colorama import init,Fore,Style
import random
import os
import time

init(autoreset=True)

SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language.",
    "Practice makes a man perfect.",
    "Typing fast is a valuable skill.",
    "Always keep learning new things.",
    "Simple code is often better than complex code.",
    "Debugging is twice as hard as writing the code.",
    "Errors help you learn and grow.",
    "Code every day to get better.",
    "Shortcuts can improve your productivity.",
    "Never give up on a bug.",
    "Readability counts in Python.",
    "Indentation matters in Python.",
    "Automate the boring stuff with Python.",
    "Version control is essential for developers.",
    "Be proud of what you build.",
    "Don't repeat yourself in code.",
    "Good code is self-explanatory.",
    "Think before you write your logic.",
    "Consistency leads to mastery."
]

RESULT_FILE = "typing_results.txt"

def get_random_sentence():
    return random.choice(SENTENCES)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_wpm(char_count,time_taken_secs):
    words = char_count/5 # 1 word = 5 characters ka average mana jata hai
    minutes = time_taken_secs/60
    return round(words/minutes,2)

def calculate_accuracy(original,typed):
    correct = sum(1 for o,t in zip(original,typed) if o==t)
    accuracy = (correct/len(original))*100
    return round(accuracy,2)

def run_typing_test():
    clear_screen()
    print(Fore.YELLOW+"🔤 Typing Speed Test\n"+"-"*30)

    sentence = get_random_sentence()
    print(Fore.CYAN+"Type this senctence:\n")
    print(Fore.WHITE+Style.BRIGHT+sentence)
    print("\n(Press Enter when done typing)\n")
    input("Press Enter when you are ready to start...")
    print(Fore.GREEN+"Start Typing below:\n")

    start = None
    user_input = ""
    try:
        start = time.time()
        user_input = input("> ")
        end = time.time()
    except KeyboardInterrupt:
        print("\n\n Test Aborted.")
        return

    time_taken = end-start
    char_count = len(user_input)
    wpm = calculate_wpm(char_count,time_taken)
    accuracy = calculate_accuracy(sentence,user_input)
    print("\n"+Fore.MAGENTA+"✅ Results:\n")
    print(Fore.YELLOW+f"✅ Original Sentence: {sentence}")
    print(Fore.CYAN+f"⌨️ Your Input: {user_input}")
    print(Fore.WHITE+f"⌛ Time Taken: {round(time_taken,2)}sec")
    print(Fore.GREEN+f"⚡ WPM: {wpm}")
    print(Fore.BLUE+f"🎯 Accuracy: {accuracy}%")

run_typing_test()





