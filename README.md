# devops-agent-test

Test repository for the DevOps AI Agent.

This repo intentionally contains bugs that trigger the AI agent's
CI/CD monitoring and auto-fix pipeline.

## How it works

1. Push code to this repo
2. GitHub Actions runs the test suite
3. If tests fail, the AI agent webhook fires
4. Agent diagnoses the failure and suggests or applies a fix

## Running locally

```bash
pip install -r requirements.txt
pytest tests/ -v
```