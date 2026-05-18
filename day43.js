// The Title Case Challenge

// Write a function called titleCase(str) that takes a string of
// words and returns the string with the first letter of each word
//  capitalized, while making sure the rest of the letters in that word are
//  lowercased.

function titleCase(str) {
  str = str.toLowerCase();
  let arr = str.split(" ");
  arr.forEach((word, index) => {
    arr[index] = word.charAt(0).toUpperCase() + word.slice(1);
  });
  let titleCaseStr = arr.join(' ')

  return titleCaseStr;
}

console.log(titleCase("i wAS once A Fat chicken"));
