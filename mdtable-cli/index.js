#!/usr/bin/env node

const { program } = require('commander');
const fs = require('fs');

program
  .name('mdtable')
  .description('Convert markdown tables to HTML tables')
  .version('1.0.0');

program
  .command('convert')
  .description('Convert a markdown file with tables to HTML')
  .argument('<input>', 'input markdown file')
  .option('-o, --output <file>', 'output HTML file (default: stdout)')
  .action((input, options) => {
    const content = fs.readFileSync(input, 'utf8');
    const html = convertMarkdownTablesToHtml(content);
    
    if (options.output) {
      fs.writeFileSync(options.output, html);
      console.log(`Converted ${input} to ${options.output}`);
    } else {
      console.log(html);
    }
  });

program
  .command('inline')
  .description('Convert markdown table syntax to HTML inline')
  .argument('<markdown>', 'markdown table string')
  .action((markdown) => {
    const html = convertMarkdownTablesToHtml(markdown);
    console.log(html);
  });

function convertMarkdownTablesToHtml(markdown) {
  // Split by lines
  const lines = markdown.split('\n');
  let inTable = false;
  let resultLines = [];
  
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    
    // Check if line looks like a markdown table row (contains |)
    if (line.trim().startsWith('|') && line.trim().endsWith('|')) {
      if (!inTable) {
        inTable = true;
        resultLines.push('<table>');
        
        // Check if next line is separator
        if (i + 1 < lines.length && lines[i + 1].trim().match(/^[\|\-\s:]+$/)) {
          // Process header
          resultLines.push('  <thead>');
          resultLines.push('    <tr>');
          const headerCells = line.substring(1, line.length - 1).split('|').map(cell => cell.trim());
          headerCells.forEach(cell => {
            resultLines.push(`      <th>${escapeHtml(cell)}</th>`);
          });
          resultLines.push('    </tr>');
          resultLines.push('  </thead>');
          resultLines.push('  <tbody>');
          
          // Skip separator line
          i++;
          
          // Process data rows
          while (i + 1 < lines.length && lines[i + 1].trim().startsWith('|') && lines[i + 1].trim().endsWith('|')) {
            i++;
            const dataLine = lines[i];
            resultLines.push('    <tr>');
            const dataCells = dataLine.substring(1, dataLine.length - 1).split('|').map(cell => cell.trim());
            dataCells.forEach(cell => {
              resultLines.push(`      <td>${escapeHtml(cell)}</td>`);
            });
            resultLines.push('    </tr>');
          }
          
          resultLines.push('  </tbody>');
          resultLines.push('</table>');
          inTable = false;
        } else {
          // No separator, treat as regular table without header
          resultLines.push('  <tbody>');
          resultLines.push('    <tr>');
          const cells = line.substring(1, line.length - 1).split('|').map(cell => cell.trim());
          cells.forEach(cell => {
            resultLines.push(`      <td>${escapeHtml(cell)}</td>`);
          });
          resultLines.push('    </tr>');
          
          // Continue collecting rows until no more table rows
          while (i + 1 < lines.length && lines[i + 1].trim().startsWith('|') && lines[i + 1].trim().endsWith('|')) {
            i++;
            const dataLine = lines[i];
            resultLines.push('    <tr>');
            const dataCells = dataLine.substring(1, dataLine.length - 1).split('|').map(cell => cell.trim());
            dataCells.forEach(cell => {
              resultLines.push(`      <td>${escapeHtml(cell)}</td>`);
            });
            resultLines.push('    </tr>');
          }
          
          resultLines.push('  </tbody>');
          resultLines.push('</table>');
          inTable = false;
        }
      } else {
        // Already in table, but we got another line that looks like table start
        // This shouldn't happen with proper parsing, but handle gracefully
        resultLines.push(line);
      }
    } else {
      // Not a table line
      if (inTable) {
        // We were in a table but hit non-table line - close table
        resultLines.push('</table>');
        inTable = false;
      }
      resultLines.push(line);
    }
  }
  
  // Close table if still open at end
  if (inTable) {
    resultLines.push('</table>');
  }
  
  return resultLines.join('\n');
}

function escapeHtml(text) {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

program.parse();

// If no command provided, show help
if (!process.argv.slice(2).length) {
  program.outputHelp();
}