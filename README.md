# GitHub Profile README Generator

A Python CLI tool to generate a GitHub profile README markdown easily.

## Features

- Simple command-line interface
- Customizable sections: bio, location, website, twitter, GitHub link
- Add technologies and projects
- Output to file or stdout

## Installation

```bash
pip install github-profile-readme-gen
```

## Usage

```bash
github-readme-gen USERNAME [options]
```

### Options

- `-b, --bio TEXT`           Short bio (default: "")
- `-l, --location TEXT`      Location (default: "")
- `-w, --website TEXT`       Personal website (default: "")
- `-t, --twitter TEXT`       Twitter handle (without @) (default: "")
- `-g, --github-link TEXT`   GitHub profile link (default: "")
- `--technologies TECH [TECH ...]`  List of technologies (default: [])
- `--projects PROJECT [PROJECT ...]` List of projects (default: [])
- `-o, --output FILE`        Output file (default: stdout)

### Example

```bash
github-readme-gen brucestudios \
    --bio "Passionate developer and open source enthusiast" \
    --location "Shanghai, China" \
    --website "https://brucestudios.github.io" \
    --twitter brucestudios \
    --github-link https://github.com/brucestudios \
    --technologies Python JavaScript Jekyll \
    --projects "Awesome Jekyll CLI" "OpenClaw Assistant" \
    --output README.md
```

This will generate a README.md file with the provided information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Bruce Fang (henshao.fang@outlook.com)