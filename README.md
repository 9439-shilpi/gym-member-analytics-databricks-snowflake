--------------------------------------------------
GYM ANALYTICS DASHBOARD PROJECT (SNOWFLAKE)
By Jatin Bhangotra
--------------------------------------------------

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

1) Initial member count in the dashboard: 973
2) A new record was inserted into the GYM_MEMBERS table using an INSERT statement.
3) The dashboard was refreshed.
4) Updated member count displayed in the dashboard: 974

This confirms that the dashboard reflects changes made to the underlying Snowflake tables.

ChatGPT Prompts Used:
1) How do I connect an AWS S3 object storage bucket with Snowflake?
2) How do I create an IAM role in AWS and connect it to Snowflake?
3) How do I create an external stage in Snowflake for loading data from AWS S3?
4) How do I build a Streamlit dashboard inside Snowflake?
5) How do I deploy a Streamlit application within the Snowflake environment?
6) How do I deploy a Streamlit application within the Snowflake environment?



--------------------------------------------------
Gym Member Analytics Project - By SUNANDANA SAHOO
--------------------------------------------------
 Project Overview

This project analyzes gym workout and exercise data using Databricks, PySpark, SQL, AWS S3, and Kaggle datasets. The objective is to generate meaningful fitness insights by analyzing workout performance and exercise distribution across muscle groups.

Datasets Used

 1. Gym Members Exercise Tracking Dataset
Source:
https://www.kaggle.com/datasets/valakhorasani/gym-members-exercise-dataset

**Key Columns:**
- Workout_Type
- Calories_Burned
- Age
- Gender
- Session_Duration
- Experience_Level

2. Fitness Exercises Dataset
Source:
https://www.kaggle.com/datasets/omarxadel/fitness-exercises-dataset

**Key Columns:**
- Exercise_Name
- Category / muscle_gp
- Equipment
- Rating
- Description

Project Workflow

Step 1: Data Collection
- Downloaded two fitness-related datasets from Kaggle.
- Both datasets were available in CSV format.

Step 2: AWS S3 Setup
- Created an AWS S3 bucket:
  - `gym-project-jatin-sunandana-sathwik`
- Uploaded both CSV datasets to the S3 bucket.

Step 3: Databricks Integration
- Connected Databricks to AWS S3.
- Accessed and loaded datasets directly from S3 into Spark DataFrames.

 Step 4: Data Loading Using PySpark


df1 = spark.read.csv(
    "s3://gym-project-jatin-sunandana-sathwik/Gym Exercises Dataset 2.csv",
    header=True,
    inferSchema=True
)

df2 = spark.read.csv(
    "s3://gym-project-jatin-sunandana-sathwik/gym_members_exercise_tracking.csv",
    header=True,
    inferSchema=True
)


Step 5: Data Analysis
- Explored dataset structure.
- Performed aggregations using SQL and PySpark.
- Created visualizations in Databricks.


 Objectives & Analysis

Objective 1: Average Calories Burned by Workout Type

Business Goal
Determine which workout types burn the highest average number of calories.

### SQL Query

```sql
SELECT
    Workout_Type,
    AVG(Calories_Burned) AS Avg_Calories
FROM gym_members
GROUP BY Workout_Type
ORDER BY Avg_Calories DESC;
```

### PySpark Code

```python
from pyspark.sql.functions import avg

obj1 = (
    df2.groupBy("Workout_Type")
       .agg(avg("Calories_Burned").alias("Avg_Calories"))
       .orderBy("Avg_Calories", ascending=False)
)

display(obj1)
```


Visualization
- Bar Chart
- X-Axis: Workout Type
- Y-Axis: Average Calories Burned



Objective 2: Number of Exercises per Muscle Group


 SQL Query

```sql
SELECT
    Category AS Muscle_Group,
    COUNT(*) AS Number_of_Exercises
FROM workspace.default.workout_lookup
GROUP BY Category
ORDER BY Number_of_Exercises DESC;
```


```python
obj2 = (
    df1.groupBy("muscle_gp")
       .count()
       .withColumnRenamed("count", "Number_of_Exercises")
       .orderBy("Number_of_Exercises", ascending=False)
)

display(obj2)
```

Visualization
- Bar Chart
- X-Axis: Muscle Group
- Y-Axis: Number of Exercises



 Results

### Objective 1
- Calculated average calories burned for each workout type.
- Compared workout effectiveness using aggregated metrics.

### Objective 2
- Counted exercises available for each muscle group.
- Analyzed exercise distribution across different body parts.

 Technologies Used

- Databricks
- PySpark
- SQL
- AWS S3
- Kaggle Datasets


Kaggle Datasets
       │
       ▼
     AWS S3
       │
       ▼
  Databricks
       │
       ▼
 PySpark & SQL
       │
       ▼
 Visualizations
       │
       ▼
 Business Insights

 Conclusion

This project successfully demonstrates an end-to-end analytics workflow using Databricks. Data was collected from Kaggle, stored in AWS S3, processed using PySpark and SQL, and visualized in Databricks to generate actionable fitness insights.

Key outcomes:
- Identified average calories burned by workout type.
- Determined the number of exercises available for each muscle group.
- Built visual analytics to support fitness-related decision making.


## 👩‍💻 Author

**Sunandana Sahoo**
