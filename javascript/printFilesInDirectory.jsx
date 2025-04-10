// In the JavaScript file, write a program to first create a file in the current directory with the name newfile.txt filled with any content.
// Then, using exec, print to the console all the files in the current directory so that they are in the following format: FILENAME, FILENAME,

// Example Output

// file.js, helloworld.txt, abc.txt

const fs = require('fs');
const { exec } = require('child_process');

fs.writeFileSync('newfile.txt', 'Hello, this is a new file.', 'utf8');

exec(process.platform === 'win32' ? 'dir /b' : 'ls', (err, stdout, stderr) => {
  if (err) {
    console.error(`Error: ${err.message}`);
    return;
  }

  const files = stdout.split('\n').filter(file => file.trim() !== '');
  console.log(files.join(', '));
});
