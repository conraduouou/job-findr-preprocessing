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
2. experience
3. experience_role
4. experience_years
5. hard_skills
6. soft_skills
7. certifications
8. training
9. degree

... with each key having a list (array) value of strings. If there is no valid value for a given feature, supply an empty array instead.