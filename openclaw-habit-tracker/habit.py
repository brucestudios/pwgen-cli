#!/usr/bin/env python3
"""
OpenClaw Habit Tracker
A simple command-line habit tracker for tracking daily habits.
"""

import json
import os
import sys
from datetime import datetime, date
from pathlib import Path

# Constants
DATA_FILE = "habits.json"

def load_habits():
    """Load habits from JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_habits(habits):
    """Save habits to JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(habits, f, indent=2)

def add_habit(name):
    """Add a new habit."""
    habits = load_habits()
    
    if name in habits:
        print(f"❌ Habit '{name}' already exists!")
        return False
    
    habits[name] = {
        "created": str(date.today()),
        "completions": []  # List of completion dates as strings
    }
    
    save_habits(habits)
    print(f"✅ Added habit: {name}")
    return True

def mark_done(name):
    """Mark a habit as done for today."""
    habits = load_habits()
    
    if name not in habits:
        print(f"❌ Habit '{name}' not found!")
        return False
    
    today_str = str(date.today())
    completions = habits[name]["completions"]
    
    if today_str in completions:
        print(f"✅ Habit '{name}' already marked as done for today!")
        return False
    
    completions.append(today_str)
    # Keep completions sorted
    completions.sort()
    
    save_habits(habits)
    print(f"✅ Marked {name} as done for today")
    return True

def list_habits():
    """List all habits with their status."""
    habits = load_habits()
    
    if not habits:
        print("📭 No habits tracked yet. Use 'add' to create a new habit.")
        return
    
    today_str = str(date.today())
    print("📋 Habits:")
    
    for name, data in habits.items():
        created = data["created"]
        completions = data["completions"]
        
        # Check if done today
        done_today = today_str in completions
        status = "✓ Today" if done_today else "○ Not done today"
        
        # Calculate streak
        streak = calculate_streak(completions)
        streak_str = f" (streak: {streak})" if streak > 0 else ""
        
        print(f"  • {name} (created: {created}) [{status}]{streak_str}")

def show_stats():
    """Show statistics for all habits."""
    habits = load_habits()
    
    if not habits:
        print("📭 No habits tracked yet. Use 'add' to create a new habit.")
        return
    
    today_str = str(date.today())
    print("📊 Statistics:")
    
    total_habits = len(habits)
    total_completions_today = 0
    
    for name, data in habits.items():
        completions = data["completions"]
        created_date = datetime.strptime(data["created"], "%Y-%m-%d").date()
        days_tracked = (date.today() - created_date).days + 1
        completion_count = len(completions)
        
        if days_tracked > 0:
            rate = (completion_count / days_tracked) * 100
        else:
            rate = 0
        
        done_today = today_str in completions
        if done_today:
            total_completions_today += 1
        
        print(f"  {name}: {completion_count}/{days_tracked} days ({rate:.1f}%)")
    
    if total_habits > 0:
        today_rate = (total_completions_today / total_habits) * 100
        print(f"  Total: {total_habits} habits, {total_completions_today}/{total_habits} completions today ({today_rate:.1f}%)")

def remove_habit(name):
    """Remove a habit."""
    habits = load_habits()
    
    if name not in habits:
        print(f"❌ Habit '{name}' not found!")
        return False
    
    del habits[name]
    save_habits(habits)
    print(f"🗑️  Removed habit: {name}")
    return True

def calculate_streak(completions):
    """Calculate current streak of consecutive days."""
    if not completions:
        return 0
    
    # Convert strings to date objects and sort
    dates = [datetime.strptime(d, "%Y-%m-%d").date() for d in completions]
    dates.sort()
    
    # Check from today backwards
    today = date.today()
    streak = 0
    check_date = today
    
    for d in reversed(dates):
        if d == check_date:
            streak += 1
            check_date = date.fromordinal(check_date.toordinal() - 1)
        elif d < check_date:
            break
    
    return streak

def print_usage():
    """Print usage information."""
    print("""
OpenClaw Habit Tracker

Usage:
  habit.py add <habit_name>     - Add a new habit
  habit.py done <habit_name>    - Mark habit as done for today
  habit.py list                 - List all habits
  habit.py stats                - Show statistics
  habit.py remove <habit_name>  - Remove a habit
  habit.py help                 - Show this help

Examples:
  habit.py add "Read 30 minutes"
  habit.py done "Read 30 minutes"
  habit.py list
  habit.py stats
""")

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print_usage()
        return
    
    command = sys.argv[1].lower()
    
    if command == "add":
        if len(sys.argv) < 3:
            print("❌ Please provide a habit name")
            print("Usage: habit.py add <habit_name>")
            return
        habit_name = " ".join(sys.argv[2:])
        add_habit(habit_name)
    
    elif command == "done":
        if len(sys.argv) < 3:
            print("❌ Please provide a habit name")
            print("Usage: habit.py done <habit_name>")
            return
        habit_name = " ".join(sys.argv[2:])
        mark_done(habit_name)
    
    elif command == "list":
        list_habits()
    
    elif command == "stats":
        show_stats()
    
    elif command == "remove":
        if len(sys.argv) < 3:
            print("❌ Please provide a habit name")
            print("Usage: habit.py remove <habit_name>")
            return
        habit_name = " ".join(sys.argv[2:])
        remove_habit(habit_name)
    
    elif command == "help":
        print_usage()
    
    else:
        print(f"❌ Unknown command: {command}")
        print_usage()

if __name__ == "__main__":
    main()