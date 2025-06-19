# Design - CSV uploader for CBIG [new_profile]

## elements
-   1 'Read CSV' button
    - click triggers browser to ask for file
        and calls main function 
-   1 table
-   1 error message
-   1 'Upload CSV' button

## main function
    - calls the following functions in order
        
### isCSV
    -checks that file ends in .csv if not --> throws error message.

## PapaParse error array-derived validation
https://www.papaparse.com/docs#errors
- Displays papaparse's in-built error message in the error message box.

they're in the papaparse object 'results.errors and call into 3 types, each with a code

### type 1. 'Delimiter'
        code: 'Undetectable'

### 2. type 2: 'FieldMismatch'
        code: 'tooFewFields': 
            This is when the field count in the data rows is FEWER than the field count in the header row
            MAKE A TABLE EXAMPLE

        code: 'TooManyFields
            This is when the field count in the data rows is GREATER than the field count of the header row 

            {
    ```         
        type: "FieldMismatch",
        code: "TooManyFields", 
        message: "Too many fields: expected 5 fields but parsed 7",
        row: 3
    ```
}
 
### 3. 'Quotes'
        code: 'MissingQuotes'
            With Csv files, sometimes a quote ("") is needed because an additional comma was used (as for example in the Place of Birth field
            (make 2 tables))
            In this example: Mexico City, Mexico would actually cause a field mismatch because an additional comma was entered. The work around for this to enter quotes: "Mexico City, Mexico". But, if you make a typo, forgetting a quote, this triggers this particular papaParse error.




### field mismatch

### quote errors




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



