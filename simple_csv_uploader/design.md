# Design - CSV uploader for CBIG [new_profile]

## elements
-   1 upload button
    - click triggers browser to ask for file
        and calls main function 
-   1 table
-   1 error message


## main function
    - calls the following functions in order
        
### isCSV
    -checks that file ends in .csv
### validateCSVstructure
    - 
    - 
### calls FileReader 
    - populates a DOM File element with csv string
### calls papaParse. csv is thereby "parsed" into an array of objects. Each row is an object. For ex:
    parsedData = [
        {'Date of Birth': '2020/02/02', '2020/03/03', '1990/06/01'}
    ];

### checkNumberofFields
        - check that fields = 9
### hasData
    - checks that .data part of papaParse obj is > 0
### hasHeaders
    - checks that .meta.fields part of papaParse obj is >0
### replaceHeaders
    - replaces the given headers with standard headers
### reorderColumns
    - reorders the columns into desired order for ingestion
### isValidDateFormat
    - transforms all date formats to a standard format
### createTable
    - table features:
        - frozen header
        - frozen row numbers
        - 5 rows deep, scrollable vertical + horizontal
### getEmptycells
    - checks for empty cells, and tells where they are



