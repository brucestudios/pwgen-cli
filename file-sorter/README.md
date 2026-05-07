# File Sorter CLI

A command-line tool to organize files in a directory into subfolders by file type (extension).

## Features

- Automatically categorizes files into folders like Images, Documents, Spreadsheets, etc.
- Handles files without extensions (placed in `no_extension` folder).
- Dry-run mode to preview changes without moving files.
- Avoids overwriting existing files by appending a counter.
- Easy to use with sensible defaults.

## Installation

### Via pip

```bash
pip install file-sorter-cli
```

### From source

```bash
git clone https://github.com/brucestudios/file-sorter.git
cd file-sorter
pip install .
```

## Usage

Basic usage:

```bash
file-sorter /path/to/directory
```

Options:

- `--dry-run`: Show what would be done without moving files.
- `--no-folders`: Do not create folders; just print the category for each file.

Example:

```bash
# Sort files in the current directory
file-sorter

# Sort files in ~/Downloads with a dry run first
file-sorter ~/Downloads --dry-run

# Just see categories without creating folders
file-sorter ~/Desktop --no-folders
```

## Categories

The tool recognizes the following file types:

- **Images**: jpg, jpeg, png, gif, bmp, tiff, webp, svg
- **Documents**: pdf, doc, docx, txt, rtf, odt, md, markdown
- **Spreadsheets**: xls, xlsx, csv
- **Presentations**: ppt, pptx, odp
- **Archives**: zip, rar, 7z, tar, gz, bz2, xz
- **Audio**: mp3, wav, flac, aac, ogg, m4a
- **Video**: mp4, mkv, avi, mov, wmv, flv, webm
- **Code**: py, js, ts, html, css, java, c, cpp, h, cs, php, rb, go, rs, sh, json, xml, yaml, yml
- **Fonts**: ttf, otf, woff, woff2
- **Executables**: exe, msi, app
- **Other**: Any extension not listed above
- **no_extension**: Files without an extension

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Bruce Fang