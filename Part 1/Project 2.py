# 2. Even Odd Counter in a Range

print("🔢 Even Odd Counter")

# Step 1: User input for range
start = int(input("Enter start of range:"))
end = int(input("Enter end of range:"))

# Initilizing counters
even_count = 0
odd_count = 0

# Step 2: Loop through range
for number in range(start,end+1):
    if number % 2 ==0:
        even_count += 1
    else:
        odd_count += 1

# Step 3: Output counts
print(f"\n☑️ Total Even number: {even_count}")
print(f"\n☑️ Total odd number: {odd_count}")

# Step 4: (Bonus) Show Percentages
total_numbers = even_count+odd_count
even_percentage = (even_count/total_numbers)*100
odd_percentage = (odd_count/total_numbers)*100

print(f"\n📊 Even Percentage: {even_percentage:.2f}%")
print(f"\n📊 Odd Percentage: {odd_percentage:.2f}%")