# REAL_ESTATE_INVESTMENT_COMPANY_PROJECT

<img width="737" alt="image" src="https://user-images.githubusercontent.com/107157533/184054977-81547807-bf90-4f5e-890a-0451922f3a76.png">


# Problem Statement: 
In the mortgage sector, manual loan processing can be time-consuming and prone to human error. 
 
# Solution: 
The Home Loan Qualifier App is designed to automate the loan evaluation process and  assess the risk of lending to borrowers and their ability to pay for the loan. 
 
# Technologies
This application uses Python 3.7 and JupyterLab.

--- 
# Phase I: Data Preparation
The NYC housing data used for this project was sourced from https://www.kaggle.com/datasets/kaijiechen/nyc-housing-data-20032019?resource=download
Customer data was created by the members of this group to simulate real world customer data.

# Installation Guide for Phase I
Ensure Python packages are installed.
Import libraries needed to create dummy customer data and NYS housing data:

<img width="632" alt="image" src="https://user-images.githubusercontent.com/107157533/184054204-dfab917e-7428-4e65-b579-56a13dca8653.png">

 
The implementation of our data analysis includes Structured data, Semistructured data, and unstructured data. 
ETL—Extract, Transform, Load—is the process of collecting data from raw data sources and transforming that data.Transforming the data into a uniform, queryable format is really the heart of the ETL process. In this phase of developing the Loan Qualifier App,  our team applied  business rules to the data, calculated new values, filter queries, used complex join operations, aggregated rows, split columns, and implemented data validation. 
 

# Data Pre-Processing
Inspecting data - This first phase is generally part of the planning involved in creating an ETL operation.
Cleansing data - This is the process of normalizing the data within the ETL operation to ensure that the fields contain the correct values and to deal with the issue of missing values.
Transforming data - This phase involves applying functions to manipulate data into new forms for analytic purposes.
Visualizing data - This is the process of building out reports and dashboards to present the value within the data.
<img width="929" alt="image" src="https://user-images.githubusercontent.com/107157533/184055191-61f3eaed-1a52-42b5-b43a-23a92eee2afd.png">

Example of our Customer Data
<img width="1024" alt="image" src="https://user-images.githubusercontent.com/107157533/184054314-aa537a93-d557-460f-b725-7ad8c9cddf86.png">

 
# Cleaning the NYC Housing Data
We removed unnecessary decimals and irrelevant housing data such as facilities and hospitals from the dataset and only kept 1,2, and 3 family homes.
 
NYC Housing Data Pre-Cleanup
<img width="1024" alt="image" src="https://user-images.githubusercontent.com/107157533/184054348-31bedfb8-316a-4a21-b64a-b4b51498b674.png">
 
NYC Housing Data Post-Cleanup
<img width="884" alt="image" src="https://user-images.githubusercontent.com/107157533/184054469-158145a0-421a-4c80-995d-549c2d747a69.png">


# Extracting Longitude and Latitude from an API and assigning the values to the dataframe for each of the addresses: https://developer.myptv.com/Documentation/Geocoding%20API/Code%20Samples/Locations%20by%20Address.htm
<img width="995" alt="image" src="https://user-images.githubusercontent.com/107157533/184054557-53c8f101-5834-43a0-bcf1-1d82979cb645.png">



--------

# How to Run.

If we have a customer 

firstname = Amanda

Lastname = Stewart

job = Sports therapist

ssn = 437-84-6672

Looking to buy a house in Manhathan, Brooklyn or Bronx

### Steps:

1. Clone this repo https://github.com/ruejo2013/REAL_ESTATE_INVESTMENT_COMPANY_PROJECT.git
2. Navigate to the folder
3. Activate and install the required libraries and dependencies
4. Run the app following the steps below

```
  conda create -n <evn_name> python=3.7 
  conda activate <evn_name>
  git clone <link to repo>
  pip install -r requirements.txt 

  # give the right permission 
  chmod +x <file_path/main.py>

# run the app 
./main.py
 <input first name eg Amanda>
 <input ssn eg 437-84-6672>
 <input requested loan amount eg 2000000>
 <select loan duration 15 or 30>
 <accept the qualified loan amount (Y/n)>
 <select a minimum of two boroughs from the list [MANHATHAN, BRONX, BROOKLYN, QUEENS, STATEN ISLAND]>

 open and run the houses_for_sale.ipynb notebook

```

![alt text](/Resources/Images/how_to_run.png)



---
 
# Phase II: Building the Application
Installation Guide for Phase II
Ensure Python packages are installed.
Import libraries needed to perform app functions:
<img width="956" alt="image" src="https://user-images.githubusercontent.com/107157533/184054635-a970c0c0-0da7-488e-9db8-a4b17bbca3fc.png">

 
The application first prompts the user to input the customer’s first name and social security number. It will then use that information to retrieve the rest of the customer’s personal and financial data to calculate whether the customer qualifies for a loan. 
 
 
 
 
 
 
 
 
 
 
 
# Acceptance Criteria 
To qualify for a loan the customer’s credit score must be greater than 690 and debt to income ratio must be less than 35%.
 ![image](https://user-images.githubusercontent.com/107157533/184054772-894ef4a6-23a5-442a-b1ba-d9e2bd2a13e0.png)


 
# User Stories:
 
* As a lender, I want to calculate the monthly debt-to-income ratio so that we can assess the borrower's ability to repay the loan.
 
* Given that I want to calculate the monthly debt-to-income ratio, when the monthly DTI is greater than 35% then the application should raise an error.
 
 
 
  
 
 
 
Error Message:   
If the customer does meet the acceptance criteria, the message will display:
 “  Congratulations, after reviewing your  application, we are happy to inform you that your application has been  accepted.
 
If the customer does not meet the acceptance criteria, the message will display:
“"Sorry {first_name} we cannot offer you a loan, your credit score is too low".
 
Next the message will display: “Would you like to continue, Yes or No ?”
Next the message will display : Then, the application will ask “how much would you like to borrow?”
Next the message will display : “What loan term would you like to select for 15 year or 30 year?”
Next the message will display : “Would you like to accept this loan, Yes or No?
 
If the customer accepts the loan, the application will ask the user “Do you have a neighborhood preference, Manhattan, Brooklyn, Queens, Bronx, Staten Island?”
 
Next the message will display: It will then return  1-, 2-, and 3-Family Homes for sale in the boroughs selected. (Next the geomap will plot locations available) 
 
 
![image](https://user-images.githubusercontent.com/107157533/184053896-8eb18df0-012c-4ff2-bf39-29ed054a1a27.png)


---
# Project Conclusion
Below is a list of methodologies we used to achieve the project goals. 
- Created Project Management Plan
- Created a Slack channel, exchange emails
- We met via zoom regularly 
- Create internal milestones to ensure that your group is on pace. We track interim tasks using a google document. 

# Next Steps: 
- Improve Interface
- Use Real-Time Real Estate Data from a web source.
- Build a Referral Directory to Connect Local Realtors


# License
Columbia Engineering FinTech Bootcamp
