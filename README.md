# CS506-Commercial-Company-Displacement
Mayor’s Office of Economic Development: Commercial Company Displacement

Team Members: Jianghong Man, Xiaoyan Su, Yirong Zhang

## File Description
### Datasets
In this project, we first tried dataset from provided by our client: assessors database. We downloaded the databases for 2018 and 2019 (Dataset is free for download at this website: https://data.boston.gov/dataset). Due to some limitations in the first dataset, we then used dataset from Reference USA for our data visualization and prediction.
* 
In the folder Cleaned Data 2018, we have two .py files.
•	Data Cleaning 1.py: Compile addresses and parcel ID from the assessors database of all commercial and mixed use parcels (LU: C and RC)
•	Data Cleaning 2.py: 
o	Narrowed geographical regions in scope, focus on the following neighborhoods: Roxbury, Mattapan, Dorchester and East Boston
o	Capture following attributes on all commercial and mixed use properties
	owner, owner address, street, city, state, zip
	Assessed building value, total value, tax
	Parcel land area, year built, year remodeled, gross area
