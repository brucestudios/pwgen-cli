/**
 * String Utils - A lightweight JavaScript library for common string manipulation tasks.
 */

/**
 * Removes leading and trailing whitespace from a string.
 * @param {string} str - The input string.
 * @returns {string} The trimmed string.
 */
function trim(str) {
  if (typeof str !== 'string') {
    throw new TypeError('Input must be a string');
  }
  return str.trim();
}

/**
 * Returns a new string with the first character capitalized and the rest in lowercase.
 * @param {string} str - The input string.
 * @returns {string} The capitalized string.
 */
function capitalize(str) {
  if (typeof str !== 'string') {
    throw new TypeError('Input must be a string');
  }
  if (str.length === 0) return '';
  return str[0].toUpperCase() + str.slice(1).toLowerCase();
}

/**
 * Returns the reversed string.
 * @param {string} str - The input string.
 * @returns {string} The reversed string.
 */
function reverse(str) {
  if (typeof str !== 'string') {
    throw new TypeError('Input must be a string');
  }
  return str.split('').reverse().join('');
}

/**
 * Checks if a string is a palindrome (case-insensitive).
 * @param {string} str - The input string.
 * @returns {boolean} True if the string is a palindrome, false otherwise.
 */
function isPalindrome(str) {
  if (typeof str !== 'string') {
    throw new TypeError('Input must be a string');
  }
  const cleaned = str.toLowerCase();
  const reversed = cleaned.split('').reverse().join('');
  return cleaned === reversed;
}

/**
 * Returns an object with character frequencies in the string.
 * @param {string} str - The input string.
 * @returns {Object} An object where keys are characters and values are their counts.
 */
function countChars(str) {
  if (typeof str !== 'string') {
    throw new TypeError('Input must be a string');
  }
  const counts = {};
  for (const char of str) {
    counts[char] = (counts[char] || 0) + 1;
  }
  return counts;
}

/**
 * Returns a new string with all occurrences of `find` replaced with `replace`.
 * @param {string} str - The input string.
 * @param {string} find - The substring to replace.
 * @param {string} replace - The replacement substring.
 * @returns {string} The new string with replacements.
 */
function replaceAll(str, find, replace) {
  if (typeof str !== 'string' || typeof find !== 'string' || typeof replace !== 'string') {
    throw new TypeError('All arguments must be strings');
  }
  return str.split(find).join(replace);
}

// Export functions for Node.js and browser environments
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    trim,
    capitalize,
    reverse,
    isPalindrome,
    countChars,
    replaceAll,
  };
} else {
  // Browser global
  window.StringUtils = {
    trim,
    capitalize,
    reverse,
    isPalindrome,
    countChars,
    replaceAll,
  };
}