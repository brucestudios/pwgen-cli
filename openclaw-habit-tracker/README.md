# OpenClaw Habit Tracker

A simple command-line habit tracker built for OpenClaw users to track daily habits and maintain consistency.

## Features

- Track multiple habits with daily check-ins
- View streak counts and completion rates
- Simple JSON-based storage
- Colorful terminal output
- Easy to use commands

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/openclaw-habit-tracker.git
cd openclaw-habit-tracker
```

2. Make the script executable:
```bash
chmod +x habit.py
```

3. (Optional) Add to your PATH for global access:
```bash
# Add to your .bashrc or .zshrc
export PATH="$PATH:/path/to/openclaw-habit-tracker"
```

## Usage

### Adding a new habit
```bash
./habit.py add "Read 30 minutes"
```

### Marking a habit as done for today
```bash
./habit.py done "Read 30 minutes"
```

### Viewing all habits and their status
```bash
./habit.py list
```

### Viewing detailed statistics
```bash
./habit.py stats
```

### Removing a habit
```bash
./habit.py remove "Read 30 minutes"
```

## Storage

Habits and their completion data are stored in `habits.json` in the application directory. The file contains:
- Habit names
- Creation dates
- Completion dates (as ISO strings)

## Example

```bash
$ ./habit.py add "Exercise"
Added habit: Exercise

$ ./habit.py add "Meditate"
Added habit: Meditate

$ ./habit.py list
📋 Habits:
  • Exercise (created: 2026-05-03) [✓ Today]
  • Meditate (created: 2026-05-03) [○ Not done today]

$ ./habit.py done "Meditate"
✅ Marked Meditate as done for today

$ ./habit.py stats
📊 Statistics:
  Exercise: 1/1 days (100.0%)
  Meditate: 1/1 days (100.0%)
  Total: 2 habits, 2/2 completions today (100.0%)
```

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## License

MIT License - feel free to modify and distribute!