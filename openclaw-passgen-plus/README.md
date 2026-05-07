# OpenClaw Password Generator Plus

An advanced CLI tool for generating secure, customizable passwords with multiple entropy sources and validation features.

## Features

- 🔐 Generate cryptographically secure passwords
- 🎯 Customizable character sets (uppercase, lowercase, numbers, symbols)
- 📊 Entropy calculation and strength scoring
- 🔍 Pattern avoidance (no sequential chars, repeated patterns)
- 💾 Export to multiple formats (txt, json, csv)
- 🔄 Batch generation with deduplication
- 📱 QR code output for mobile transfer
- 🌐 Multiple language support (i18n ready)
- ⚡ Lightning fast generation (10K+ passwords/sec)
- 🛡️ Security auditing and breach checking (local)
- 🎨 Beautiful terminal output with colors and progress bars

## Installation

```bash
# Install via npm
npm install -g @brucestudios/passgen-plus

# Or install via Homebrew (macOS/Linux)
brew install brucestudios/tools/passgen-plus

# Or install via pip (Python version available)
pip install passgen-plus

# Or download binary from releases
curl -L https://github.com/brucestudios/openclaw-passgen-plus/releases/latest/download/passgen-plus-linux-amd64 -o passgen-plus
chmod +x passgen-plus
sudo mv passgen-plus /usr/local/bin/
```

## Usage

### Basic Password Generation

```bash
# Generate a single 16-character password
passgen-plus

# Generate a 32-character password
passgen-plus -l 32

# Generate 5 passwords of 20 characters each
passgen-plus -l 20 -c 5
```

### Advanced Options

```bash
# Exclude ambiguous characters (0, O, l, 1, etc.)
passgen-plus --exclude-ambiguous

# Include only specific character types
passgen-plus --letters-only --numbers --symbols "!@#"

# Generate pronounceable passwords (easier to remember)
passgen-plus --pronounceable -l 16

# Generate PIN codes (numbers only)
passgen-plus --pin -l 6

# Generate memorable passphrases
passgen-plus --passphrase -w 4  # 4-word passphrase

# Batch generation with export
passgen-plus -l 24 -c 100 --export json --output passwords.json

# Generate QR codes for mobile transfer
passgen-plus --qr -l 24

# Strength analysis of existing password
passgen-plus --check "MyP@ssw0rd123!"
```

### Configuration

Create a `.passgen-plusrc` file in your home directory:

```json
{
  "length": 20,
  "count": 1,
  "characterSets": {
    "uppercase": true,
    "lowercase": true,
    "numbers": true,
    "symbols": true
  },
  "excludeAmbiguous": true,
  "excludeSimilar": true,
  "avoidPatterns": true,
  "pronounceable": false,
  "exportFormat": "txt"
}
```

## Security Features

### Entropy Calculation
Each generated password includes an entropy score (bits) and crack time estimates based on various attack scenarios:
- Online attack (100 guesses/sec)
- Offline attack (1B guesses/sec)
- Massive cracking array (100B guesses/sec)
- Nation-state level (1T guesses/sec)

### Pattern Avoidance
The tool actively avoids:
- Sequential characters (abc, 123, qwerty)
- Repeated characters (aaa, 111)
- Keyboard patterns (qaz, plm)
- Common substitutions (p@ssw0rd)
- Personal information patterns

### Local Breach Checking
When enabled, checks generated passwords against a local database of common weak passwords (rockyou.txt, haveibeenpwned top 1M, etc.) without transmitting data externally.

## Development

### Building from Source

```bash
# Clone the repository
git clone https://github.com/brucestudios/openclaw-passgen-plus.git
cd openclaw-passgen-plus

# Install dependencies
npm install

# Build for production
npm run build

# Run tests
npm test

# Generate documentation
npm run docs
```

### Project Structure

```
openclaw-passgen-plus/
├── src/                    # Source code
│   ├── core/               # Password generation algorithms
│   ├── cli/                # Command-line interface
│   ├── utils/              # Utility functions
│   ├── i18n/               # Internationalization
│   └── security/           # Security auditing modules
├── tests/                  # Test suite
├── docs/                   # Documentation
├── examples/               # Usage examples
└── templates/              # Template files
```

## Algorithms

### Password Generation
1. **Character Pool Construction**: Build pool based on selected character sets
2. **Entropy Validation**: Ensure minimum entropy threshold is met
3. **Pattern Screening**: Filter out generated passwords containing weak patterns
4. **Bias Elimination**: Use cryptographically secure random selection (no modulo bias)
5. **Post-processing**: Apply final transformations (if requested)

### Strength Scoring
Based on NIST SP 800-63B and OWASP guidelines:
- Length score (0-40 points)
- Character variety score (0-30 points)
- Entropy score (0-20 points)
- Pattern penalty (0-20 points deduction)
- Dictionary check (0-10 points deduction)

Total score: 0-100+ (higher is stronger)

## API Usage

The tool can also be used as a library:

```javascript
const { generatePassword, checkStrength } = require('@brucestudios/passgen-plus');

// Generate a password
const password = generatePassword({
  length: 20,
  uppercase: true,
  lowercase: true,
  numbers: true,
  symbols: true,
  excludeAmbiguous: true,
  avoidPatterns: true
});

// Check strength of existing password
const strength = checkStrength("MySecureP@ssw0rd!");
console.log(`Strength: ${strength.score}/100 (${strength.entropy} bits)`);
```

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Security Policy

Please see our [Security Policy](SECURITY.md) for how we handle security vulnerabilities.

## Acknowledgments

- Inspired by xkcd #936 (Password Strength)
- Uses cryptographically secure random number generators
- Based on password generation best practices from NIST and OWASP
- Built with love by the OpenClaw community