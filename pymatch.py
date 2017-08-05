"""This program is designed to generate a short dating profile for users then
    using this profile, find a love match from the database.

    The program should guide the user through the questionnaire, compute a love
    match, then return a single matching candidate's name (str) to the user.

    By Rachel Quilligan, 2017
"""
def physical_characteristics_question(question, answer1, answer2, answer3):
    """Prompts user to answer questions about physical preferences.

    Parameters:
        question (str): The question posed about physical characteristics.
        answer1 (str): The first answer choice
        answer2 (str): The second answer choice
        answer2 (str): The third answer choice

    Return:
        int: The number corresponding to the user's choice of answer.
    """
    print(question, answer1, answer2, answer3)
    while True:
        response = input("Please enter your answer: ")
        if response.isdigit() == True:
            response = int(response)
            if response in range(1, 4):
                return response
            else:
                print("I'm sorry, that response wasn't valid. Please select the",
                  " number corresponding to your choice.")
        else:
            print("I'm sorry, that response wasn't valid. Please select the",
                  " number corresponding to your choice.")
            
def personality_question(question):
    """Prompts the user to answer questions about their personality type.

    Parameters:
        question (str): THe question posed to the user.

    Return:
        int: The number corresponding to the user's answer. 
    """
    answer_set ="1) Yes\n2) Most of the time\n3) Neutral\n4) Sometimes\n5) No"
    print(question)
    print(answer_set)
    while True:
        response = input("Please enter your answer: ")
        if response.isdigit() == True:
            response = int(response)
            if response in range(1, 6):
                return response
            else:
                print("I'm sorry, that response wasn't valid. Please select the",
                  " number corresponding to your choice.")
        else:
            print("I'm sorry, that response wasn't valid. Please select the",
                  " number corresponding to your choice.")

def personality_score():
    """Calculates the user's final personality score as determined by the
    personality questionnaire and then totalling the user's results and
    multiplying that by two.

    Return:
        int: The user's final personality score.
    """
    score = 2 * (personality_question("Do you find it easy to introduce " +
                                      "yourself to other people?")
                 + personality_question("Do you usually initiate " +
                                        "conversations?")
                 + personality_question("Do you often do something out of " +
                                        "sheer curiosity?")
                 + personality_question("Do you prefer being out with a " +
                                        "large group of friends rather than"
                                        " spending time on your own?")
                 )
    return score

def matchmaker(gender, sexual_pref, height, height_pref, personality_score):
    """Sifts the database for the best partner match.

    Evaluates gender and sexual preference matching, followed by personality
    score matching, then height preference matching, to find the best candidate
    for the user.

    Parameters:
        gender (str): the user's gender, as gleaned from earlier questionnaire
        sexual_pref (str): the user's preferred gender of the database candidate
        height (str): the user's height, as gleaned from earlier questionnaire
        height_pref (str): the user's preferred height of the candidate
        personality_score (int): the user's personality score, as determined by
        personality_score()

    Return:
        str: The name of the best suited candidate
    """
    import partners
    potential_partners = partners.Partners()
    best_score = 40
    height_list = []
    height_pref_list = []
    best_partner = None
    while potential_partners.available():
        if (potential_partners.get_gender() == sexual_pref and
            gender == potential_partners.get_sexual_pref()):
            personality_value = abs(potential_partners.get_personality_score()
                                    - personality_score)
            if personality_value < best_score:
                best_score = personality_value
                best_partner = potential_partners.get_name()
            elif personality_value == best_score:
                if potential_partners.get_height() == height_pref:
                    height_list.append(potential_partners.get_name())
                    if len(height_list) == 1:
                        best_partner = height_list[0]
                    elif len(height_list) > 1:
                        if potential_partners.get_height_pref() == height:
                            height_pref_list.append(potential_partners.
                                                    get_name())
                            best_partner = height_pref_list[0]
                elif potential_partners.get_height() != height_pref:
                    if potential_partners.get_height_pref() == height:
                        height_pref_list.append(potential_partners.get_name())
                        best_partner = height_pref_list[0]
                    elif potential_partners.get_height_pref() != height:
                        best_partner = potential_partners.get_name()
    return best_partner

def main_program():
    """The main function that runs the partner-matching program and guides the
    user.

    Outlines all the instructions and brings together the functionality of the
    rest of the code.

    Return:
        str: The name of the best matched person from the database.

    """
    print("Welcome to PyMatch")
    name = input("Please enter your name: ")

    print("\nHi " + name + ". ")
    first_question = physical_characteristics_question("What is your gender?",
                                                       "\n1) male",
                                                       "\n2) female",
                                                       "\n3) other")
    if first_question == 1:
        first_answer = "male"
    elif first_question == 2:
        first_answer = "female"
    elif first_question == 3:
        first_answer = "other"
    second_question = physical_characteristics_question("What is your sexual" +
                                                        " preference?",
                                                        "\n1) male",
                                                        "\n2) female",
                                                        "\n3) other")
    if second_question == 1:
        second_answer = "male"
    elif second_question == 2:
        second_answer = "female"
    elif second_question == 3:
        second_answer = "other"
    third_question = physical_characteristics_question("What is your height?",
                                                       "\n1) tall",
                                                       "\n2) medium",
                                                       "\n3) short")
    if third_question == 1:
        third_answer = "tall"
    elif third_question == 2:
        third_answer = "medium"
    elif third_question == 3:
        third_answer = "short"
    fourth_question = physical_characteristics_question("What height do you" +
                                                        " prefer your partne" +
                                                        "r to be?",
                                                        "\n1) tall",
                                                        "\n2) medium",
                                                        "\n3) short")
    if fourth_question == 1:
        fourth_answer = "tall"
    elif fourth_question == 2:
        fourth_answer = "medium"
    elif fourth_question == 3:
        fourth_answer = "short"
    print("We will now ask you some questions to try to determine your" +
          " personality type.")
    score = personality_score()
    final_match = matchmaker(first_answer, second_answer, third_answer,
                             fourth_answer, score)
    print("Thank you for answering all the questions. We have found your best",
          "match from our database and hope that you enjoy getting to know",
          "each other. Your best match is:\n",final_match)
main_program()
