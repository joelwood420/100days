// Write a function that splits an array into smaller sub-arrays of a specified maximum length.

// The Requirements
// The function should take two arguments: an array and a size (integer).

// It should return a new array containing those smaller "chunks".

// If the original array can't be split evenly, the final chunk should just contain the remaining elements.

// Examples
// JavaScript
// // If you pass this:
// chunkArray([1, 2, 3, 4, 5], 2);
// // It should return:
// [[1, 2], [3, 4], [5]]

// // If you pass this:
// chunkArray([1, 2, 3, 4, 5, 6, 7, 8], 3);
// // It should return:
// [[1, 2, 3], [4, 5, 6], [7, 8]]

function chunkArr(arr, size) {
  let i = 0;
  let chunks = [];
  if (size < 1) {
    return "invalid size";
  }

  while (i < arr.length) {
    chunks.push(arr.slice(i, i + size));
    i += size;
  }

  return chunks;
}

console.log(chunkArr([1, 2, 3, 4, 5, 6, 1], 2));
