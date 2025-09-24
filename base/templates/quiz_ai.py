import math
user_progress = {
    "easy": {"attempts": ' ', "average": ' '},
    "medium": {"attempts": ' ', "average": ' '},
    "hard": {"attempts": ' ', "average": ' '}
}

def get_suggestion(progress):
    if progress['easy']['attempts'] >=5 and progress['easy']['average'] >= 80:
        return "You are doing great with easy questions! try medium level MCQs!"
    elif progress['medium']['attempts'] >=5 and progress['medium']['average'] >= 80:
        return "You are doing great with medium questions! try hard level MCQs!"
    elif progress['hard']['attempts'] >=5 and progress['hard']['average'] >= 80:
        return "You are doing great with hard questions! try more challenging MCQs!"
    else:
        return "Keep practicing to improve your skills."
print(get_suggestion(user_progress)) 