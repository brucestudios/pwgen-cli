# OpenClaw Skill CLI

A command-line utility to manage OpenClaw skills from ClawHub.

## Features

- List available skills from ClawHub
- Install a skill from ClawHub
- Update an installed skill from ClawHub
- Publish a skill to ClawHub

## Installation

You can install the CLI globally via npm:

```bash
npm install -g openclaw-skill-cli
```

Or clone the repository and link it locally:

```bash
git clone https://github.com/brucestudios/openclaw-skill-cli.git
cd openclaw-skill-cli
npm link
```

## Usage

List available skills:

```bash
oc-skill list
```

Install a skill:

```bash
oc-skill install <skill-name>
```

Update a skill:

```bash
oc-skill update <skill-name>
```

Publish a skill:

```bash
oc-skill publish <skill-directory>
```

## Requirements

- Node.js (>=18.0.0)
- ClawHub CLI installed globally (`npm install -g clawhub`)

## License

MIT