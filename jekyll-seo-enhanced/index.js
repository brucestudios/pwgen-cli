#!/usr/bin/env node

const { program } = require('commander');
const inquirer = require('inquirer');
const chalk = require('chalk');
const slugify = require('slugify');
const fs = require('fs');
const path = require('path');

program
  .name('jekyll-seo')
  .description('CLI tool to enhance SEO for Jekyll blogs')
  .version('1.0.0');

program
  .command('new-post')
  .description('Create a new Jekyll post with SEO-optimized front matter')
  .option('-t, --title <title>', 'Post title')
  .option('-c, --category <category>', 'Post category')
  .option('-d, --date <date>', 'Post date (YYYY-MM-DD)')
  .action(async (options) => {
    const answers = await inquirer.prompt([
      {
        type: 'input',
        name: 'title',
        message: 'Enter post title:',
        default: options.title,
        validate: (input) => input.length > 0 || 'Title is required'
      },
      {
        type: 'input',
        name: 'category',
        message: 'Enter post category (default: blog):',
        default: options.category || 'blog'
      },
      {
        type: 'input',
        name: 'date',
        message: 'Enter post date (YYYY-MM-DD, default: today):',
        default: options.date || new Date().toISOString().split('T')[0]
      },
      {
        type: 'input',
        name: 'tags',
        message: 'Enter tags (comma-separated):',
        default: ''
      },
      {
        type: 'input',
        name: 'description',
        message: 'Enter meta description for SEO:',
        validate: (input) => input.length > 0 || 'Description is required for SEO'
      },
      {
        type: 'input',
        name: 'keywords',
        message: 'Enter SEO keywords (comma-separated):',
        default: ''
      }
    ]);

    const title = answers.title;
    const category = answers.category;
    const date = answers.date;
    const tagsInput = answers.tags.trim();
    const description = answers.description;
    const keywordsInput = answers.keywords.trim();

    const tags = tagsInput ? tagsInput.split(',').map(tag => tag.trim()).filter(tag => tag) : [];
    const keywords = keywordsInput ? keywordsInput.split(',').map(keyword => keyword.trim()).filter(keyword => keyword) : [];

    const slug = slugify(title, { lower: true, strict: true });
    const filename = `${date}-${slug}.md`;
    const filepath = path.join('_posts', filename);

    // Ensure _posts directory exists
    const postsDir = path.join(process.cwd(), '_posts');
    if (!fs.existsSync(postsDir)) {
      fs.mkdirSync(postsDir, { recursive: true });
    }

    const frontmatter = [
      '---',
      `layout: post`,
      `title: "${title}"`,
      `date: ${date}`,
      `category: ${category}`,
      tags.length > 0 ? `tags: [${tags.map(t => `"${t}"`).join(', ')}]` : 'tags: []',
      `description: "${description}"`,
      keywords.length > 0 ? `keywords: [${keywords.map(k => `"${k}"`).join(', ')}]` : 'keywords: []',
      '---',
      '',
      '# ' + title,
      '',
      'Write your content here...',
      ''
    ].join('\n');

    fs.writeFileSync(filepath, frontmatter, 'utf8');
    console.log(chalk.green(`✅ Created post: ${filepath}`));
    console.log(chalk.blue(`📝 Edit the file to add your content`));
  });

program
  .command('audit')
  .description('Audit existing Jekyll posts for SEO issues')
  .action(() => {
    const postsDir = path.join(process.cwd(), '_posts');
    if (!fs.existsSync(postsDir)) {
      console.log(chalk.red('❌ No _posts directory found'));
      return;
    }

    const files = fs.readdirSync(postsDir).filter(file => file.endsWith('.md'));
    if (files.length === 0) {
      console.log(chalk.yellow('⚠️  No posts found in _posts directory'));
      return;
    }

    console.log(chalk.blue(`🔍 Auditing ${files.length} posts for SEO issues...\n`));

    let issues = 0;
    files.forEach(file => {
      const filepath = path.join(postsDir, file);
      const content = fs.readFileSync(filepath, 'utf8');
      
      // Extract frontmatter
      const frontmatterMatch = content.match(/^---\n([\s\S]*?)\n---/);
      if (!frontmatterMatch) {
        console.log(chalk.red(`❌ ${file}: Missing or malformed frontmatter`));
        issues++;
        return;
      }

      const frontmatter = frontmatterMatch[1];
      const issuesInFile = [];

      // Check for title
      if (!frontmatter.match(/title:/i)) {
        issuesInFile.push('Missing title');
      }

      // Check for date
      if (!frontmatter.match(/date:/i)) {
        issuesInFile.push('Missing date');
      }

      // Check for description (SEO)
      if (!frontmatter.match(/description:/i)) {
        issuesInFile.push('Missing description (important for SEO)');
      }

      // Check for keywords (SEO)
      if (!frontmatter.match(/keywords:/i)) {
        issuesInFile.push('Missing keywords (helpful for SEO)');
      }

      if (issuesInFile.length > 0) {
        console.log(chalk.yellow(`⚠️  ${file}:`));
        issuesInFile.forEach(issue => console.log(`   - ${issue}`));
        issues += issuesInFile.length;
      } else {
        console.log(chalk.green(`✅ ${file}: SEO looks good`));
      }
    });

    console.log(`\n${chalk.blue('Audit complete:')}`);
    if (issues === 0) {
      console.log(chalk.green(`🎉 All posts pass SEO audit!`));
    } else {
      console.log(chalk.red(`🚨 Found ${issues} SEO issues across ${files.length} posts`));
    }
  });

program
  .command('suggest')
  .description('Get SEO suggestions for a post title or content')
  .action(async () => {
    const answers = await inquirer.prompt([
      {
        type: 'input',
        name: 'title',
        message: 'Enter post title or content to analyze:',
        validate: (input) => input.length > 0 || 'Input is required'
      }
    ]);

    const input = answers.title;
    const suggestions = [];

    // Title length suggestion
    if (input.length < 30) {
      suggestions.push(chalk.blue('💡 Consider making your title more descriptive (aim for 50-60 characters)'));
    } else if (input.length > 60) {
      suggestions.push(chalk.yellow(`⚠️  Title is ${input.length} characters - consider shortening to under 60 chars for better SERP display`));
    } else {
      suggestions.push(chalk.green(`✅ Title length is good (${input.length} characters)`));
    }

    // Check for power words
    const powerWords = ['how to', 'guide', 'tips', 'best', 'top', 'ultimate', 'complete', 'essential'];
    const hasPowerWord = powerWords.some(word => input.toLowerCase().includes(word));
    if (!hasPowerWord && input.length > 10) {
      suggestions.push(chalk.blue('💡 Consider adding power words like "how to", "guide", "tips", "best" to increase click-through rates'));
    }

    // Check for numbers (list posts perform well)
    if (!/\d/.test(input)) {
      suggestions.push(chalk.blue('💡 Consider adding a number to make it a list post (e.g., "5 Ways to...")'));
    } else {
      suggestions.push(chalk.green('✅ Contains numbers - list posts often perform well in search'));
    }

    // Check for question format
    if (!input.endsWith('?') && !input.toLowerCase().startsWith('how to') && !input.toLowerCase().startsWith('what is')) {
      suggestions.push(chalk.blue('💡 Consider phrasing as a question or "how to" guide for better search visibility'));
    }

    console.log(chalk.bold('\n🔍 SEO Suggestions:'));
    suggestions.forEach(suggestion => console.log(`  ${suggestion}`));
    console.log('');
  });

program.parse();