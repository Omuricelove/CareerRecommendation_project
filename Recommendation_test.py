from Recommendation_engine import calculate_career_match
from Career_profile import career_profile
from Recommendation_engine import validate_rating, validate_student_profile

test_student_profile = {
    "programming": {
        "skill": 5,
        "preference": 4
    },
    "problem_solving": {
        "skill": 5,
        "preference": 5
    },
    "communication": {
        "skill": None,
        "preference": None
    }
}

cleaned_profile, validation_errors = validate_student_profile(test_student_profile)

score = calculate_career_match(cleaned_profile, career_profile["ui_ux_designer"])

print(score)

print("Cleaned profile:")
print(cleaned_profile)

print("Validation errors:")
print(validation_errors)