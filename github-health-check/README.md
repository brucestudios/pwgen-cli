# OpenClaw Health Check

A tool to perform security hardening and risk-tolerance configuration checks for OpenClaw deployments.

## Usage

Run the script to perform a health check:

```bash
./healthcheck.sh
```

## What it checks

- Firewall status (ufw)
- SSH configuration
- System updates
- OpenClaw cron scheduling
- Version status

## Requirements

- Bash
- sudo privileges for some checks

## License

MIT