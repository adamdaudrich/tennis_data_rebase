const btn_upload = document.getElementById('btn-upload-csv');
const fileInput = document.getElementById('file-input');


// Hide error

btn_upload.addEventListener('click', function(){
    fileInput.click();
});
fileInput.addEventListener('change', handleFileUpload);

function showError(errorMsg){
    document.getElementById('error-container').innerHTML = errorMsg;
        document.getElementById('error-container').style.display = 'block';
}

function hideError(){
    document.getElementById('error-container').style.display = 'none';
}

/**  
 * Main Function
* Processes an uploaded CSV and displays it in a table 
*
* @param {e} - event 
* @returns {void} - 
*/

function handleFileUpload(e) {
    const file = e.target.files[0]; 
    if (!isCSV(file.name)) return;

    Papa.parse(file, { 
        header: true, // returns an array of arrays
        skipEmptyLines: true,
        delimiter:',',
        trimHeaders: true,
        complete: function(results){
            //use papaParse to handle errors
            handleParseErrors(results);
            //handle errors that papaParse doesn't handle 
            if (!hasData(results)) return;
            if (!checkFields(results))return; 
            replaceHeaders(parsedData, REQUIRED_HEADERS);
            // reorderColumns(results);
            // //validateDateFormat()
            // createTable(results);
            // getEmptyCells(results);
            // //processData()
            //for (row in parsedData){
            //sendToRidasSubmithandler()
        }
    });
} 

function handleParseErrors(results) {
    if (results.errors.length === 0) {
        return false; // No errors, continue processing
    }

    // Group errors by type
    const delimiterErrors = results.errors.filter(err => err.type === 'Delimiter');
    const fieldMismatchErrors = results.errors.filter(err => err.type === 'FieldMismatch');
    const quoteErrors = results.errors.filter(err => err.type === 'Quotes');

    //when field count in results.data is less than that of results.meta.fields
    const tooFewFieldsErrors = fieldMismatchErrors.filter(err => err.code === 'TooFewFields');

    //when the field count in results.data is more than that of results.meta.fields
    const tooManyFieldsErrors = fieldMismatchErrors.filter(err => err.code === 'TooManyFields');

    // when a quote is started but not finished ex: ("Mexico city, Mexico)
    const missingQuotesErrors = quoteErrors.filter(err => err.code === 'MissingQuotes');


    const undetectableDelimiterErrors = delimiterErrors.filter(err => err.code === 'UndetectableDelimiter');

    let errorMessage = '';
    let errorDetails = [];

    // Handle delimiter errors
    if (delimiterErrors.length > 0) {
        errorMessage += `${delimiterErrors.length} delimiter issue(s) found. `;
        delimiterErrors.forEach(err => {
            errorDetails.push(`Delimiter issue: ${err.message}`);
        });
    }

    // Handle field mismatch errors
    if (fieldMismatchErrors.length > 0) {
        errorMessage += `${fieldMismatchErrors.length} field mismatch error(s) found. `;
        
        // Show specific field mismatch details with row numbers
        fieldMismatchErrors.forEach(err => {
            const rowNumber = err.row !== undefined ? err.row + 1 : 'unknown';
            errorDetails.push(`Row ${rowNumber}: ${err.message}`);
        });
    }

    // Handle quote errors
    if (quoteErrors.length > 0) {
        errorMessage += `${quoteErrors.length} quote formatting error(s) found. `;
        quoteErrors.forEach(err => {
            const rowNumber = err.row !== undefined ? err.row + 1 : 'unknown';
            errorDetails.push(`Row ${rowNumber}: ${err.message}`);
        });
    }

    // Create comprehensive error message
    let fullErrorMessage = `Total errors: ${results.errors.length}<br>${errorMessage}`;
    
    // Add suggestions based on error types
    if (delimiterErrors.length > 0) {
        fullErrorMessage += '<br>• Check that your file uses comma separators';
    }
    if (fieldMismatchErrors.length > 0) {
        fullErrorMessage += '<br>• Verify all rows have the same number of fields';
        fullErrorMessage += '<br>• Check for extra commas or missing data';
    }
    if (quoteErrors.length > 0) {
        fullErrorMessage += '<br>• Check for unmatched quotes in your data';
        fullErrorMessage += '<br>• Ensure quoted fields are properly escaped';
    }

    // Add detailed error list (limit to first 10 to avoid overwhelming)
    if (errorDetails.length > 0) {
        fullErrorMessage += '<br><br>Error details:';
        const limitedDetails = errorDetails.slice(0, 10);
        limitedDetails.forEach(detail => {
            fullErrorMessage += `<br>• ${detail}`;
        });
        
        if (errorDetails.length > 10) {
            fullErrorMessage += `<br>• ...and ${errorDetails.length - 10} more errors`;
        }
    }

    // Display the error
    showError(fullErrorMessage);
    
    return true; // Errors found, stop processing
}

/** 
* Checks for a .csv file
* @param {file} 
* @returns {bool}
*/
function isCSV(file){     
    // file also needs to have an extension   
    if (!file.toLowerCase().endsWith('.csv')) {
        const errorMsg = 'The file extension is not .csv';
        console.error(errorMsg);
        showError(errorMsg);
        return false;
    }
    console.log('The file extension is .csv');
    hideError();
    return true;
}

/**
* Checks that number of fields in the submitted .CSV is correct
* @param {Object} - parsedData
* @returns {boolean} - True if field count is correct, false other
*/

