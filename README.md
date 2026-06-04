# GitHub Secrets Demonstration Project

This is a bare minimum project designed to illustrate how to store and safely use secrets (like API keys, tokens, or passwords) in GitHub Secrets.

## How it Works

1. **Storage**: The secret is securely stored in your GitHub repository's settings under **Secrets and variables**.
2. **Injection**: When a GitHub Actions workflow runs, it retrieves the secret from GitHub's storage and injects it as an environment variable (`MY_SECRET_TOKEN`) into the runner environment.
3. **Usage**: The Python script ([verify_secret.py](file:///home/mohit/training/devsecops/secret/verify_secret.py)) reads the environment variable and uses it.
4. **Masking**: GitHub automatically masks any outputs in the workflow logs that match the secret value, replacing them with `***` to prevent accidental exposure.

---

## Step-by-Step Setup Guide

### 1. Store the Secret in GitHub

Before running the project on GitHub, you need to add your secret:

1. Push this repository to GitHub.
2. Go to your repository on GitHub.
3. Click on the **Settings** tab.
4. In the left sidebar, expand **Secrets and variables** and click **Actions**.
5. Click the **New repository secret** button.
6. Enter the following details:
   - **Name**: `MY_SECRET_TOKEN`
   - **Secret**: `SuperSecret123Value` (or any token/string you wish to use)
7. Click **Add secret**.

### 2. Trigger the Workflow

The workflow is configured to run automatically when you push code to `main`/`master`, or it can be run manually:

1. In your GitHub repository, click on the **Actions** tab.
2. Under **Workflows** in the left sidebar, click **GitHub Secrets Demonstration**.
3. Click the **Run workflow** dropdown on the right.
4. Click the green **Run workflow** button.

### 3. Inspect the Output

Once the run completes, click on the workflow run to view the logs:

1. Click on the **demonstrate-secrets** job.
2. Expand the **Run script with Secret injected** step.
3. You will see output similar to this:
   ```text
   ✅ Successfully accessed the secret token!
   Secret length: 19 characters
   Attempting to print the secret (GitHub should automatically mask this): ***
   ```
   > [!NOTE]
   > Notice how the actual secret value `SuperSecret123Value` was automatically replaced with `***` in the logs by GitHub's built-in log mask security feature!

---

## File Structure

- [.github/workflows/demo.yml](file:///home/mohit/training/devsecops/secret/.github/workflows/demo.yml): The GitHub Actions workflow file that runs the demonstration job and handles injecting the secret into the environment.
- [verify_secret.py](file:///home/mohit/training/devsecops/secret/verify_secret.py): The Python script that accesses the secret via environment variables and validates its presence.
