#!/usr/bin/env node

const axios = require('axios');
const { JSDOM } = require('jsdom');
const { program } = require('commander');
const chalk = require('chalk');

program
  .name('jekyll-link-checker')
  .description('Check for broken links in Jekyll sites')
  .option('-s, --source <path>', 'Path to Jekyll source directory', './')
  .option('-d, --destination <path>', 'Path to Jekyll build directory (defaults to _site)', '_site')
  .option('-t, --timeout <ms>', 'Request timeout in milliseconds', '5000')
  .option('--skip-external', 'Skip checking external links')
  .option('--verbose', 'Verbose output')
  .action(async (options) => {
    const fs = await import('fs');
    const path = await import('path');
    
    const sourceDir = path.resolve(process.cwd(), options.source);
    const destDir = path.resolve(process.cwd(), options.destination);
    const timeout = parseInt(options.timeout);
    const skipExternal = options.skipExternal;
    const verbose = options.verbose;
    
    console.log(chalk.blue(`🔍 Jekyll Link Checker`));
    console.log(chalk.blue(`Source: ${sourceDir}`));
    console.log(chalk.blue(`Destination: ${destDir}`));
    console.log(chalk.blue(`Timeout: ${timeout}ms`));
    console.log(chalk.blue(`Skip external: ${skipExternal}\n`));
    
    // Check if destination exists
    if (!fs.existsSync(destDir)) {
      console.error(chalk.red(`❌ Destination directory ${destDir} does not exist. Build your Jekyll site first.`));
      process.exit(1);
    }
    
    // Find all HTML files in destination
    const htmlFiles = findHtmlFiles(destDir);
    console.log(chalk.green(`📄 Found ${htmlFiles.length} HTML files to check\n`));
    
    // Collect all links
    const links = [];
    for (const file of htmlFiles) {
      const fileLinks = extractLinksFromFile(file, destDir);
      links.push(...fileLinks);
    }
    
    console.log(chalk.green(`🔗 Found ${links.length} total links to check\n`));
    
    // Check links
    const results = await checkLinks(links, { timeout, skipExternal, verbose });
    
    // Print summary
    printSummary(results);
    
    // Exit with error code if broken links found
    const brokenCount = results.filter(r => r.status === 'broken').length;
    if (brokenCount > 0) {
      process.exit(1);
    } else {
      process.exit(0);
    }
  });

function findHtmlFiles(dir) {
  const fs = require('fs');
  const path = require('path');
  const files = [];
  
  function traverse(directory) {
    const entries = fs.readdirSync(directory, { withFileTypes: true });
    for (const entry of entries) {
      const fullPath = path.join(directory, entry.name);
      if (entry.isDirectory()) {
        traverse(fullPath);
      } else if (entry.isFile() && entry.name.endsWith('.html')) {
        files.push(fullPath);
      }
    }
  }
  
  traverse(dir);
  return files;
}

function extractLinksFromFile(filePath, baseDir) {
  const fs = require('fs');
  const path = require('path');
  
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    const dom = new JSDOM(content);
    const document = dom.window.document;
    
    const links = [];
    const anchors = document.querySelectorAll('a[href]');
    const images = document.querySelectorAll('img[src]');
    const scripts = document.querySelectorAll('script[src]');
    const linksTags = document.querySelectorAll('link[href]');
    
    // Process anchors
    anchors.forEach(anchor => {
      const href = anchor.getAttribute('href');
      if (href && !href.startsWith('#') && !href.startsWith('javascript:')) {
        links.push({
          url: href,
          type: 'anchor',
          file: filePath,
          text: anchor.textContent.trim().substring(0, 100)
        });
      }
    });
    
    // Process images
    images.forEach(img => {
      const src = img.getAttribute('src');
      if (src) {
        links.push({
          url: src,
          type: 'image',
          file: filePath,
          alt: img.getAttribute('alt') || ''
        });
      }
    });
    
    // Process scripts
    scripts.forEach(script => {
      const src = script.getAttribute('src');
      if (src) {
        links.push({
          url: src,
          type: 'script',
          file: filePath
        });
      }
    });
    
    // Process link tags (CSS, etc)
    linksTags.forEach(link => {
      const href = link.getAttribute('href');
      if (href && link.rel !== 'stylesheet') { // We'll check CSS too actually
        links.push({
          url: href,
          type: 'link',
          file: filePath,
          rel: link.rel
        });
      }
      
      // Also check stylesheet links
      if (href && link.rel === 'stylesheet') {
        links.push({
          url: href,
          type: 'stylesheet',
          file: filePath
        });
      }
    });
    
    return links;
  } catch (error) {
    console.error(chalk.yellow(`⚠️  Warning: Could not parse ${filePath}: ${error.message}`));
    return [];
  }
}

