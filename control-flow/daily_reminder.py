# daily_reminder.py

# === Prompt for a Single Task ===
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# === Process the Task Based on Priority and Time Sensitivity ===
match priority:
    case "high":
        if time_bound == "yes":
            # === Provide a Customized Reminder ===
            # === Print a reminder about the task that includes its priority level and whether immediate action is required based on time sensitivity ===
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Consider addressing it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Consider working on it when possible.")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"Reminder: '{task}' has an unknown priority. Please enter high, medium, or low.")

# === Well done message ===
print("\n✅ Well done on completing this project! Let the world hear about this milestone achieved.")
