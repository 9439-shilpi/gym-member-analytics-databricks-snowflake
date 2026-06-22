# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

st.title("Gym Analytics Dashboard")

session = get_active_session()

# Business Objective 1
st.header("Business Objective 1")
st.write("Average Calories Burned by Workout Type")

query1 = """
SELECT WORKOUT_TYPE,
       AVG(CALORIES_BURNED) AS AVG_CALORIES
FROM GYM_DB.PUBLIC.GYM_MEMBERS
GROUP BY WORKOUT_TYPE
ORDER BY AVG_CALORIES DESC
"""

df1 = session.sql(query1).to_pandas()
st.bar_chart(df1.set_index("WORKOUT_TYPE"))

# Business Objective 2
st.header("Business Objective 2")
st.write("Number of Exercises per Muscle Group")

query2 = """
SELECT C5 AS MUSCLE_GROUP,
       COUNT(*) AS EXERCISE_COUNT
FROM GYM_DB.PUBLIC.GYM_EXERCISES
GROUP BY C5
ORDER BY EXERCISE_COUNT DESC
"""

df2 = session.sql(query2).to_pandas()
st.bar_chart(df2.set_index("MUSCLE_GROUP"))

# Summary KPIs
st.header("Dataset Summary")

members = session.sql("""
SELECT COUNT(*) AS CNT
FROM GYM_DB.PUBLIC.GYM_MEMBERS
""").to_pandas()

exercises = session.sql("""
SELECT COUNT(*) AS CNT
FROM GYM_DB.PUBLIC.GYM_EXERCISES
""").to_pandas()

st.metric("Total Members", int(members.iloc[0]["CNT"]))
st.metric("Total Exercises", int(exercises.iloc[0]["CNT"]))