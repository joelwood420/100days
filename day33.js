// Write a function that takes a string and returns the first character that does not repeat anywhere in the string.
// If all characters repeat, return null


function firstNonRepeatingCharacter(str) {
    let charCount = {};
    
    for (let char of str) {
        if (charCount[char]) {
            charCount[char]++;
        } else {
            charCount[char] = 1;
        }
    }
    
    for (let char of str) {
        if (charCount[char] === 1) {
            return char;
        }
    }
    
    return null
}


console.log(firstNonRepeatingCharacter("hello")); 
console.log(firstNonRepeatingCharacter("aabbcc")); 