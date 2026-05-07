#!/bin/bash
# System Monitor Script
# Monitors system resources (CPU, Memory, Disk) and sends alerts if thresholds are exceeded.

# Configuration
CPU_THRESHOLD=80       # Percentage
MEMORY_THRESHOLD=80    # Percentage
DISK_THRESHOLD=90      # Percentage
ALERT_EMAIL="admin@example.com"  # Change to your email
LOG_FILE="/var/log/system_monitor.log"

# Colors for output (if supported)
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

check_cpu() {
    local cpu_usage
    cpu_usage=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
    cpu_usage=${cpu_usage%.*}  # Remove decimal part
    
    if [ "$cpu_usage" -ge "$CPU_THRESHOLD" ]; then
        log_message "${RED}ALERT: CPU usage is ${cpu_usage}% (threshold: ${CPU_THRESHOLD}%)${NC}"
        # Send email alert (requires mailutils or similar)
        echo "CPU usage high: ${cpu_usage}%" | mail -s "System Alert: High CPU Usage" "$ALERT_EMAIL"
    else
        log_message "${GREEN}CPU usage: ${cpu_usage}%${NC}"
    fi
}

check_memory() {
    local mem_usage
    mem_usage=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
    mem_usage=${mem_usage%.*}
    
    if [ "$mem_usage" -ge "$MEMORY_THRESHOLD" ]; then
        log_message "${RED}ALERT: Memory usage is ${mem_usage}% (threshold: ${MEMORY_THRESHOLD}%)${NC}"
        echo "Memory usage high: ${mem_usage}%" | mail -s "System Alert: High Memory Usage" "$ALERT_EMAIL"
    else
        log_message "${GREEN}Memory usage: ${mem_usage}%${NC}"
    fi
}

check_disk() {
    local disk_usage
    disk_usage=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
    
    if [ "$disk_usage" -ge "$DISK_THRESHOLD" ]; then
        log_message "${RED}ALERT: Disk usage is ${disk_usage}% (threshold: ${DISK_THRESHOLD}%)${NC}"
        echo "Disk usage high: ${disk_usage}%" | mail -s "System Alert: High Disk Usage" "$ALERT_EMAIL"
    else
        log_message "${GREEN}Disk usage: ${disk_usage}%${NC}"
    fi
}

main() {
    log_message "Starting system monitor check..."
    check_cpu
    check_memory
    check_disk
    log_message "System monitor check completed."
    echo "---"
}

# If script is called directly, run main
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi