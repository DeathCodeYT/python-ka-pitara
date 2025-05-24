# Marks to Grade Converter with Motivation

print("📚 Welcome to the Grade Converter!")

marks = int(input("🎓 Enter your marks(0,100):"))

if marks <0 or marks > 100:
    print("❌ Invalid Marks!")
else:
    if marks >= 90:
        grade = 'A'
        message = "🌟 Excellent work! Keep it up!"
    elif marks >= 80:
        grade = 'B'
        message = "👍 Good job! You are doing great!"
    elif marks >= 70:
        grade = 'C'
        message = "🙂 Nice! A little more effort will take you far."
    elif marks >= 60:
        grade = 'D'
        message = "📘 Keep Pushing! You can improve!"
    else:
        grade = 'F'
        message = "💪 Don't Give Up. Learn from mistakes and bounce back stronger!"
    print(f"📊 Your Grade: {grade}")
    print(f"💬 Motivation: {message}")