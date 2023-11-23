import unittest
from preprocessing import preprocessing as pre

class TestAgePreprocessing(unittest.TestCase):
    def test_age(self):
        result = pre.prepare_age("12")
        assert type(result) == int
        result = pre.prepare_age("0")
        assert type(result) == int
    
    def test_negative(self):
        result = pre.prepare_age("-1")
        assert result > 0

    def test_age_with_whitespace(self):
        result = pre.prepare_age("12  ")
        assert type(result) == int
        result = pre.prepare_age("12  \n")
        assert type(result) == int

    def test_age_with_special_character(self):
        result = pre.prepare_age("12|")
        assert type(result) == int
        result = pre.prepare_age("-++-+++==45!)|||")
        assert type(result) == int

    def test_not_age(self):
        result = pre.prepare_age("says what on your bun")
        assert result == "N/A"
        result = pre.prepare_age("...,, // ))")
        assert result == "N/A"


class TestCertificationsPreprocessing(unittest.TestCase):
    def test_certifications(self):
        result = pre.prepare_certifications(2)
        assert result
        result = pre.prepare_certifications(0)
        assert not result


class TestTrainingPreprocessing(unittest.TestCase):
    def test_training(self):
        result = pre.prepare_training(2)
        assert result
        result = pre.prepare_training(0)
        assert not result


class TestExperienceYearsPreprocessing(unittest.TestCase):
    def test_year(self):
        result = pre.prepare_experience_years(["2023", "2000"])
        assert result == 2
        result = pre.prepare_experience_years(["1938"])
        assert result == 1

    def test_year_range(self):
        result = pre.prepare_experience_years(["2023-2025", "2018 to 2023", "2017 - 2018"])
        assert result == 8
        result = pre.prepare_experience_years(["2019-current"])
        assert result == 4

    def test_not(self):
        result = pre.prepare_experience_years(["-- !! )"])
        assert result == 0
        result = pre.prepare_experience_years(["hehe"])
        assert result == 0
    
    def test_summary(self):
        result = pre.prepare_experience_years(["4"])
        assert result == 4
        result = pre.prepare_experience_years(["12 years"])
        assert result == 12
        result = pre.prepare_experience_years(["-- ! \\|| | 12 -- ! "])
        assert result == 12

    def test_summary_with_range(self):
        result = pre.prepare_experience_years(["2000-2010", "2018 to 2024", "15"])
        assert result == 16

    def test_current(self):
        result = pre.prepare_experience_years(["present"])
        assert result == 1
        result = pre.prepare_experience_years(["presently"])
        assert result == 1
        result = pre.prepare_experience_years(["current"])
        assert result == 1
        result = pre.prepare_experience_years(["currently"])
        assert result == 1
        result = pre.prepare_experience_years(["cur"])
        assert result == 1
        result = pre.prepare_experience_years(["CURRENTLY"])
        assert result == 1
        result = pre.prepare_experience_years(["now"])
        assert result == 1
        result = pre.prepare_experience_years(["what are you doing"])
        assert result == 0
        result = pre.prepare_experience_years(["no"])
        assert result == 0


class TestDegreePreprocessing(unittest.TestCase):
    def test_degree(self):
        result = pre.prepare_degree("Bachelor in Computer Science")
        assert result == "computer science"
        result = pre.prepare_degree("00== 1 history")
        assert result == "history"
        result = pre.prepare_degree("history")
        assert result == "history"
        result = pre.prepare_degree("polsci")
        assert result == "political science"
        result = pre.prepare_degree("bspa")
        assert result == "public administration"
        result = pre.prepare_degree("hrm")
        assert result == "hotel and restaurant management"
        result = pre.prepare_degree("")
        assert result == None


if __name__ == '__main__':
    unittest.main()