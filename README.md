# Data Science Salary Estimator: Project Overview 
* Created a tool that estimates data science salaries (MAE ~ $ 11K) to help data scientists negotiate their income when they get a job.
* Used a Dataset containing over 1000 job descriptions from glassdoor
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark. 
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model. 
* Built a client facing API using flask 

## Code and Resources Used 
**Python Version:** 3.7.11  
**Packages:** numpy, pandas, sklearn, matplotlib, seaborn, pickle, flask, json  
**Project Idea and Dataset from [Ken Jee](https://www.linkedin.com/in/kenjee/) 
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  
**Model Deployment using Flask:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2


## Features of the Dataset
Dataset contains 1000 job postings from glassdoor.com. With each job, we got the following:
*	Job title
*	Salary Estimate
*	Job Description
*	Rating
*	Company 
*	Location
*	Company Headquarters 
*	Company Size
*	Company Founded Date
*	Type of Ownership 
*	Industry
*	Sector
*	Revenue
*	Competitors 

## Data Cleaning
After scraping the data, the data was cleaned it up to make it usable for the model. The following changes were made and new variables(feartures) were created:

*	Parsed numeric data out of salary 
*	Made columns for employer provided salary and hourly wages 
*	Removed rows without salary 
*	Parsed rating out of company text 
*	Made a new column for company state 
*	Added a column for if the job was at the company’s headquarters 
*	Transformed founded date into age of company 
*	Made columns for if different skills were listed in the job description:
    * Python  
    * R studio
    * Spark  
    * AWS  
    * Excel 
*	Column for simplified job title and Seniority 
*	Column for description length 

## Exploratory Data Analysis (EDA)
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables. 

HIghlights


## Model Building 

The categorical variables were transformed into dummy variables. Dataset was split into train and tests sets with a test size of 20%.   

Three different models was tested and they were evaluated using Mean Absolute Error(MAE). I chose MAE as an evaluation metric because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.   

The three different models used are:
*	**Multiple Linear Regression** – Baseline for the model
*	**Lasso Regression** – Because of the sparse data from the many categorical variables, a normalized regression like lasso would be effective.
*	**Random Forest** – Again, with the sparsity associated with the data, this estimator would be a good fit. 

## Model performance
The Random Forest model outperformed the other models on the test and validation sets. 
*	**Multiple Linear Regression**: MAE (Mean absolute error) = 38668910.50
*	**Lasso Regression**: MAE = 19.09
*	**Random Forest**: MAE = 12.25

## Model Deployment
In this step, a flask API endpoint was hosted on a local webserver. API endpoint takes in a request with a list of values from a job listing and returns an estimated salary. 



