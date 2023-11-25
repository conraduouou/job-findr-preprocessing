from datetime import datetime
from .degree_labels import DEGREE_LABELS
import string

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
            value = -1
        try:
            value = int(value)
        except ValueError:
            value = value.strip(string.punctuation + string.whitespace + string.ascii_letters)
    return value


def prepare_age(age_strs: list[str] | None) -> int | str:
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
        # remove special characters from both ends
        # handy, since this also removes a dash (minus, hyphen) character, so as to
        # prevent negative numbers from being output
        age = age_str.strip(string.punctuation)
        
        try:
            age = int(age)
        except ValueError:
            return "N/A"
        
        return age


def prepare_certifications(cert_array: list[str] | None) -> bool:
    """
    Expects a list of strings that contains the applicant's certifications.

    If there is at least one (1) certification found, then return True.
    """
    return cert_array != None and len(cert_array) > 0


def prepare_training(training_array: list[str] | None) -> bool:
    """
    Expects a list of strings that contains the applicant's training data.

    If there is at least one (1) training data found, then return True.
    """
    return training_array != None and len(training_array) > 0


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