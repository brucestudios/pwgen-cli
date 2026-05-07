import { Command } from 'commander';
import { readFileSync } from 'fs';
import matter from 'gray-matter';

const program = new Command();

program
  .name('markdown-toc')
  .description('Generate table of contents for markdown files')
  .argument('<file>', 'markdown file to process')
  .option('-s, --skip-first', 'skip the first header (usually title)')
  .option('-m, --max-depth <number>', 'maximum header depth to include', parseInt)
  .action((filePath, options) => {
    const content = readFileSync(filePath, 'utf8');
    const { content: mdContent } = matter(content);
    const lines = mdContent.split('\n');
    const headers: Array<{ level: number; text: string; id: string }> = [];

    let headerCount = 0;
    for (const line of lines) {
      const match = line.match(/^(#{1,6})\s+(.+)/);
      if (match) {
        const level = match[1].length;
        const text = match[2].trim();
        // Generate ID: lowercase, replace spaces with -, remove non-alphanumeric/-/_
        let id = text
          .toLowerCase()
          .replace(/[^\w\s-]/g, '')
          .replace(/\s+/g, '-')
          .replace(/^-+|-+$/g, '');
        // Ensure uniqueness
        let baseId = id;
        let counter = 0;
        while (headers.some(h => h.id === id)) {
          counter++;
          id = `${baseId}-${counter}`;
        }
        headers.push({ level, text, id });
        headerCount++;
      }
    }

    const skipFirst = options.skipFirst ?? false;
    const maxDepth = options.maxDepth ?? 6;
    const startIndex = skipFirst ? 1 : 0;
    const filtered = headers.slice(startIndex).filter(h => h.level <= maxDepth);

    if (filtered.length === 0) {
      console.log('No headers found.');
      return;
    }

    const indent = '  ';
    let output = '';
    for (const header of filtered) {
      const spaces = indent.repeat(header.level - 1);
      output += `${spaces}- [${header.text}](#${header.id})\n`;
    }
    console.log(output);
  });

program.parse();