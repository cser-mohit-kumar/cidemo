import os
import sys

def main():
    # Retrieve the secret from the environment variable
    secret = os.environ.get("MY_SECRET_TOKEN")
    
    if not secret:
        print("❌ Error: MY_SECRET_TOKEN environment variable is not set!")
        print("Please check the README.md to configure your GitHub Secrets.")
        sys.exit(1)
    
    print("✅ Successfully accessed the secret token!")
    print(f"Secret length: {len(secret)} characters")
    
    # Demonstrate GitHub Actions log masking
    # If the secret is printed, GitHub Actions automatically masks it with asterisks (***)
    print(f"Attempting to print the secret (GitHub should automatically mask this): {secret}")

if __name__ == "__main__":
    main()
