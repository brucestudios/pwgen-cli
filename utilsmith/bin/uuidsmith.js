#!/usr/bin/env node

/**
 * UUID Smith CLI - Command line interface for UUID utilities
 */

const { generate, generateV1, generateV4, validate, getVersion, format } = require('../src/uuidsmith/index');
const { program } = require('commander');

program
  .name('uuidsmith')
  .description('UUID/GUID utility toolkit')
  .version('1.0.0');

program
  .command('generate')
  .description('Generate a random UUID')
  .option('-v, --version <number>', 'UUID version (1 or 4)', '4')
  .option('-c, --count <number>', 'Number of UUIDs to generate', '1')
  .option('-u, --uppercase', 'Output in uppercase')
  .option('--urn', 'Prefix with urn:uuid:')
  .action((options) => {
    const count = parseInt(options.count);
    const version = parseInt(options.version);
    
    if (isNaN(count) || count < 1) {
      console.error('Error: Count must be a positive integer');
      process.exit(1);
    }
    
    if ([1, 4].indexOf(version) === -1) {
      console.error('Error: Only UUID versions 1 and 4 are supported');
      process.exit(1);
    }
    
    for (let i = 0; i < count; i++) {
      let uuid;
      if (version === 1) {
        uuid = generateV1();
      } else {
        uuid = generateV4();
      }
      
      console.log(format(uuid, {
        uppercase: options.uppercase,
        urn: options.urn
      }));
    }
  });

program
  .command('validate <uuid>')
  .description('Validate a UUID string')
  .action((uuid) => {
    const isValid = validate(uuid);
    if (isValid) {
      console.log(`✓ "${uuid}" is a valid UUID (version ${getVersion(uuid)})`);
    } else {
      console.log(`✗ "${uuid}" is not a valid UUID`);
      process.exit(1);
    }
  });

program
  .command('info <uuid>')
  .description('Get information about a UUID')
  .action((uuid) => {
    if (!validate(uuid)) {
      console.log(`✗ "${uuid}" is not a valid UUID`);
      process.exit(1);
    }
    
    console.log(`UUID: ${uuid}`);
    console.log(`Version: ${getVersion(uuid)}`);
    console.log(`Formatted (lowercase): ${format(uuid, { lowercase: true })}`);
    console.log(`Formatted (uppercase): ${format(uuid, { uppercase: true })}`);
    console.log(`Formatted (URN): ${format(uuid, { urn: true })}`);
  });

program.parse();