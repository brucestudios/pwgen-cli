#!/usr/bin/env python3
"""
Daily Motivational Quote
A simple command-line tool that prints a random motivational quote.
"""

import random

QUOTES = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Innovation distinguishes between a leader and a follower. – Steve Jobs",
    "Your time is limited, don't waste it living someone else's life. – Steve Jobs",
    "Stay hungry, stay foolish. – Steve Jobs",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "It is during our darkest moments that we must focus to see the light. – Aristotle",
    "Whoever is happy will make others happy too. – Anne Frank",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. – Ralph Waldo Emerson",
    "When you reach the end of your rope, tie a knot in it and hang on. – Franklin D. Roosevelt",
    "Always remember that you are absolutely unique. Just like everyone else. – Margaret Mead",
    "Don't judge each day by the harvest you reap but by the seeds that you plant. – Robert Louis Stevenson",
    "The only limit to our realization of tomorrow will be our doubts of today. – Franklin D. Roosevelt",
    "We can do anything we want to if we stick to it long enough. – Helen Keller",
    "Everything you’ve ever wanted is on the other side of fear. – George Addair",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Act as if what you do makes a difference. It does. – William James",
    "The best time to plant a tree was 20 years ago. The second best time is now. – Chinese Proverb",
    "Yesterday is history, tomorrow is a mystery, today is a gift of God, which is why we call it the present. – Bil Keane",
    "Life is what happens when you're busy making other plans. – John Lennon"
]

def main():
    """Print a random motivational quote."""
    quote = random.choice(QUOTES)
    print(quote)

if __name__ == "__main__":
    main()