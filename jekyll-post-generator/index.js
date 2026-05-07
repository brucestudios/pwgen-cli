#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { program } = require('commander');
const inquirer = require('inquirer');
const slugify = require('slugify');
const chalk = require('chalk');

const POSTS_DIR = '_posts';
const TEMPLATE = `---\nlayout: post\ntitle: "{{ title }}"\ndate: {{ date }}\ncategories: [{{ categories }}]\ntags: [{{ tags }}]\n---\n\n`;

program
  .name('jekyll-post')
  .description('CLI helper to create Jekyll posts')
  .version('1.0.0');

program
  .command('new')
  .description('Create a new Jekyll post')
  .action(async () => {
    const answers = await inquirer.prompt([
      {
        type: 'input',
        name: 'title',
        message: 'Post title:',
        validate: input => input.length > 0 || 'Title is required'
      },
      {
        type: 'input',
        name: 'categories',
        message: 'Categories (comma separated):',
        default: ''
      },
      {
        type: 'input',
        name: 'tags',
        message: 'Tags (comma separated):',
        default: ''
      }
    ]);

    const date = new Date().toISOString().slice(0, 19).replace('T', ' ');
    const slug = slugify(answers.title, { lower: true, strict: true });
    const fileName = `${date.split(' ')[0]}-${slug}.md`;
    const filePath = path.join(process.cwd(), POSTS_DIR, fileName);

    // Ensure _posts directory exists
    if (!fs.existsSync(POSTS_DIR)) {
      fs.mkdirSync(POSTS_DIR);
    }

    const frontMatter = TEMPLATE
      .replace('{{ title }}', answers.title)
      .replace('{{ date }}', date)
      .replace('{{ categories }}', answers.categories.split(',').map(c => c.trim()).filter(Boolean).join(', '))
      .replace('{{ tags }}', answers.tags.split(',').map(t => t.trim()).filter(Boolean).join(', '));

    fs.writeFileSync(filePath, frontMatter);
    console.log(chalk.green(`Post created: ${filePath}`));
  });

program.parse();