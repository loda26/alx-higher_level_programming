#!/usr/bin/node

// The first argument is the file path
// The content of the file must be read in utf-8
// If an error occurred during the reading, print the error object

const filesys = require('fs');
filesys.readFile(process.argv[2], 'utf-8',
  function (err, data) {
    if (err) {
      console.log(err);
      return;
    }
    console.log(data);
  });
