import re
import sys
import argparse

def check_password(password):
    """Check password strength and return a score and feedback."""
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 20
    else:
        feedback.append("Too short (minimum 8 characters)")

    # Character variety
    if re.search(r'[a-z]', password):
        score += 20
    else:
        feedback.append("Add lowercase letters")

    if re.search(r'[A-Z]', password):
        score += 20
    else:
        feedback.append("Add uppercase letters")

    if re.search(r'\\d', password):
        score += 20
    else:
        feedback.append("Add numbers")

    if re.search(r'[!@#$%^&*(),.?\\":{}|<>]', password):
        score += 20
    else:
        feedback.append("Add special characters (!@#$%^&*(),.?\\\":{}|<>)")

    # Common patterns (optional)
    # We can add more checks like common passwords, sequences, etc.
    # For simplicity, we'll skip.

    return score, feedback

def main():
    parser = argparse.ArgumentParser(description="Check the strength of a password.")
    parser.add_argument('password', nargs='?', help="Password to check. If omitted, you will be prompted.")
    args = parser.parse_args()

    if args.password:
        password = args.password
    else:
        # Prompt for password (hidden input)
        import getpass
        password = getpass.getpass("Enter password to check: ")

    score, feedback = check_password(password)

    if score == 100:
        print(f"✅ Strong password (score: {score}/100)")
    else:
        print(f"❌ Weak password (score: {score}/100)")
        if feedback:
            print("Feedback:")
            for line in feedback:
                print(f"- {line}")

if __name__ == "__main__":
    main()