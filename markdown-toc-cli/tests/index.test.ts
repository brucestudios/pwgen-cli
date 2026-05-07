import { execSync } from 'child_process';
import { readFileSync, writeFileSync } from 'fs';
import { tmpdir } from 'os';
import { join } from 'path';

describe('markdown-toc-cli', () => {
  const bin = './dist/index.js';

  beforeAll(() => {
    // Ensure the binary is built
    execSync('npm run build', { stdio: 'ignore' });
  });

  test('generates TOC for a simple markdown file', () => {
    const markdown = `
# Title

## Section 1

Some content.

### Subsection 1.1

More content.

## Section 2

Even more.
`;
    const tmpDir = tmpdir();
    const filePath = join(tmpDir, 'test.md');
    writeFileSync(filePath, markdown, 'utf8');

    const output = execSync(`node ${bin} ${filePath}`, { encoding: 'utf8' });
    expect(output).toContain('- [Section 1](#section-1)');
    expect(output).toContain('  - [Subsection 1.1](#subsection-1-1)');
    expect(output).toContain('- [Section 2](#section-2)');
    // Should not include the title because we didn't skip first
    expect(output).not.toContain('Title');
  });

  test('skips first header when option is used', () => {
    const markdown = `
# Title

## Section 1

Content.
`;
    const tmpDir = tmpdir();
    const filePath = join(tmpDir, 'test.md');
    writeFileSync(filePath, markdown, 'utf8');

    const output = execSync(`node ${bin} ${filePath} --skip-first`, { encoding: 'utf8' });
    expect(output).toContain('- [Section 1](#section-1)');
    expect(output).not.toContain('Title');
  });

  test('limits depth', () => {
    const markdown = `
# Title

## Section 1

### Subsection 1.1

#### Subsubsection 1.1.1
`;
    const tmpDir = tmpdir();
    const filePath = join(tmpDir, 'test.md');
    writeFileSync(filePath, markdown, 'utf8');

    const output = execSync(`node ${bin} ${filePath} --max-depth 2`, { encoding: 'utf8' });
    expect(output).toContain('- [Section 1](#section-1)');
    expect(output).toContain('  - [Subsection 1.1](#subsection-1-1)');
    expect(output).not.toContain('Subsubsection 1.1.1');
  });
});