function hasData(results) {
    if (!results.data || results.data.length === 0) {
        const errorMsg1 = 'No data found in CSV';
        showError(errorMsg1);
        return false;
    }
        console.log('Your CSV contains data')
        return true;
}   

function getEmptyCells(parsedData) {
    const emptyCells = [];
    parsedData.data.forEach((row, rowIndex) => {
        Object.values(row).forEach((cellValue, colIndex) => {
            if (!cellValue || cellValue.toString().trim() === '') {
                emptyCells.push({ row: rowIndex + 1, col: colIndex });
            }
        });
    });
    console.log('You have empty data in', emptyCells);
    return emptyCells;
}

function checkFields(results){

    const fieldNames = results.meta.fields;
    const emptyFields = [];


    fieldNames.forEach((field, index) => {
        if (field === ''){
            emptyFields.push(index + 1);
        }
    });
    
    if (emptyFields.length > 0){
        let errorMsg = 'Missing values at field numbers: ' 
        + emptyFields.join(', ') + '<br>AllFields: ' + fieldNames.join(', ');

    const fieldCount = Object.keys(results.data[0]).length; 
    if (fieldCount !== 9) {
        errorMsg = 'Your .csv file has ' 
        + fieldCount + ' fields instead of 9:<br>' 
        + fieldNames;
        showError(errorMsg);
        return false;
        }
    console.log('Field count is correct');
    hideError();
    return true;
}


 /**
 * Replaces headers with the required headers
 *@param {parsedData}
 *@returns {}
 */   

function replaceHeaders(parsedData) {

    const headerMappings = {
        'Date of Birth': ['date of birth', 'date-of-birth', 'birthday', 
            'birth day','birth-day', 'birthdate', 'dob', 'd.o.b', 'birth', 
            'bornday', 'born'],
        'Sex': ['sex', 'sexe', 'sexy', 'sx', 'gender', 'genderid', 
            'gender id'],
        'Site': ['site', 'sites', ],
        'Project': ['project', 'proj', 'prj'],
        'First Name': ['firstname', 'first name', 'name', 'given name'],
        'Middle Name': ['middlename', 'middle-name', 'middle name'],
        'Family Name': ['family name', 'familyname', 'lastname', 'last name'],
        'Birth Place': ['place of birth', 'location of birth', 'birth place', 
            'city of birth', 'birth city'],
        'Study ID': ['studyid', 'id','i.d', 'i.d.', 'study id'],
        };

    // Get the headers (assuming first row or meta.fields)
    const headers = parsedData.meta.fields; // or parsedData.data[0] if no header row
    
    headers.forEach((headerName, index) => {
        const lowerHeader = headerName.toLowerCase();
        
        //so.find is actually an inner loop that uses the key and associated 
        // values
        // (headerMappings[key] of that (outer loop)iteration of the object 
        // to see if .some (or any) of the variations match the key when put 
        // to lower case 
        const standardName = Object.keys(headerMappings).find(key => 
            headerMappings[key].some(variation => variation === lowerHeader)
        );
        
        if (standardName) {
            headers[index] = standardName;
        }
    });
}

function reorderColumns(parsedData, newKeyOrder) {
    newKeyOrder = [
        'DOB', 'Sex', 'Site', 'Project', 'First Name', 'Middle Name', 'Family Name', 'Birth Place','Study ID' 
      ]
    
    const reorderedObj = parsedData.data.map(obj => {
        const newObj = {};
        
        // Build new row in the desired order
        newKeyOrder.forEach(key => {
            newObj[key] = obj[key];
        });
        
        return newObj;
    });
    
    // Update meta fields to match new order
    parsedData.data = reorderedObj;
    //update the meta.fields part of papaParse
    parsedData.meta.fields = newKeyOrder;
    
    return parsedData;
}

/**
 * Creates an HTML table from the parsed CSV data
 * @param {Array} - data portion of the papaParse object parsedData
 * @returns {void}
 */

function createTable(parsedData) {
    console.log('createTable called with:', parsedData);
    console.log('parsedData.data', parsedData.data);
    
    const tableContainer = document.getElementById('table-container');
    
    //create wrapper
    const wrapper = document.createElement('div');
    wrapper.className = 'csv-table-wrapper';
    
    // create table
    const table = document.createElement('table');
    table.className = 'csv-table';

    // create header
    const thead = document.createElement('thead');
    const headerRow = document.createElement('tr');
    
    // Use the keys from first object as headers
    const headers = Object.keys(parsedData.data[0]);
    headers.forEach(header => {
        const th = document.createElement('th');
        th.textContent = header;
        headerRow.appendChild(th);
    });
    
    thead.appendChild(headerRow);
    table.appendChild(thead);
    
    // Create body
    const tbody = document.createElement('tbody');
    parsedData.data.forEach(row => {
        const tr = document.createElement('tr');
        headers.forEach(header => {
            const td = document.createElement('td');
            td.textContent = row[header] || '';
            tr.appendChild(td);
        });
        tbody.appendChild(tr);
    });
    
    table.appendChild(tbody);
    
    // Clear container and add table
    wrapper.appendChild(table);
    tableContainer.innerHTML = '';
    tableContainer.appendChild(wrapper);
}


// /** Processes validated CSV data and sends it to the database
// * @param {Object}- Papa Parse .data property
// * @returns {void}
// */

// function uploadCSV() {
//     console.log('Processing validated data:', parsedData);
//     const rows = parsedData.data;
//     rows.forEach((row, index) => {
//         console.log(`Row ${index}:`, row);
//         // TODO: Send to database
//     });

//     return true;
