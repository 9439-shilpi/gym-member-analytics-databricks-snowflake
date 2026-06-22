# gym-member-analytics-databricks-snowflake
Gym members insights 


GYM ANALYTICS DASHBOARD PROJECT (SNOWFLAKE) By Jatin Bhangotra

Dashboard URL:
https://app.snowflake.com/streamlit/xgikphl/vk34735/#/apps/dbnsw2p5zshlr2rok3sf

Git Repo URL:
https://github.com/9439-shilpi/gym-member-analytics-databricks-snowflake.git

Dashboard Access Information:
The dashboard is deployed as a Snowflake Streamlit application and is hosted within the Snowflake platform.
The dashboard URL cannot be accessed publicly like a normal website. To open the dashboard, a user must have:
1) A valid Snowflake account.
2) Access permissions to the Snowflake environment where the application is deployed.
3) Snowflake authentication credentials.

Because Snowflake is a private cloud data platform, users without a Snowflake account and the required permissions will not be able to access the dashboard through the provided URL.

For this reason, screenshots of the dashboard and its functionality have been included with the project submission.

Dashboard Deployment Note:
The dashboard was implemented using Snowflake Streamlit instead of the native Snowflake Dashboard feature. During project development, the Dashboards section in my Snowflake account displayed a notice stating that new dashboards could no longer be created and that the feature was being deprecated.

Therefore, Streamlit in Snowflake was used to build and deploy the Gym Analytics Dashboard. The application connects directly to Snowflake tables and visualizes the business objectives using interactive charts.

Project Overview:
This project demonstrates the integration of AWS S3 object storage, Snowflake Data Cloud, SQL analytics, and Streamlit. The goal was to create a Gym Analytics Dashboard that provides insights from gym member and exercise datasets.

Data Source:
The datasets used in this project were obtained from Kaggle. The data was downloaded in CSV format and uploaded to an AWS S3 bucket, which was then connected to Snowflake for data storage and analysis.

Datasets Used:
1) Gym Members Exercise Tracking Dataset
2) Gym Exercises Dataset

Project Data Flow:
Kaggle Dataset → AWS S3 Bucket → Snowflake Tables → SQL Analysis → Snowflake Streamlit Dashboard

AWS S3 Object Storage:
An Amazon S3 bucket named "gym-project-jatin-sunandana-sathwik" was created to serve as the project's object storage layer.
The following datasets were uploaded to the bucket:
1) Gym Exercises Dataset 2.csv
2) gym_members_exercise_tracking.csv

Snowflake Database Objects:
Database: GYM_DB
Tables:
1) GYM_MEMBERS
2) GYM_EXERCISES

Business Objective 1:
Determine the average calories burned for each workout type.

SQL Query:
SELECT WORKOUT_TYPE,
AVG(CALORIES_BURNED) AS AVG_CALORIES
FROM GYM_DB.PUBLIC.GYM_MEMBERS
GROUP BY WORKOUT_TYPE
ORDER BY AVG_CALORIES DESC;

Business Objective 2:
Determine the number of exercises available for each muscle group.

SQL Query:
SELECT C5 AS MUSCLE_GROUP,
COUNT(*) AS EXERCISE_COUNT
FROM GYM_DB.PUBLIC.GYM_EXERCISES
GROUP BY C5
ORDER BY EXERCISE_COUNT DESC;
Dashboard Update Test:
To verify that the dashboard updates correctly when data changes:

Initial member count in the dashboard: 973
A new record was inserted into the GYM_MEMBERS table using an INSERT statement.
The dashboard was refreshed.
Updated member count displayed in the dashboard: 974

This confirms that the dashboard reflects changes made to the underlying Snowflake tables.

ChatGPT Prompts Used:
1) How do I connect an AWS S3 object storage bucket with Snowflake?
2) How do I create an IAM role in AWS and connect it to Snowflake?
3) How do I create an external stage in Snowflake for loading data from AWS S3?
4) How do I build a Streamlit dashboard inside Snowflake?
5) How do I deploy a Streamlit application within the Snowflake environment?
6) How do I deploy a Streamlit application within the Snowflake environment?
