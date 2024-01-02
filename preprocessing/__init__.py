import csv
import numpy as np
import pandas as pd
import tensorflow_hub as hub
import tensorflow as tf
import os
import string

from datetime import datetime
from sklearn.metrics.pairwise import cosine_similarity

from .degree_labels import DEGREE_LABELS
from .baselines import *

# ELMo doesn't support eager execution
tf.compat.v1.disable_eager_execution()

__CURRENT_STRING_CONSTANTS = [ "current", "present", "now", "cur" ]

__MONTH_CONSTANTS = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
]

__ELMO_PATH = "elmo"

def __check_elmo_model() -> bool:
    current_dir = os.getcwd()
    elmo_path = os.path.join(current_dir, __ELMO_PATH)
    return os.path.isdir(elmo_path)

# check path if elmo model exists
if not __check_elmo_model():
    raise FileNotFoundError("A path to a ELMo is required to run this package.")

# def set_elmo_path(elmo_path: str):
#     """
#     An optional function to set the relative path to the ELMo model.
#     """

#     global elmo

#     if not __check_elmo_model():
#         raise FileNotFoundError("A path to a ELMo is required to run this package.")

#     elmo = hub.Module(elmo_path)

def __has_current_string(value: str) -> bool:
    for word in __CURRENT_STRING_CONSTANTS:
        if word in value:
            return True
    return False

def __is_character_surrounded_by_numbers(input_string: str, target_character: str) -> bool:
    index = input_string.find(target_character)
    return (
        index != -1
        and index > 0
        and index < len(input_string) - 1
        and (input_string[index - 1].isdigit()
             or input_string[index + 1].isdigit())
    )

def __has_month_word(value: str) -> bool:
    for word in __MONTH_CONSTANTS:
        if word in value.lower():
            return True
    return False

def __has_month_number(value: str) -> bool:
    if "-" in value or "/" in value:
        return True
    
def __force_parse_int(value: str) -> int:
    """
    Go in a while loop until the value inserted is parsed to integer.

    Returns -1 when the value cannot be parsed anymore and is found to have no number characters.
    """
    while type(value) == str:
        if len(value) == 0:
            return -1
        try:
            value = int(float(value))
        except ValueError:
            value = value.strip(string.punctuation + string.whitespace + string.ascii_letters)
    return abs(value)

def __get_field(resume_data: list[str]) -> str:
    # get tuples of hard skills 
    tuples = list(JOB_FIELDS_BASELINES.items())
    baseline_statements = [ value for _, value in tuples ]

    resume_embeddings = __get_embeddings(resume_data)[0]
    statement_embeddings = __get_embeddings(*baseline_statements)

    max_score = -2
    max_index = 0
    for baseline_index in range(len(statement_embeddings)):
        statements = statement_embeddings[baseline_index]
        for statement in statements:
            baseline_mean = np.reshape(np.mean(statement, axis=0), (1, -1))
            for item in resume_embeddings:
                item_mean = np.reshape(np.mean(item, axis=0), (1, -1))
                similarity = cosine_similarity(baseline_mean, item_mean)
                similarity = float(similarity.squeeze())

                if similarity > max_score:
                    max_score = similarity
                    max_index = baseline_index

    return tuples[max_index][0]

def __get_embeddings(*args: list[str]) -> list[np.ndarray]:
    graph = tf.Graph()
    with graph.as_default():
        # Load ELMo model
        elmo = hub.Module(__ELMO_PATH)

        to_embed = []

        for arg in args:
            to_add = elmo(
                arg,
                as_dict=True,
                signature="default"
            )["word_emb"]

            to_embed.append(to_add)
        
        init_op = tf.group([tf.compat.v1.global_variables_initializer(), tf.compat.v1.tables_initializer()])
    graph.finalize()
    
    # Since ELMo doesn't support eager execution, running the `elmo` variable doesn't
    # give us the numpy arrays yet--it has to be run in a session.
    with tf.compat.v1.Session(graph=graph) as session:
        session.run(init_op)

        to_return = []
        for item in to_embed:
            to_return.append(session.run(item))

    return to_return


