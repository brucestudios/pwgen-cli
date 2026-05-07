#!/usr/bin/env node

import { Command } from 'commander';
import { generatePassword } from '../core/passwordGenerator';
import { checkPasswordStrength } from '../utils/entropy';
import { QRCodeTerminal } from 'qrcode-terminal';
import chalk from 'chalk';
import { promises as fs } from 'fs';
import path from 'path';

const program = new Command();

program
  .name('passgen-plus')
  .description('Advanced CLI tool for generating secure, customizable passwords')
  .version('1.0.0');

program
  .option('-l, --length <number>', 'Password length', parseInt)
  .option('-c, --count <number>', 'Number of passwords to generate', parseInt)
  .option('--uppercase', 'Include uppercase letters', true)
  .option('--lowercase', 'Include lowercase letters', true)
  .option('--numbers', 'Include numbers', true)
  .option('--symbols', 'Include symbols', true)
  .option('--exclude-ambiguous', 'Exclude ambiguous characters (0, O, l, 1)', true)
  .option('--exclude-similar', 'Exclude similar looking characters', true)
  .option('--pronounceable', 'Generate pronounceable passwords')
  .option('--pin', 'Generate PIN (numbers only)')
  .option('--passphrase', 'Generate passphrase (words only)')
  .option('--words <number>', 'Number of words in passphrase', parseInt)
  .option('--wordlist <path>', 'Custom wordlist for passphrase')
  .option('--avoid-patterns', 'Avoid common patterns (sequential, repeated)', true)
  .option('--export <format>', 'Export format (txt, json, csv)', /^(txt|json|csv)$/i)
  .option('--output <file>', 'Output file path')
  .option('--qr', 'Output as QR code')
  .option('--check <password>', 'Check strength of provided password')
  .option('--no-color', 'Disable color output')
  .option('--verbose', 'Verbose output');

program.parse();

const options = program.opts();

if (options.check) {
  const strength = checkPasswordStrength(options.check);
  console.log(chalk.bold(`Password Strength Analysis for: ${options.check}`));
  console.log(chalk.green(`Score: ${strength.score}/100`));
  console.log(chalk.blue(`Entropy: ${strength.entropy.toFixed(2)} bits`));
  console.log(chalk.yellow(`Crack Time Estimates:`));
  console.log(`  Online (100 guesses/sec): ${strength.crackTimeOnline}`);
  console.log(`  Offline (1B guesses/sec): ${strength.crackTimeOffline}`);
  console.log(`  Massive Array (100B guesses/sec): ${strength.crackTimeMassive}`);
  console.log(`  Nation State (1T guesses/sec): ${strength.crackTimeNationState}`);
  process.exit(0);
}

if (options.qr && !(options.length || options.passphrase)) {
  console.error(chalk.red('Error: QR code generation requires a password to encode.'));
  process.exit(1);
}

async function run() {
  try {
    let passwords: string[] = [];

    if (options.passphrase) {
      const wordCount = options.words || 4;
      passwords = await generatePassphrase(wordCount, options.wordlist);
    } else if (options.pin) {
      const length = options.length || 6;
      passwords = Array.from({ length: options.count || 1 }, () =>
        generatePin(length)
      );
    } else {
      const length = options.length || 16;
      const count = options.count || 1;
      passwords = Array.from({ length: count }, () =>
        generatePassword({
          length,
          uppercase: options.uppercase,
          lowercase: options.lowercase,
          numbers: options.numbers,
          symbols: options.symbols,
          excludeAmbiguous: options.excludeAmbiguous,
          excludeSimilar: options.excludeSimilar,
          pronounceable: options.pronounceable,
          avoidPatterns: options.avoidPatterns
        })
      );
    }

    // Handle output
    if (options.output) {
      await writeToFile(passwords, options.output, options.export);
      if (!options.quiet) {
        console.log(chalk.green(`Successfully saved ${passwords.length} password(s) to ${options.output}`));
      }
    } else if (options.qr) {
      // For QR, we assume single password (first one)
      QRCodeTerminal.generate(passwords[0], { small: true });
    } else {
      passwords.forEach((pwd, index) => {
        if (options.count && options.count > 1) {
          console.log(chalk.blue(`Password ${index + 1}:`), chalk.green(pwd));
        } else {
          console.log(chalk.green(pwd));
        }
      });
    }
  } catch (error) {
    console.error(chalk.red('Error:'), error.message);
    if (options.verbose) {
      console.error(error.stack);
    }
    process.exit(1);
  }
}

// Helper functions (simplified for brevity)
function generatePin(length: number): string {
  return Array.from({ length: length }, () => Math.floor(Math.random() * 10)).join('');
}

async function generatePassphrase(wordCount: number, customWordlist?: string): Promise<string[]> {
  // In a real implementation, we would load a wordlist and select random words
  // For now, we'll use a small static list
  const wordlist = customWordlist 
    ? await fs.readFile(customWordlist, 'utf8').then(content => content.split('\n').filter(Boolean))
    : ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew'];
  
  return Array.from({ length: 1 }, () => 
    Array.from({ length: wordCount }, () => 
      wordlist[Math.floor(Math.random() * wordlist.length)]
    ).join('-')
  );
}

async function writeToFile(passwords: string[], filePath: string, format?: string) {
  const ext = path.extname(filePath).toLowerCase();
  let data: string;

  if (format || ext) {
    const fmt = (format || ext.substring(1)).toLowerCase();
    switch (fmt) {
      case 'json':
        data = JSON.stringify(passwords, null, 2);
        break;
      case 'csv':
        data = passwords.map(p => `"${p}"`).join('\n');
        break;
      case 'txt':
      default:
        data = passwords.join('\n');
    }
  } else {
    data = passwords.join('\n');
  }

  await fs.writeFile(filePath, data, 'utf8');
}

run();