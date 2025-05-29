# Python Quiz app

def quiz_app():
    questions = [
        "What is the keyword to define a function in python?",
        "Which data type is used to store True or False?",
        "What symbol is used to start a comment in python?",
        "Which function is used to get input from the user?",
        "What is the index of the first element in python list?"
    ]
    answers = [
        'def',
        'bool',
        '#',
        'input',
        '0'
    ]
    score = 0
    for q,a in zip(questions,answers):
        user_ans = input(f"❓{q}\n👉 Your Answer: ")
        if user_ans.lower() == a.lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct Answer: {a}\n")
    print(f"🎯 Your final score: {score}/{len(questions)}")
    
    # Bonus: Feedback
    if score == len(questions):
        print("🏆 Feedback: Excellent! You're a Python Pro!")
    elif score >= len(questions) * 0.6:
        print("👍 Feedback: Good Job! Keep Practicing.")
    else:
        print("📘 Feedback: Try Again! Practice Makes Perfect.")

    again = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
    if again == "yes":
        quiz_app()
    else:
        print("👋 Thanks for playing! Bye!")


quiz_app()

