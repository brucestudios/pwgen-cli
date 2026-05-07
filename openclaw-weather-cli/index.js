#!/usr/bin/env node

const axios = require('axios');
const chalk = require('chalk');
const { program } = require('commander');

program
  .name('weather')
  .description('Get current weather information for a location')
  .option('-l, --location <location>', 'Location to get weather for (city name, zip code, etc.)', 'auto')
  .option('-u, --units [units]', 'Units for temperature: m (metric), u (USCS), or empty for default', '')
  .option('-F, --no-formatting', 'Disable color/formatting output')
  .action(async (options) => {
    try {
      let url = 'https://wttr.in/';
      if (options.location && options.location !== 'auto') {
        url += encodeURIComponent(options.location);
      }
      const params = {
        format: options.noFormatting ? 1 : 4, // 1 for plain text, 4 for ANSI-colored
      };
      if (options.units) {
        // wttr.in uses 'm' for metric, 'u' for USCS, and empty for default
        params[options.units] = '';
      }

      const response = await axios.get(url, { params, responseType: 'text' });
      console.log(response.data);
    } catch (error) {
      if (error.response) {
        console.error(chalk.red(`Error: ${error.response.status} ${error.response.statusText}`));
        process.exit(1);
      } else {
        console.error(chalk.red('Error: Failed to fetch weather data'), error.message);
        process.exit(1);
      }
    }
  });

program.parse();