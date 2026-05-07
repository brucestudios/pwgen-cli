#!/usr/bin/env node
/**
 * OpenClaw Skill CLI
 * A command-line utility to manage OpenClaw skills from ClawHub.
 */

const { execSync } = require('child_process');
const { program } = require('commander');
const chalk = require('chalk');
const ora = require('ora');

program
  .name('oc-skill')
  .description('CLI to manage OpenClaw skills')
  .version('1.0.0');

program
  .command('list')
  .description('List available skills from ClawHub')
  .action(async () => {
    const spinner = ora('Fetching skill list...').start();
    try {
      const output = execSync('clawhub search', { encoding: 'utf8' });
      spinner.succeed('Skill list fetched');
      console.log(output);
    } catch (error) {
      spinner.fail('Failed to fetch skill list');
      console.error(chalk.red('Error:'), error.message);
      process.exit(1);
    }
  });

program
  .command('install <skill-name>')
  .description('Install a skill from ClawHub')
  .action(async (skillName) => {
    const spinner = ora(`Installing skill ${skillName}...`).start();
    try {
      execSync(`clawhub install ${skillName}`, { stdio: 'inherit' });
      spinner.succeed(`Skill ${skillName} installed`);
    } catch (error) {
      spinner.fail(`Failed to install skill ${skillName}`);
      console.error(chalk.red('Error:'), error.message);
      process.exit(1);
    }
  });

program
  .command('update <skill-name>')
  .description('Update an installed skill from ClawHub')
  .action(async (skillName) => {
    const spinner = ora(`Updating skill ${skillName}...`).start();
    try {
      execSync(`clawhub update ${skillName}`, { stdio: 'inherit' });
      spinner.succeed(`Skill ${skillName} updated`);
    } catch (error) {
      spinner.fail(`Failed to update skill ${skillName}`);
      console.error(chalk.red('Error:'), error.message);
      process.exit(1);
    }
  });

program
  .command('publish <skill-directory>')
  .description('Publish a skill to ClawHub')
  .action(async (skillDirectory) => {
    const spinner = ora(`Publishing skill from ${skillDirectory}...`).start();
    try {
      execSync(`clawhub publish ${skillDirectory}`, { stdio: 'inherit' });
      spinner.succeed(`Skill published from ${skillDirectory}`);
    } catch (error) {
      spinner.fail(`Failed to publish skill from ${skillDirectory}`);
      console.error(chalk.red('Error:'), error.message);
      process.exit(1);
    }
  });

program.parse();