# randgen

A command-line tool for generating random numbers with various distributions.

## Features

- Generate random numbers from uniform, normal (Gaussian), exponential, and Poisson distributions
- Configurable parameters for each distribution
- Flexible output formats (one per line or space-separated)
- Simple and intuitive CLI interface

## Installation

### From Cargo

```bash
cargo install randgen-cli
```

### From Source

```bash
git clone https://github.com/brucestudios/randgen-cli.git
cd randgen-cli
cargo install --path .
```

## Usage

### Basic Examples

Generate a single uniform random number between 0 and 1 (default):

```bash
randgen
```

Generate 5 uniform random numbers between 10 and 20:

```bash
randgen --count 5 --min 10 --max 20
```

Generate 3 normally distributed numbers with mean 5 and standard deviation 2:

```bash
randgen --normal --mean 5 --stddev 2 --count 3
```

Generate 4 exponentially distributed numbers with rate 0.5:

```bash
randgen --exponential --lambda 0.5 --count 4
```

Generate 2 Poisson distributed numbers with lambda 3:

```bash
randgen --poisson --lambda 3 --count 2
```

### Output Format

By default, numbers are printed one per line. To get space-separated output on a single line:

```bash
randgen --count 3 --format space-separated
```

## Building from Source

Requires Rust and Cargo. Then:

```bash
cargo build --release
```

The binary will be available at `target/release/randgen`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.