import json

def load_questions(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def ask_questions(questions):
    score = 0
    for question in questions:
        print("\n" + question["question"])
        for option in question["options"]:
            print(option)
        answer = input("Your answer (a-d): ")
        if answer == question["answer"]:
            score += 1
    return score

def main():
    filename = 'questions.json'
    data = load_questions(filename)
    
    name = input("Enter your name: ")
    total_questions_answered = 0
    total_score = 0
    
    while True:
        print(f"\nHello, {name}! Please select a subject:")
        subjects = list(data.keys())
        for i, subject in enumerate(subjects, 1):
            print(f"{i}. {subject}")
        
        subject_choice = int(input("Your choice (1-3): "))
        selected_subject = subjects[subject_choice - 1]
        
        print(f"\nYou have selected {selected_subject}. Let's start the quiz!")
        questions = data[selected_subject]
        score = ask_questions(questions)
        
        total_questions_answered += len(questions)
        total_score += score
        
        continue_quiz = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_quiz != 'yes':
            break
    
    if total_questions_answered > 0:
        percentage = (total_score / total_questions_answered) * 100
        print(f"\n{name}, you answered {total_questions_answered} questions in total.")
        print(f"Your total score is {total_score}.")
        print(f"Your score percentage is {percentage:.2f}%.")
        if percentage >= 90:
            grade = 'A'
        elif percentage >= 80:
            grade = 'B'
        elif percentage >= 70:
            grade = 'C'
        elif percentage >= 60:
            grade = 'D'
        else:
            grade = 'F'
        print(f"Your grade is {grade}.")
    else:
        print("No questions were answered.")

if __name__ == "__main__":
    main()
