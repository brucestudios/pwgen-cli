# UUID Smith

A comprehensive UUID/GUID utility toolkit with both programmatic API and command-line interface.

## Features

- Generate UUIDs (versions 1 and 4)
- Validate UUID strings
- Get UUID version information
- Format UUIDs (uppercase, lowercase, URN)
- Easy-to-use CLI

## Installation

```bash
npm install @brucestudios/uuidsmith
```

## Usage

### Programmatic API

```javascript
const { generate, generateV1, generateV4, validate, getVersion, format } = require('@brucestudios/uuidsmith');

// Generate a random UUID v4
const uuidv4 = generate();
// or
const uuidv4 = generateV4();

// Generate a UUID v1
const uuidv1 = generateV1();

// Validate a UUID
const isValid = validate(uuidv4);

// Get UUID version
const version = getVersion(uuidv4);

// Format UUID
const uppercase = format(uuidv4, { uppercase: true });
const urn = format(uuidv4, { urn: true });
```

### Command Line Interface

```bash
# Generate a single UUID v4 (default)
uuidsmith generate

# Generate multiple UUIDs
uuidsmith generate -c 5

# Generate a UUID v1
uuidsmith generate -v 1

# Generate uppercase UUIDs
uuidsmith generate -u

# Generate UUID with URN prefix
uuidsmith generate --urn

# Validate a UUID
uuidsmith validate 123e4567-e89b-12d3-a456-426614174000

# Get information about a UUID
uuidsmith info 123e4567-e89b-12d3-a456-426614174000
```

## API Reference

### `generate(version = 4)`
Generate a random UUID of the specified version (1 or 4).

### `generateV1()`
Generate a random UUID version 1.

### `generateV4()`
Generate a random UUID version 4.

### `validate(uuid)`
Validate a UUID string. Returns `true` if valid, `false` otherwise.

### `getVersion(uuid)`
Get the version of a UUID string (1-5). Returns `null` if invalid.

### `format(uuid, options)`
Format a UUID string.
Options:
- `uppercase`: boolean, output in uppercase
- `lowercase`: boolean, output in lowercase (default)
- `urn`: boolean, prefix with 'urn:uuid:'

## Running Tests

```bash
npm test
```

## License

MIT