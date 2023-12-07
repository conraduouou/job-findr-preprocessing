# Job-FinDR Custom Preprocessing Package

Preprocessing package that contains methods and utility functions custom-made for our thesis tool, Job-FinDR.

## Requirements

1. An instance of ELMo must be present in the current working directory. This will be a directory containing the model and should be named "elmo".

## Steps in installation

1. Run the following command in the terminal.
    ```
    pip install git+https://github.com/conraduouou/job-findr-preprocessing
    ```

2. This should then give you the `preprocessing` package made for Job-FinDR. To confirm its functionality, you can run the following command in your terminal:
    ```
    python -c "import preprocessing as pre; print(pre.prepare_age([\"__12]]\"]))"
    # Should output "12"
    ```

## The most important function

All you need with this package, really, is just the `prepare_features` function.

To run it as I have intended, you have to supply a dictionary argument that contains all the features as string keys:

1. age
2. sex
3. experience
4. experience_role
5. experience_years
6. hard_skills
7. soft_skills
8. certifications
9. training
10. degree

... with each key having a list (array) value of strings. If there is no valid value for a given feature, supply an empty array instead.

This is effective when preprocessing a single set of resume data. For preprocessing multiple resume data, it should be in the form of a
csv, where rows denote each resume and columns defining the feature.

## Sample CSV data:
```csv
age,sex,experience,experience_role,experience_years,hard_skills,soft_skills,certifications,training,degree,job_field
28,m,Software Engineer,Lead Developer,5,Java,Communication,Oracle Certified Professional,Agile Development,Creative Writing,Technology
34,f,Data Scientist,Machine Learning Engineer,7,Python,Analytical Thinking,Data Science Professional,Deep Learning,Master's in Data Science,Technology
25,m,UX Designer,Interaction Designer,3,UI/UX Design,Empathy,Adobe XD Certification,Human-Computer Interaction,Bachelor's in Design,Services
31,f,Project Manager,Scrum Master,8,Project Management,Leadership,Project Management Professional,Agile Leadership,Certified ScrumMaster,Management
29,m,Network Administrator,Systems Administrator,6,Network Security,Troubleshooting,Cisco Certified Network Associate,Network Administration,Bachelor's in Information Technology,Technology
```