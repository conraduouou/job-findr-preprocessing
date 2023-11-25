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
    python -c "import preprocessing as pre; print(pre.prepare_age(\"__12]]\"))"
    # Should output "12"
    ```