def __get_max_similarity(baselines: list[str], data: list[str]) -> float:
    """
    Expects 2 3D numpy arrays that contains the ELMo embeddings of every token (word) in a baseline
    or the actual value in the 3rd axis.

    Returns a float that defines the similarity score between each statement from both arrays.
    """

    embeddings = __get_embeddings(baselines, data)
    embeddings1 = embeddings[0]
    embeddings2 = embeddings[1]

    # Actual similarity check using cosine
    max_score = -2
    for emb1 in embeddings1:
        emb1_mean = np.reshape(np.mean(emb1, axis=0), (1, -1))
        for emb2 in embeddings2:
            emb2_mean = np.reshape(np.mean(emb2, axis=0), (1, -1))
            similarity = cosine_similarity(emb1_mean, emb2_mean)
            similarity = float(similarity.squeeze())

            if similarity > max_score:
                max_score = similarity
    
    return max_score


def __get_prepared(data: dict, is_common=False, field: str | None=None) -> dict:
    if field:
        job_field = field
    else:
        job_field = __get_field(
            data["experience"]
            + data["experience_role"]
            + data["hard_skills"]
            + data["degree"]
            + data["certifications"]
            + data["training"]
        )

    prepared = {
        "age": [prepare_age(data["age"])],
        "sex": [data["sex"]],
        "experience": [prepare_experience(data["experience"], job_field)],
        "experience_role": [prepare_experience_role(data["experience_role"])],
        "experience_years": [prepare_experience_years(data["experience_years"])],
        "hard_skills": [prepare_hard_skills(data["hard_skills"], job_field)],
        "soft_skills": [prepare_soft_skills(data["soft_skills"], job_field)],
        "certifications": [prepare_certifications(data["certifications"])],
        "degree": [prepare_degree(data["degree"])],
        "training": [prepare_training(data["training"])],
        "job_field": [job_field],
    }

    if is_common:
        del prepared["experience"]
        del prepared["experience_years"]
        del prepared["hard_skills"]
        del prepared["soft_skills"]
        del prepared["certifications"]
        del prepared["training"]

    return prepared


