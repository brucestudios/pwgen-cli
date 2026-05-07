#!/usr/bin/env node

const { program } = require('commander');
const chalk = require('chalk');
const inquirer = require('inquirer');
const slugify = require('slugify');
const { createPost } = require('./lib/createPost');
const { getTemplate } = require('./lib/utils');

program
  .name('jekyll-post')
  .description('CLI helper for Jekyll bloggers to create posts with proper front matter and templates')
  .version('1.0.0');

program
  .command('new')
  .description('Create a new Jekyll post')
  .option('-t, --title <title>', 'Post title')
  .option('-c, --category <category>', 'Post category')
  .option('-T, --tags <tags>', 'Comma-separated tags')
  .option('-l, --layout <layout>', 'Layout to use (default: post)', 'post')
  .option('-d, --date <date>', 'Date (YYYY-MM-DD), defaults to today')
  .option('-s, --slug <slug>', 'Custom slug (overrides title-based slug)')
  .action(async (options) => {
    try {
      // If title not provided via option, ask interactively
      let title = options.title;
      if (!title) {
        const { titleInput } = await inquirer.prompt([
          {
            type: 'input',
            name: 'titleInput',
            message: 'Enter post title:',
            validate: input => input.length > 0 || 'Title is required',
          },
        ]);
        title = titleInput;
      }

      let category = options.category;
      if (!category) {
        const { categoryInput } = await inquirer.prompt([
          {
            type: 'input',
            name: 'categoryInput',
            message: 'Enter category (optional):',
          },
        ]);
        category = categoryInput.trim() || undefined;
      }

      let tagsInput = options.tags;
      let tags = [];
      if (tagsInput) {
        tags = tagsInput.split(',').map(tag => tag.trim()).filter(tag => tag.length > 0);
      } else {
        const { tagsAnswer } = await inquirer.prompt([
          {
            type: 'input',
            name: 'tagsAnswer',
            message: 'Enter tags (comma-separated, optional):',
          },
        ]);
        tags = tagsAnswer.split(',').map(tag => tag.trim()).filter(tag => tag.length > 0);
      }

      const layout = options.layout || 'post';
      let date = options.date;
      if (!date) {
        const today = new Date();
        date = today.toISOString().slice(0, 10); // YYYY-MM-DD
      }

      let slug = options.slug;
      if (!slug) {
        slug = slugify(title, { lower: true, strict: true });
      }

      await createPost({ title, category, tags, layout, date, slug });
      console.log(chalk.green('✅ Post created successfully!'));
    } catch (error) {
      console.error(chalk.red('❌ Error creating post:'), error.message);
      process.exit(1);
    }
  });

program.parse();