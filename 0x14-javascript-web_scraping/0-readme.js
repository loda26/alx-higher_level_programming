#!/usr/bin/node

// The first argument is the file path
// The content of the file must be read in utf-8
// If an error occurred during the reading, print the error object

const file_sys = require('fs');
const file_path = process.argv[2];
const file_code = 'utf8';

file_sys.readFile(file_path, file_code,
    function (err, data) {
        if (err) {
            console.log(err);
            return;
        }
        console.log(data);
    });