async function checkLinks(links, options) {
  const results = [];
  
  for (let i = 0; i < links.length; i++) {
    const link = links[i];
    const isExternal = isExternalUrl(link.url);
    
    if (options.skipExternal && isExternal) {
      if (options.verbose) {
        console.log(chalk.gray(`⏭️  Skipping external: ${link.url}`));
      }
      results.push({
        ...link,
        status: 'skipped',
        reason: 'external link skipped'
      });
      continue;
    }
    
    try {
      const url = resolveUrl(link.url, link.file, options.baseDir || process.cwd());
      
      if (options.verbose) {
        console.log(chalk.blue(`🔗 [${i+1}/${links.length}] Checking: ${url}`));
      }
      
      const response = await axios.head(url, {
        timeout: options.timeout,
        validateStatus: status => status < 500 // Accept any status < 500
      });
      
      if (response.status >= 400) {
        results.push({
          ...link,
          status: 'broken',
          statusCode: response.status,
          url: url
        });
        
        if (!options.verbose) {
          console.log(chalk.red(`❌ Broken: ${url} (${response.status})`));
        }
      } else {
        results.push({
          ...link,
          status: 'ok',
          statusCode: response.status,
          url: url
        });
        
        if (options.verbose) {
          console.log(chalk.green(`✅ OK: ${url} (${response.status})`));
        }
      }
    } catch (error) {
      results.push({
        ...link,
        status: 'broken',
        error: error.message,
        url: typeof url !== 'undefined' ? url : link.url
      });
      
      if (!options.verbose) {
        console.log(chalk.red(`❌ Broken: ${link.url} (${error.message})`));
      } else {
        console.log(chalk.red(`❌ Broken: ${link.url} (${error.message})`));
      }
    }
    
    // Small delay to be respectful to servers
    await new Promise(resolve => setTimeout(resolve, 50));
  }
  
  return results;
}

function isExternalUrl(url) {
  try {
    const urlObj = new URL(url);
    return urlObj.protocol !== 'file:' && 
           !(urlObj.hostname === 'localhost' || urlObj.hostname === '127.0.0.1') &&
           urlObj.hostname !== '';
  } catch (e) {
    // If URL parsing fails, treat as relative/internal
    return false;
  }
}

function resolveUrl(href, filePath, baseDir) {
  try {
    // If it's already an absolute URL, return as is
    if (/^https?:\/\//i.test(href)) {
      return new URL(href).toString();
    }
    
    // If it's a protocol-relative URL
    if (/^\/\//.test(href)) {
      return `https:${href}`;
    }
    
    // If it's root-relative
    if (href.startsWith('/')) {
      const url = new URL(`http://placeholder.com${href}`);
      return url.toString().replace('http://placeholder.com', '');
    }
    
    // Relative to the file's directory
    const fileDir = require('path').dirname(filePath);
    const fullPath = require('path').resolve(fileDir, href);
    const relativePath = require('path').relative(baseDir, fullPath);
    
    // For local file paths, we'll check if file exists
    if (require('fs').existsSync(fullPath)) {
      return `file://${fullPath}`;
    }
    
    // Otherwise treat as URL relative to site root
    return `/${relativePath.split(require('path').sep).join('/')}`;
  } catch (e) {
    // Fallback: return as-is
    return href;
  }
}

function printSummary(results) {
  const ok = results.filter(r => r.status === 'ok').length;
  const broken = results.filter(r => r.status === 'broken').length;
  const skipped = results.filter(r => r.status === 'skipped').length;
  
  console.log('\n' + '='.repeat(50));
  console.log(chalk.blue('📊 LINK CHECK SUMMARY'));
  console.log('='.repeat(50));
  console.log(chalk.green(`✅ OK links:      ${ok}`));
  console.log(chalk.red(`❌ Broken links:  ${broken}`));
  console.log(chalk.gray(`⏭️  Skipped:       ${skipped}`));
  console.log(chalk.blue(`🔗 Total checked: ${results.length}`));
  console.log('='.repeat(50));
  
  if (broken > 0) {
    console.log(chalk.red(`\n🚨 Found ${broken} broken link(s):\n`));
    const brokenLinks = results.filter(r => r.status === 'broken');
    brokenLinks.forEach((link, index) => {
      console.log(chalk.red(`${index + 1}. ${link.url}`));
      console.log(chalk.dim(`   File: ${link.file}`));
      console.log(chalk.dim(`   Type: ${link.type}`));
      if (link.statusCode) {
        console.log(chalk.dim(`   Status: ${link.statusCode}`));
      }
      if (link.error) {
        console.log(chalk.dim(`   Error: ${link.error}`));
      }
      console.log('');
    });
  } else {
    console.log(chalk.green(`\n🎉 All links are working correctly!\n`));
  }
}

program.parse();