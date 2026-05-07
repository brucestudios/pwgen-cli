use clap::{Parser, ValueEnum};
use rand::distributions::{Distribution, Normal, Poisson, Exponential, Uniform};
use rand::thread_rng;
use std::fmt;

/// A command-line tool for generating random numbers with various distributions
#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
struct Args {
    /// Number of random numbers to generate (default: 1)
    #[arg(default_value_t = 1)]
    count: usize,

    /// Generate from uniform distribution (default)
    #[arg(long, short, action = clap::ArgAction::SetTrue)]
    uniform: bool,

    /// Generate from normal (Gaussian) distribution
    #[arg(long, short, action = clap::ArgAction::SetTrue)]
    normal: bool,

    /// Generate from exponential distribution
    #[arg(long, short, action = clap::ArgAction::SetTrue)]
    exponential: bool,

    /// Generate from poisson distribution (discrete)
    #[arg(long, short, action = clap::ArgAction::SetTrue)]
    poisson: bool,

    /// Mean for normal distribution (default: 0.0)
    #[arg(long, default_value_t = 0.0)]
    mean: f64,

    /// Standard deviation for normal distribution (default: 1.0)
    #[arg(long, default_value_t = 1.0)]
    stddev: f64,

    /// Lambda (rate) for exponential and poisson distributions (default: 1.0)
    #[arg(long, default_value_t = 1.0)]
    lambda: f64,

    /// Minimum value for uniform distribution (default: 0.0)
    #[arg(long, default_value_t = 0.0)]
    min: f64,

    /// Maximum value for uniform distribution (default: 1.0)
    #[arg(long, default_value_t = 1.0)]
    max: f64,

    /// Output format: one per line (default) or space-separated
    #[arg(long, value_enum, default_value_t = OutputFormat::OnePerLine)]
    format: OutputFormat,
}

#[derive(Copy, Clone, PartialEq, Eq, PartialOrd, Ord, ValueEnum, Debug)]
enum OutputFormat {
    /// One number per line
    OnePerLine,
    /// Space-separated on a single line
    SpaceSeparated,
}

fn main() {
    let args = Args::parse();

    // Determine distribution
    let mut uniform_specified = args.uniform;
    let mut normal_specified = args.normal;
    let mut exponential_specified = args.exponential;
    let mut poisson_specified = args.poisson;

    // Default to uniform if no distribution specified
    if !(uniform_specified || normal_specified || exponential_specified || poisson_specified) {
        uniform_specified = true;
    }

    let rng = &mut thread_rng();

    if uniform_specified {
        let uniform = Uniform::new_inclusive(args.min, args.max);
        let values: Vec<f64> = (0..args.count)
            .map(|_| uniform.sample(rng))
            .collect();
        print_values(&values, &args.format);
    } else if normal_specified {
        let normal = Normal::new(args.mean, args.stddev).expect("Invalid normal distribution parameters");
        let values: Vec<f64> = (0..args.count)
            .map(|_| normal.sample(rng))
            .collect();
        print_values(&values, &args.format);
    } else if exponential_specified {
        let exponential = Exponential::new(args.lambda).expect("Invalid exponential distribution parameters");
        let values: Vec<f64> = (0..args.count)
            .map(|_| exponential.sample(rng))
            .collect();
        print_values(&values, &args.format);
    } else if poisson_specified {
        let poisson = Poisson::new(args.lambda).expect("Invalid poisson distribution parameters");
        let values: Vec<u64> = (0..args.count)
            .map(|_| poisson.sample(rng))
            .collect();
        print_values(&values, &args.format);
    }
}

fn print_values<T: fmt::Display>(values: &[T>, format: &OutputFormat) {
    match format {
        OutputFormat::OnePerLine => {
            for v in values {
                println!("{}", v);
            }
        }
        OutputFormat::SpaceSeparated => {
            let line = values.iter()
                .map(|v| v.to_string())
                .collect::<Vec<_>>()
                .join(" ");
            println!("{}", line);
        }
    }
}