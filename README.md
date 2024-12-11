# Data Science Exploration
This repository contains a collection of data science projects and exploratory analyses. 
The primary objective is to showcase various machine learning techniques, data manipulation, and statistical analysis methods to solve real-world problems.

Table of Contents:
1. Risk Model for Credit Loan Default Prediction // [Notebook](finance/risk-modeling/main.ipynb)


Older projects:
1. Data Collection // [Repo](https://github.com/jannctu/PythonDataCollection)
2. Software Engineer Salary Prediction // [Repo](https://github.com/jannctu/SoftwareEngineerSalaryEstimation)
3. Apache Spark Demo // [Repo](https://github.com/jannctu/apache-spark-demo)
4. Various Data Science Projects // [Repo](https://github.com/jannctu/Kaggle-Submissions)
   - Data Visualization
     - Student Performance on Exam
     - Software Developer Survey
     - Speech Recognition 
     - Bitcoin Price A gentle introduction Technical Analysis on Python.
   
   - Classification
     - Titanic
     - Gender Classification
     - Twitter Sentiment Analysis
     - Fish Classification
   - Regression
     - CommonLitReadability 




## Prerequisites

Before running the script, ensure you have the following set up:

1. **Python**: Make sure Python 3.x is installed. You can download Python from [here](https://www.python.org/downloads/).
2. **Kaggle API Key**: You need a Kaggle API key (`kaggle.json`) to authenticate the Kaggle API. Follow these steps:
   - Go to your [Kaggle Account](https://www.kaggle.com/account) page.
   - Scroll down to the **API** section and click **Create New API Token**.
   - Download the `kaggle.json` file.

3. **Install Dependencies**: The script uses the `kaggle` and `python-dotenv` packages. You can install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
    ```
4. **Environment Variable Configuration**:
   - Place the kaggle.json file you downloaded in the project root or a specific directory.
   - Set up a .env file to specify the path to kaggle.json. `KAGGLE_CONFIG_DIR`