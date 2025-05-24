# Number Guessing Game with Rating

import random

print("🎯 Welcome to the Number Guessing Game!")
print("👉 I have Selected a number b/w 1 and 100.")
print("🤖 Try to Guess it\n")

# Step 1: Generate random number between 1 and 100
secret_number  = random.randint(1,100)

# Step 2: Initialize attempt counter
attempts = 0

while True:
    guess = int(input("🎲 Enter your Guess:"))
    attempts += 1

    if guess < 1 and guess > 100:
        print("⚠️ Please Guess a number b/w 1 and 100.")
        continue
    if guess < secret_number:
        print("📉 Too Low! Try a higher number.")
    elif guess > secret_number:
        print("📈 Too High! Try a lower number")
    else:
        print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts")
        # Step 5: Bouns Rating System
        if attempts <= 5:
            rating = "🧠 Genius"
        elif attempts <=10:
            rating = "🙂 Average"
        else:
            rating = "😅 Try Again"
        print(f"🏆 Your Rating: {rating}\n")
        break



