const btn_upload = document.getElementById('btn-upload-csv');
const fileInput = document.getElementById('file-input');

function csvInstructions(){
    const getTxt = document.getElementById('text-display').innerHTML = 
    'Use this table as a reference: <br>Place your headers in the' +
    ' order shown.';
}

csvInstructions()

function createStaticTable() {
    
    console.log('creating static table');
    const tableContainer = document.getElementById('table-container');
    
    //create wrapper
    const wrapper = document.createElement('table');
    wrapper.className = 'csv-table-wrapper';
    
    //create table
    const table = document.createElement('table');
    table.className = 'csv-table';

    // Create header
    const thead = document.createElement('thead');
    const headerRow = document.createElement('tr');
    const headers = ['Date of Birth', 'Sex', 'Site', 'Project', 'First Name',
         'Middle Name', 'Family Name', 'Birth Place', 'Study ID'];
    
    headers.forEach(headerText => {
        const th = document.createElement('th');
        th.textContent = headerText;
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);
    
    // Create body with sample data
    const tbody = document.createElement('tbody');
    const sampleData = [
        ['1990-05-15', 'M', 'Site A', 'Sample Project A', 'John', 'Michael', 'Smith', 'New York', 'SAMPLE_ID_100101_P'],
        ['1985-12-03', 'F', 'Site B', 'Sample Project B', 'Sarah', 'Ann', 'Johnson', 'Los Angeles', 'SAMPLE_ID_100102_P'],
        ['1992-08-22', 'M', 'Site C', 'Sample Project C', 'David', 'James', 'Brown', 'Chicago', 'SAMPLE_ID_100103_P']
    ];
    
    sampleData.forEach(rowData => {
        const row = document.createElement('tr');
        rowData.forEach(cellData => {
            const td = document.createElement('td');
            td.textContent = cellData;
            row.appendChild(td);
        });
        tbody.appendChild(row);
    });
    
    table.appendChild(tbody);

    //Clear container and add table
    wrapper.appendChild(table);
    tableContainer.innerHTML = '';
    tableContainer.appendChild(wrapper);
}

createStaticTable()


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
* Validates the CSV in several ways and displays it in a table 
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
            if (!replaceHeaders(results)) return;
            //if (!reorderColumns(results)) return;
            // //validateDateFormat()
            createTable(results);
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
    console.log('handleParseErrors')
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
    console.log('is CSV : The file extension is .csv');
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
        console.log('hasData : Your CSV contains data')
        return true;
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
            + emptyFields.join(', ') + '<br>AllFields: ' 
            + fieldNames.join(', ');
            showError(errorMsg);
            return false
        }

    const fieldCount = Object.keys(results.data[0]).length; 
    if (fieldCount !== 9) {
        let errorMsg = 'Your .csv file has ' 
        + fieldCount + ' fields instead of 9:<br>' 
        showError(errorMsg);
        return false;
        }
    console.log('checkFields');
    hideError();
    return true;
}

 /**
 * Replaces headers with the required headers
 *@param {parsedData}
 *@returns {}
 */   

function replaceHeaders(results) {

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
        'Study ID': ['studyid', 'id','i.d', 'i.d.', 'study id', 'external study id'],
        };

  
    const headers = results.meta.fields; 
    let errorMsgs = [];

    const headerMap = {};
    
    headers.forEach((headerName, index) => {
        const lowerHeader = headerName.toLowerCase();
        
        const standardName = Object.keys(headerMappings).find(key => 
            headerMappings[key].some(variation => variation === lowerHeader)
        );
        
        if (standardName) {
            headerMap[headerName] = standardName;
            headers[index] = standardName;
            console.log(`Replaced "${headerName}" with "${standardName}"`);
        } else {
            // Concatenate instead of overwrite
            errorMsgs += `CSV field "${headerName}" is not in our mapping list\n`;
        }
    });

    results.data = results.data.map(row =>{
        const newRow = {};
        Object.keys(row).forEach(oldKey => {
            const newKey = headerMap[oldKey] || oldKey;
            newRow[newKey] = row[oldKey];
        });
        return newRow;
    });

    if (errorMsgs.length > 0) {
        console.error('Header mapping errors:\n' + errorMsgs);
        return false;
    }
    results.data = results.data.map(row => {
        const newRow = {};
        Object.keys(row).forEach(oldKey => {
            const newKey = headerMap[oldKey] || oldKey;
            newRow[newKey] = row[oldKey];
        });
        return newRow;
    });

    return results;
}


// function reorderColumns(results) {
//     newKeyOrder = [
//         'Date of Birth', 'Sex', 'Site', 'Project', 'First Name', 'Middle Name', 'Family Name', 'Birth Place','Study ID' 
//       ]
    
//     //outer loop
//     const reorderedObj = results.data.map(obj => {
//         const newObj = {};
        
//         // inner loop
//         newKeyOrder.forEach(key => {
//             const actualKey = Object.keys(obj).find(objKey => objKey === key);
//             if
//             newObj[key] = obj[key];
//         });
        
//         return newObj;
//     });
    
//     // Update meta fields to match new order
//     results.data = reorderedObj;
//     //update the meta.fields part of papaParse
//     results.meta.fields = newKeyOrder;
    
//     console.log('reorderColumns : your columns have been put in the right order')
//     return results;
// }

/**
 * Creates an HTML table from the parsed CSV data
 * @param {Array} - data portion of the papaParse object parsedData
 * @returns {void}
 */

function createTable(results) {
    console.log('createTable called with:', results);
    console.log('results.data', results.data);
    
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
    const headers = Object.keys(results.data[0]);
    headers.forEach(header => {
        const th = document.createElement('th');
        th.textContent = header;
        headerRow.appendChild(th);
    });
    
    thead.appendChild(headerRow);
    table.appendChild(thead);
    
    // Create body
    const tbody = document.createElement('tbody');
    results.data.forEach(row => {
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