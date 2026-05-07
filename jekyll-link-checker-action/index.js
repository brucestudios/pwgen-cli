const core = require('@actions/core');
const github = require('@actions/github');
const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

async function run() {
  try {
    // Get inputs
    const siteDir = core.getInput('site-dir') || '.';
    const excludePatterns = core.getInput('exclude') || '';
    const timeout = parseInt(core.getInput('timeout')) || 30000;
    const failOnError = core.getBooleanInput('fail-on-error') || true;
    
    core.info(`Checking links in Jekyll site at: ${siteDir}`);
    
    // Build the Jekyll site first
    core.info('Building Jekyll site...');
    execSync('bundle exec jekyll build', { 
      cwd: siteDir,
      stdio: 'pipe'
    });
    
    // Check links in the built site
    const siteBuiltDir = path.join(siteDir, '_site');
    if (!fs.existsSync(siteBuiltDir)) {
      throw new Error(`Jekyll build failed: _site directory not found in ${siteDir}`);
    }
    
    core.info('Checking for broken links...');
    
    // Build html-link-checker command
    let cmd = `html-link-checker ${siteBuiltDir}`;
    
    if (excludePatterns) {
      const excludes = excludePatterns.split(',').map(p => p.trim()).filter(p => p);
      excludes.forEach(pattern => {
        cmd += ` --exclude "${pattern}"`;
      });
    }
    
    cmd += ` --timeout ${timeout}`;
    
    // Run link checker
    try {
      execSync(cmd, { stdio: 'pipe' });
      core.info('✅ All links are valid!');
    } catch (error) {
      const output = error.stdout ? error.stdout.toString() : error.stderr ? error.stderr.toString() : error.message;
      core.setFailed(`Link checker found broken links:\n${output}`);
      
      if (!failOnError) {
        core.warning('Continuing despite broken links (fail-on-error set to false)');
      } else {
        throw error;
      }
    }
    
  } catch (error) {
    core.setFailed(`Action failed with error: ${error.message}`);
  }
}

run();