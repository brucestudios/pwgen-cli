const fs = require('fs');
const path = require('path');
const { frontMatter } = require('./utils');

async function createPost({ title, category, tags, layout, date, slug }) {
  const postsDir = path.join(process.cwd(), '_posts');
  // Ensure _posts directory exists
  if (!fs.existsSync(postsDir)) {
    fs.mkdirSync(postsDir, { recursive: true });
  }

  const fileName = `${date}-${slug}.md`;
  const filePath = path.join(postsDir, fileName);

  if (fs.existsSync(filePath)) {
    throw new Error(`Post ${fileName} already exists`);
  }

  const frontMatterData = {
    layout,
    title,
    date: `${date} 00:00:00 +0000`,
    ...(category && { category }),
    ...(tags && tags.length > 0 && { tags }),
  };

  const content = `---\n${Object.entries(frontMatterData)
    .map(([key, value]) => {
      if (Array.isArray(value)) {
        return `${key}:\n${value.map(v => `  - ${v}`).join('\n')}`;
      }
      return `${key}: ${value}`;
    })
    .join('\n')}\n---\n\n# ${title}\n\nWrite your post content here.\n`;

  fs.writeFileSync(filePath, content, 'utf8');
}

module.exports = { createPost };