# String Utils

A lightweight JavaScript library for common string manipulation tasks.

## Features

- Trim whitespace
- Capitalize first letter
- Reverse string
- Check palindrome
- Count characters
- Replace all occurrences
- And more!

## Installation

```bash
npm install string-utils
```

## Usage

```javascript
const { trim, capitalize, reverse, isPalindrome, countChars, replaceAll } = require('string-utils');

// trim
trim('  hello  '); // 'hello'

// capitalize
capitalize('hello'); // 'Hello'

// reverse
reverse('hello'); // 'olleh'

// palindrome check
isPalindrome('racecar'); // true
isPalindrome('hello'); // false

// count characters
countChars('hello'); // { h:1, e:1, l:2, o:1 }

// replace all
replaceAll('hello world', 'l', 'x'); // 'hexxo worxd'
```

## API

### trim(str)
Removes leading and trailing whitespace.

### capitalize(str)
Returns a new string with the first character capitalized and the rest in lowercase.

### reverse(str)
Returns the reversed string.

### isPalindrome(str)
Returns true if the string reads the same forwards and backwards (case-insensitive, ignores non-alphanumeric? Actually we'll keep simple).

### countChars(str)
Returns an object with character frequencies.

### replaceAll(str, find, replace)
Returns a new string with all occurrences of `find` replaced with `replace`.

## License

ISC