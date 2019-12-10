# CS506-Commercial-Company-Displacement
Mayor’s Office of Economic Development: Commercial Company Displacement

Team Members: Jianghong Man, Xiaoyan Su, Yirong Zhang

## File Description
### Assessors Datasets
In this project, we first tried dataset from provided by our client: assessors database. We downloaded the databases for 2018 and 2019 (Dataset is free for download at this website: https://data.boston.gov/dataset). 

* Parcels_2018.csv (assessors database in 2018)
* fy19fullpropassess.csv (assessors database in 2019)

### Assessors Database Preprocessing
Folder: Cleaned Data 2018
* Data Cleaning 1.py: Compile addresses and parcel ID from the assessors database of all commercial and mixed use parcels (LU: C and RC)
* Data Cleaning 2.py: Narrowed geographical regions in scope, focus on the following neighborhoods: Roxbury, Mattapan, Dorchester and East Boston; Capture following attributes on all commercial and mixed use properties:
   
   * owner, owner address, street, city, state, zip
   
   * Assessed building value, total value, tax
   
   * Parcel land area, year built, year remodeled, gross area

Folder: Cleand Data 2019
* Data Preprocessing.ipynb: Also done the same cleaning job as the above two .py files.

### Reference USA Datasets (Folder: Reference USA Data)
Due to some limitations in the first dataset, we then used dataset from Reference USA for our data visualization and prediction. Original and cleaned databases all located in Reference USA Data folder.

* Combined Closed Business.csv (only includes closed businesses from Reference USA)
* new all business.csv (all businesses from Reference USA)
* new_all_business_cleaned.csv (cleaned data with specific "Rent Expenses", "Square Footage", "Rent sq ft" attributes)
* crime_with_area_time.csv （crime incidences in areas of interest）
* clean_ethnicity.csv (cleaned data to determine ethnicity trends of closed business owners)

### Reference USA Database Preprocessing and Visualization (Folder: Data Visualization Code)
* Rent sq ft cleaning code.py
The code in this file handles data cleaning process and calculation based on the original dataset "new all business.csv". The resulting dataset after cleaning is saved as "new_all_business_cleaned.csv".



