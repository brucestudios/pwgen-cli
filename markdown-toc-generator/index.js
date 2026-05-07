#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { Command } = require('commander');

const program = new Command();

program
  .name('markdown-toc')
  .description('Generate a table of contents for markdown files')
  .argument('<file>', 'markdown file to process')
  .option('-d, --depth <number>', 'maximum heading depth to include (default: 3)', parseInt, 3)
  .option('-o, --output <file>', 'output file (default: stdout)')
  .action((file, options) => {
    // Read the markdown file
    const filePath = path.resolve(file);
    let content;
    try {
      content = fs.readFileSync(filePath, 'utf8');
    } catch (err) {
      console.error(`Error reading file ${filePath}: ${err.message}`);
      process.exit(1);
    }

    // Extract headings
    const headings = [];
    const headingRegex = /^(#{1,6})\s+(.+)$/gm;
    let match;
    
    while ((match = headingRegex.exec(content)) !== null) {
      const level = match[1].length;
      const text = match[2].trim();
      
      if (level <= options.depth) {
        headings.push({ level, text });
      }
    }

    if (headings.length === 0) {
      console.error('No headings found in the markdown file.');
      process.exit(0);
    }

    // Generate TOC
    let toc = '# Table of Contents\n\n';
    headings.forEach(heading => {
      const indent = '  '.repeat(heading.level - 1);
      // Create anchor link: convert to lowercase, replace spaces with hyphens, remove special chars
      const anchor = heading.text
        .toLowerCase()
        .replace(/[^\w\s-]/g, '')
        .replace(/\s+/g, '-');
      
      toc += `${indent}- [${heading.text}](#${anchor})\n`;
    });

    // Output
    if (options.output) {
      try {
        fs.writeFileSync(options.output, toc);
        console.log(`Table of contents written to ${options.output}`);
      } catch (err) {
        console.error(`Error writing to file ${options.output}: ${err.message}`);
        process.exit(1);
      }
    } else {
      console.log(toc);
    }
  });

program.parse();