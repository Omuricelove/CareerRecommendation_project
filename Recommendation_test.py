from Recommendation_engine import calculate_career_match
from Career_profile import career_profile
from Recommendation_engine import validate_rating, validate_student_profile

test_student_profile = {
    "programming": {
        "skill": 6,
        "preference": 5
    },
    "problem_solving": {
        "skill": 3,
        "preference": 4
    },
    "communication": {
        "skill": None,
        "preference": None
    }
}


score = calculate_career_match(test_student_profile, career_profile["ui_ux_designer"])

print(score)


cleaned_profile, validation_errors = validate_student_profile(test_student_profile)

print("Cleaned profile:")
print(cleaned_profile)

print("Validation errors:")
print(validation_errors)