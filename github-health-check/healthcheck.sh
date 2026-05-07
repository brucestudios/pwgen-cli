#!/bin/bash

# OpenClaw Health Check Script
# Performs security hardening and risk-tolerance configuration checks

echo "=== OpenClaw Health Check ==="
echo ""

# Check if running as root (for some checks that require sudo)
if [ "$EUID" -ne 0 ]; then
  echo "Warning: Some checks require sudo privileges. Consider running with sudo."
fi
echo ""

# 1. Firewall status (ufw)
echo "1. Firewall Status (ufw):"
if command -v ufw &> /dev/null; then
  ufw status | head -n 1
  if [ "$(ufw status | grep -i 'Status: active')" ]; then
    echo "  Status: Active"
    echo "  Rules:"
    ufw status numbered | head -n 10
  else
    echo "  Status: Inactive"
  fi
else
  echo "  ufw not installed. Consider installing ufw for firewall management."
fi
echo ""

# 2. SSH Configuration
echo "2. SSH Configuration (/etc/ssh/sshd_config):"
if [ -f /etc/ssh/sshd_config ]; then
  echo "  Checking PermitRootLogin:"
  grep -i '^PermitRootLogin' /etc/ssh/sshd_config | head -n 1
  echo "  Checking PasswordAuthentication:"
  grep -i '^PasswordAuthentication' /etc/ssh/sshd_config | head -n 1
  echo "  Checking Protocol:"
  grep -i '^Protocol' /etc/ssh/sshd_config | head -n 1
else
  echo "  SSH config file not found at /etc/ssh/sshd_config"
fi
echo ""

# 3. System Updates
echo "3. System Updates:"
if [ -f /etc/os-release ]; then
  . /etc/os-release
  echo "  OS: $NAME $VERSION"
  if [ "$ID" = "ubuntu" ] || [ "$ID" = "debian" ]; then
    echo "  Checking for updates (apt):"
    apt-get update 2>/dev/null && apt-get -s upgrade | grep -E '^Inst' | head -n 5
  elif [ "$ID" = "centos" ] || [ "$ID" = "rhel" ] || [ "$ID" = "fedora" ] || [ "$ID" = "rocky" ] || [ "$ID" = "almalinux" ]; then
    echo "  Checking for updates (yum/dnf):"
    if command -v dnf &> /dev/null; then
      dnf check-update 2>/dev/null | head -n 10
    else
      yum check-update 2>/dev/null | head -n 10
    fi
  else
    echo "  Unsupported package manager for automatic update check."
  fi
else
  echo "  Cannot determine OS release."
fi
echo ""

# 4. OpenClaw Cron
echo "4. OpenClaw Cron:"
if command -v openclaw &> /dev/null; then
  echo "  OpenClaw CLI is available."
  # Check if there's a cron job for OpenClaw
  if crontab -l 2>/dev/null | grep -i openclaw &> /dev/null; then
    echo "  Found OpenClaw cron jobs:"
    crontab -l 2>/dev/null | grep -i openclaw
  else
    echo "  No OpenClaw cron jobs found in user's crontab."
    # Check system cron
    if [ -d /etc/cron.d ]; then
      echo "  Checking /etc/cron.d for OpenClaw:"
      ls -la /etc/cron.d/*openclaw* 2>/dev/null || echo "  None found."
    fi
  fi
else
  echo "  OpenClaw CLI not found in PATH."
fi
echo ""

# 5. Version Status
echo "5. Version Status:"
if command -v openclaw &> /dev/null; then
  echo "  OpenClaw version:"
  openclaw --version 2>/dev/null || echo "  Could not retrieve version."
else
  echo "  OpenClaw CLI not installed or not in PATH."
fi
echo ""

echo "=== Health Check Complete ==="
echo "Note: This script provides basic checks. For a comprehensive audit,"
echo "consider using the OpenClaw healthcheck skill or manual inspection."