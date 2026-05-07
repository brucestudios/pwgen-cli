# mdtable-cli

A command-line interface tool to convert markdown tables to HTML tables.

## Installation

```bash
npm install -g mdtable-cli
```

## Usage

### Convert a markdown file to HTML

```bash
mdtable convert input.md -o output.html
```

### Convert markdown table string to HTML (inline)

```bash
mdtable inline "| Header | Value |\n|--------|-------|\n| A      | B     |"
```

## Features

- Converts markdown tables with headers to HTML `<thead>` and `<tbody>`
- Handles tables without headers (treats first row as data)
- Properly escapes HTML entities in table cells
- Supports both file input and inline string conversion

## Examples

Given a markdown file `example.md`:

```markdown
| Name | Age | City      |
|------|-----|-----------|
| John | 25  | New York  |
| Jane | 30  | London    |
```

Running:

```bash
mdtable convert example.md
```

Outputs:

```html
<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Age</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>John</td>
      <td>25</td>
      <td>New York</td>
    </tr>
    <tr>
      <td>Jane</td>
      <td>30</td>
      <td>London</td>
    </tr>
  </tbody>
</table>
```

## License

ISC