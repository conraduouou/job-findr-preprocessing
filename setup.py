from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Job-FinDR Preprocessing package'
LONG_DESCRIPTION = 'A custom preprocessing package made for preparing data to be fed to the C5.0 Decision Tree.'

# Setting up
setup(
        name="preprocessing", 
        version=VERSION,
        author="Louise Lalu",
        author_email="louiserafaellalu@gmail.com",
        url="https://github.com/conraduouou/job-findr-preprocessing",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        keywords=['preprocessing', 'custom'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)