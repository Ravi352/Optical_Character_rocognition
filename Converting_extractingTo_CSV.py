# -*- coding: utf-8 -*-
"""Assignment_placement.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ms5IuUoANXumka5agcXTnJ_vlvt2A9NZ
"""

import pandas as pd

# CSV file path
csv_file = 'data.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file)

## Droping the NAN values
dff= df.dropna()

dff.reset_index(drop=True, inplace=True)
new_indexes = dff["ee"].index
new_indexes

Credits_attempted = dff["ee"][13:21]
Credit_completed = dff["ee"][21:29]

dff1 = dff[:30]
dff2 = dff[32:61]
dff3 = dff[61:98]
dff3 = dff3.replace("i>)","P")

dff1 = dff[:30]
updated_dff1 = dff1.drop([0,1,2,3,12],axis = 0)
updated_dff1.reset_index(drop=True, inplace=True)
mark1 =['P','A','A','B','A','A','A','A']
Credits_attempted1 = updated_dff1["ee"][8:16]
Credit_completed1 = updated_dff1["ee"][8:16]
course_Id_code1 = updated_dff1['ee'][:8]

dff2 = dff[32:61]
updated_dff2 = dff2.drop([41],axis = 0)
updated_dff2.reset_index(drop=True, inplace=True)
mark2 = ['P','B','A','B','A','P','A','B','A']
Credits_attempted2 = updated_dff2["ee"][9:18]
Credit_completed2=updated_dff2["ee"][9:18]
course_Id_code2 = updated_dff2['ee'][:9]

updated_dff3 = dff3.drop([61,62],axis = 0)
updated_dff3.reset_index(drop=True, inplace=True)
Credits_attempted3 = updated_dff3["ee"][18:27]
Credit_completed3=updated_dff3["ee"][18:27]
mark3 = updated_dff3["ee"][9:18]
course_Id_code3 = updated_dff3['ee'][:9]

##Separating the Course Code and Course Title separatly
Course_code1 = []
Course_title1 =[]
Course_code2 = []
Course_title2 =[]
Course_code3 = []
Course_title3 =[]
for course_id in course_Id_code1:
  if ("Spanish" in  course_id) or ("Algebra" in  course_id) or ("Basic" in  course_id) or ("Health" in  course_id) or ("Student" in  course_id) or ("Social" in  course_id):
    Course_code1.append(course_id[0:5])
    Course_title1.append(course_id[5:])
  else:
    Course_code1.append(course_id[0:6])
    Course_title1.append(course_id[6:])

for course_id in course_Id_code2:
  if ("Spanish" in  course_id) or ("Algebra" in  course_id) or ("Basic" in  course_id) or ("Health" in  course_id) or ("Student" in  course_id) or ("Social" in  course_id):
    Course_code2.append(course_id[0:5])
    Course_title2.append(course_id[5:])
  else:
    Course_code2.append(course_id[0:6])
    Course_title2.append(course_id[6:])

for course_id in course_Id_code3:
  if ("Spanish" in  course_id) or ("Algebra" in  course_id) or ("Basic" in  course_id) or ("Health" in  course_id) or ("Student" in  course_id) or ("Social" in  course_id):
    Course_code3.append(course_id[0:5])
    Course_title3.append(course_id[5:])
  else:
    Course_code3.append(course_id[0:6])
    Course_title3.append(course_id[6:])

### Making the different columns for the dataframe
headers = ["Course code",'Course title',"Grade","Credits attempted","Credit completed"]

## merge all the different coulmns in one
for i in Course_code2:
  Course_code1.append(i)
for i in Course_code3:
  Course_code1.append(i)
for i in mark2:
  mark1.append(i)
for i in mark3:
  mark1.append(i)
for i in Course_title2:
  Course_title1.append(i)
for i in Course_title3:
  Course_title1.append(i)

Credit_completed1,Credit_completed2,Credit_completed3
# Create the individual DataFrames
df1 = pd.DataFrame(Credit_completed1)
df2 = pd.DataFrame(Credit_completed2)
df3 = pd.DataFrame(Credit_completed3)

# Concatenate the DataFrames into one
merged_df = pd.concat([df1, df2, df3])

# Reset the index
Credit_completed = merged_df.reset_index(drop=True)

### Similar for Credit Attempted
# Create the individual DataFrames
df1 = pd.DataFrame(Credits_attempted1)
df2 = pd.DataFrame(Credits_attempted2)
df3 = pd.DataFrame(Credits_attempted3)

# Concatenate the DataFrames into one
merged_df = pd.concat([df1, df2, df3])

# Reset the index
Credits_attempted = merged_df.reset_index(drop=True)

# Create the individual DataFrames
df1 = pd.DataFrame(Credits_attempted1)
df2 = pd.DataFrame(Credits_attempted2)
df3 = pd.DataFrame(Credits_attempted3)

# Concatenate the DataFrames into one
merged_df = pd.concat([df1, df2, df3])

# Reset the index
Credits_attempted = merged_df.reset_index(drop=True)

# Display the merged DataFrame
print(len(Credits_attempted["ee"]))

"""Adding First dataframe"""

df2 = pd.DataFrame(columns=headers)
# new_data = pd.Series([course_Id_code1], index=df.columns)
# df2["Course code"] = course_Id_code1
df2["Course title"] = Course_title1
df3 = pd.DataFrame(columns=headers)
df3["Course code"] =Course_code1
df3["Course title"] = Course_title1
df3['Grade'] = mark1
df3['Credits attempted'] = Credits_attempted
df3['Credit completed'] = Credit_completed
# Create a DataFrame
df = pd.DataFrame(df3)

# Convert DataFrame to CSV
df.to_csv('extracted_data.csv', index=False)