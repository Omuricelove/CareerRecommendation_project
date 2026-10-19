from Student_profile import student_profile
from Career_profile import career_profile


def validate_rating(value):
    if value is None:
        return True
    if not isinstance(value, int) or isinstance(value, bool):
        return False
    if value < 1 or value > 5:
        return False
    return True

def validate_student_profile(student_profile):
    validation_errors = []

    # Check each attribute in the student profile
    for attribute, rating in student_profile.items():

        # Check skill and preference separately
        for field in ["skill", "preference"]:
            value = rating.get(field)

            # Missing ratings are allowed
            if value is None:
                continue

            # Record invalid ratings      
            if not validate_rating(value):
                validation_errors.append({
                    "attribute": attribute,
                    "field": field,
                    "value": value,
                    "reason": "Rating must be an integer from 1 to 5"
                })

                
                # Replace invalid rating with None
                rating[field] = None

    return student_profile,validation_errors


def calculate_skill_match(student_skill, career_requirement):
    calculate_skill = student_skill / career_requirement * 100

    if calculate_skill > 100:
        calculate_skill = 100

    return calculate_skill


def calculate_preference_match(student_preference, career_involvement):
    calculate_difference = abs(student_preference - career_involvement)
    calculate_preference = (1 - calculate_difference / 4) * 100

    return calculate_preference


def calculate_attribute_match(skill_match, preference_match):
    if skill_match is None or preference_match is None:
        return None

    calculate_attribute = (skill_match * 0.60) + (preference_match * 0.40)

    return calculate_attribute


def calculate_career_match(student_profile, career_profile):

    attribute_matches = []

    for attribute in student_profile:

        student_skill = student_profile[attribute].get("skill")
        student_preference = student_profile[attribute].get("preference")

        career_skill = career_profile[attribute].get("skill")
        career_involvement = career_profile[attribute].get("involvement")

        if student_skill is None and student_preference is None:
            continue

        #Handle student_skill missing attribute
        if student_skill is not None:
            skill_match = calculate_skill_match(student_skill, career_skill)
        else:
            skill_match = None

        #Handle Student_preference missing attribute
        if student_preference is not None:
            preference_match = calculate_preference_match(student_preference, career_involvement)
        else:
            preference_match = None

        #Handle missing skill_match
        if skill_match is not None and preference_match is not None:
            attribute_match = calculate_attribute_match(skill_match, preference_match)

        elif skill_match is not None:
            attribute_match = skill_match   
        else:
            attribute_match = preference_match 

        if attribute_match is not None:
            attribute_matches.append(attribute_match)

        print(attribute)
        print("Student Skill:", student_skill)
        print("Student Preference:", student_preference)
        print("------------------------------------------")
        print("Career Skill:", career_skill)
        print("Career Involvement:", career_involvement)
        print("------------------------------------------")
        print("Skill Match:", skill_match)
        print("Preference Match:", preference_match)
        print("------------------------------------------")
        print("Attribute Match:", attribute_match)
        print("\n")


    total = 0

    for num in attribute_matches:
        total += num

    if len(attribute_matches) == 0:
        return None

    average = total / len(attribute_matches)

    return average

if __name__ == "__main__":

    career_scores = {}

    for career in career_profile:

     career_score = calculate_career_match(student_profile, career_profile[career])

     career_scores[career] = career_score


    ranked_careers = sorted(career_scores.items(), key=lambda item: item[1],reverse=True)

    print(ranked_careers)

    