def prepare_features(features: dict | str, is_common: bool=False, field: str | None=None):
    """
    A utility function that runs the individual preprocessing functions and generates
    a csv file containing the values.

    The `features` argument can either be of type `dict` or `str`. If it's a string, then
    it is assumed to be a path to the csv containing data of a resume per row.
    
    The dictionary to be inputted here as an argument must have the following features as
    string keys, with list values (except for sex):

    1. age
    2. sex
    3. experience
    4. experience_role
    5. experience_years
    6. hard_skils
    7. soft_skills
    8. certifications
    9. degree
    10. training
    
    If there are no values found or valid for a specific feature, supply an empty array.

    If the data is generated from a csv file, the continuous values will be expected to have
    a phrase or sentence belonging to a feature. These values are experience, experience_role,
    hard_skills, soft_skills, certifications, and training, which are all expected to have
    multiple values in a real life application.
    
    For convenience purposes, the data inputted in the csv are expected to be THE CLOSEST 
    SOUNDING TO BEING PROFESSIONAL, as the numerical value converted from the continuous value
    is acquired through `max` anyway, not the mean. Judge whether each statement is indeed the
    closest to being professional as best as you can.
    """

    if field != None:
        field = field.lower()
        if field not in JOB_FIELDS:
            raise ValueError(f"Field supplied is not supported. This value should only be {JOB_FIELDS}.")

    if type(features) == str:
        df = pd.read_csv(features)
        output = df.apply(lambda x: x.to_dict(), axis=1).tolist()

        # str conversion of features as well as data format preparation
        output = [ { key: ([str(value)] if key != "sex" else value) for key, value in resume_data.items() } for resume_data in output ]

        prepared = {}
        count = 1
        for data in output:
            processed = __get_prepared(data, is_common, field)
            if not prepared:
                prepared = processed
            else:
                for key, value in processed.items():
                    prepared[key].extend(value)
            
            print(f"Finished processing data count #{str(count).rjust(4)}")
            count += 1
    else:
        prepared = __get_prepared(features, is_common, field)

    to_csv = [
        list(prepared.keys()),
    ]

    to_csv.extend(
        [ [ prepared[k][i] for k in prepared.keys() ] for i in range(len(prepared["age"])) ]
    )

    result_dir = "preprocessed_result"
    
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    
    file_path = os.path.join(result_dir, "result.csv")

    with open(file_path, "w", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in to_csv:
            csv_writer.writerow(row)
    

def prepare_age(age_strs: list[str] | None) -> int | None:
    """
    Expects a string with which the applicant's age will be inferred.

    Knowing this will be received from LayoutLM, various forms of this string
    should be considered, thoroughly tested.

    *NOTE*: This returns THE FIRST VALID AGE FOUND from the list. Once found, all subsequent
    values in the list are disregarded.
    """

    # Return nil if array does not contain anything or if it's None
    if not age_strs or len(age_strs) == 0:
        return None

    for age_str in age_strs:
        age = __force_parse_int(age_str)
        if age == -1:
            return None
        return age


def prepare_certifications(cert_array: list[str] | None) -> str:
    """
    Expects a list of strings that contains the applicant's certifications.

    If there is at least one (1) certification found, then return TRUE (string).
    """
    if cert_array == None:
        return "FALSE"
    elif len(cert_array) == 1 and "nan" in cert_array:
        return "FALSE"
    
    for cert_str in cert_array:
        if len(cert_str) > 0:
            return "TRUE"

    return "FALSE"


def prepare_training(training_array: list[str] | None) -> str:
    """
    Expects a list of strings that contains the applicant's training data.

    If there is at least one (1) training data found, then return TRUE (string).
    """
    if training_array == None:
        return "FALSE"
    elif len(training_array) == 1 and "nan" in training_array:
        return "FALSE"
    
    for training_str in training_array:
        if len(training_str) > 0:
            return "TRUE"

    return "FALSE"


def prepare_experience_years(years_array: list[str]) -> int | None:
    """
    Expects a list of string values acquired by LayoutLM.

    This could come in a variety of forms, most notably in the form of year range (YYYY-YYYY)
    with spaces in between, simple (natural numbers), or with a mixture of strings (YYYY-current).

    Preprocessing should at least be able to cater to common forms.
    """

    # Return nil if array does not contain anything or if it's None
    if not years_array or len(years_array) == 0:
        return None

    # if years of experience is mentioned somewhere in the summary, we'll return
    # this instead. We can't make sure, however. That's why we'll still loop through
    # the whole array and then compare the two values. We'll return whichever is greater
    # then.
    summary_years = 0

    # keep track of years of experience
    experience_years = 0

    # keep track of months, if applicable
    # experience_months = 0

    for value in years_array:
        value = value.strip(string.punctuation + string.whitespace)

        # if value is found to be in the form of range, then it must be
        # split and computed accordingly
        if "-" in value or "to" in value:
            if "to" in value:
                split_character = "to"
            # if the applicant used dashes as separators of both the date and range,
            # we'll assume they separated the start and end dates with a dash surrounded
            # by spaces.
            elif value.count("-") > 1:
                split_character = " - "
            else:
                split_character = "-"
            
            years = [ year.strip(string.punctuation) for year in value.split(split_character) ]

            # We're essentially expecting a range between two values. If what we got from splitting
            # the string were more, then we'll have to assume it's a failed parse.
            if len(years) > 2:
                continue

            ### ---- Handle MONTH format here ---- ###

            # a quick check if LayoutLM understood the number 0 (zero) as the letter O, as it
            # does in many other fonts.
            for year in years:
                if __is_character_surrounded_by_numbers(year, "o"):
                    year = year.replace("o", "0")

            if __has_current_string(years[1].lower()):
                # we'll just assume the applicant is still working currently
                current_year = datetime.now().year
                experience_years += current_year - int(years[0])
            else:
                experience_years += int(years[1]) - int(years[0])

        # if value isn't in the form of a range, it's probably a year, in which case we'll add 1
        # accordingly to what we'll return.
        else:
            # SPECIAL CASE: if value is just in current constants and nothing else, then we'll have
            # to assume he's been working for a year.
            if __has_current_string(value.lower().strip(string.punctuation)):
                experience_years += 1
                continue

            value = __force_parse_int(value)

            # if value is found to be a year, add 1 to experience_years
            if value > 1900:
                experience_years += 1
            # SPECIAL CASE: if years of experience is found in the summary, then we
            # may have to assume that the applicant stated his total years of experience.
            elif value > 0:
                summary_years = value
    
    return max(experience_years, summary_years)


def prepare_experience(experience_array: list[str] | None, field: str) -> float | None:
    """
    Expects a list of experiences that contains the applicant's experience data.

    This function makes use of the ELMo model to compare baseline statements, ultimately
    determining **professional** an applicant's resume seems.

    This might be a flaw in the system, since it does not determine how close an experience
    is to a specific role. This is a future recommendation for researchers.
    """
    # Return nil if array does not contain anything or if it's None
    if not experience_array or len(experience_array) == 0 or field not in JOB_FIELDS:
        return None
    
    list = []

    # clean data
    for experience in experience_array:
        experience = experience.strip(string.punctuation + string.whitespace)
        if len(experience) > 0:
            list.append(experience)

    if len(list) == 0:
        return None

    return __get_max_similarity(EXPERIENCE_BASELINES[field], list)


def prepare_hard_skills(hard_array: list[str] | None, field: str) -> float | None:
    """
    Expects a list of hard skills that contains the applicant's hard skills data.

    This function makes use of the ELMo model to compare baseline statements, ultimately
    determining **professional** an applicant's resume seems.

    This might be a flaw in the system, since it does not determine how close a hard skill
    is to a specific role. This is a future recommendation for researchers.
    """
    # Return nil if array does not contain anything or if it's None
    if not hard_array or len(hard_array) == 0 or field not in JOB_FIELDS:
        return None
    
    list = []

    # clean data
    for skill in hard_array:
        skill = skill.strip(string.punctuation + string.whitespace)
        if len(skill) > 0:
            list.append(skill)

    if len(list) == 0:
        return None

    return __get_max_similarity(HARD_SKILLS_BASELINES[field], list)


def prepare_soft_skills(soft_array: list[str] | None, field: str) -> float | None:
    """
    Expects a list of soft skills that contains the applicant's soft skills data.

    This function makes use of the ELMo model to compare baseline statements, ultimately
    determining **professional** an applicant's resume seems.

    This might be a flaw in the system, since it does not determine how close a hard skill
    is to a specific role. This is a future recommendation for researchers.
    """
    # Return nil if array does not contain anything or if it's None
    if not soft_array or len(soft_array) == 0 or field not in JOB_FIELDS:
        return None
    
    list = []

    # clean data
    for skill in soft_array:
        skill = skill.strip(string.punctuation + string.whitespace)
        if len(skill) > 0:
            list.append(skill)

    if len(list) == 0:
        return None

    return __get_max_similarity(SOFT_SKILLS_BASELINES[field], list)


def prepare_experience_role(role_array: list[str] | None) -> float | None:
    """
    Expects a list of roles that contains the applicant's past roles.

    This function makes use of the ELMo model to compare baseline statements, ultimately
    determining **professional** an applicant's resume seems.

    This might be a flaw in the system, since it does not determine how close a hard skill
    is to a specific role. This is a future recommendation for researchers.
    """
    # Return nil if array does not contain anything or if it's None
    if not role_array or len(role_array) == 0:
        return None
    
    list = []

    # clean data
    for role in role_array:
        role = role.strip(string.punctuation + string.whitespace)
        if len(role) > 0:
            list.append(role)

    if len(list) == 0:
        return None

    return __get_max_similarity(ROLE_BASELINES, list)

    
def prepare_degree(degree_strs: list[str] | None) -> str | None:
    """
    Expects a string that contains information regarding the applicant's finished course.

    This should return a value within the scope of the DEGREE_LABELS constant dict.

    *NOTE*: This returns THE FIRST VALID DEGREE FOUND from the list. Once found, all subsequent
    values in the list are disregarded.
    """

    # Return nil if array does not contain anything or if it's None
    if not degree_strs or len(degree_strs) == 0:
        return None
    
    for degree_str in degree_strs:
        words = degree_str.strip(string.punctuation + string.digits).lower().split()
        word_count = len(words)

        for index in range(word_count):
            current_word = words[index]

            for label, options in DEGREE_LABELS.items():
                name_tokens = options["name"]
                abbreviations = options["abbr"]

                # check if there's a match in the created LABELS constant
                if len(name_tokens) <= word_count - index:
                    is_match = True
                    for j in range(len(name_tokens)):
                        if name_tokens[j] != words[index + j]:
                            is_match = False
                            break
                    
                    if is_match:
                        return label
                
                # check if current word is in abbreviated form, in which case the
                # label should be returned as well.
                for j in range(len(abbreviations)): 
                    if current_word == abbreviations[j]:
                        return label