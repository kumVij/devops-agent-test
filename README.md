# devops-agent-test-v2 — Multi-error test project

This project has **5 intentional bugs across 5 files** to test the AI agent's
ability to handle multiple different error types in a single CI run.

## Bug map

| File | Error type | What's wrong |
|---|---|---|
| `app.py` | `dependency_missing` | `import requests` — not in requirements.txt |
| `config/settings.py` | `env_var_missing` | `os.environ["DATABASE_URL"]` — not set in CI |
| `services/order.py` | `syntax_error` | Missing `:` after `if not validate_order(items)` |
| `services/payment.py` | `test_failure` | `tax_rate = "0.18"` (str) causes TypeError |
| `utils/calculator.py` | `test_failure` | `apply_discount` divides instead of subtracts |

## What the AI agent should detect

The CI pipeline will fail on the **first error it hits** (syntax error or import error).
The agent receives the full log and should identify:

1. Primary error: whichever fails first in pytest collection
2. Root cause: the specific line and reason
3. Fix: minimal patch to resolve it

## Project structure

```
devops-agent-test-v2/
├── app.py                    ← missing import
├── requirements.txt          ← missing requests
├── config/
│   └── settings.py           ← missing env var
├── services/
│   ├── order.py              ← syntax error
│   └── payment.py            ← type error
├── utils/
│   ├── calculator.py         ← wrong business logic
│   └── validator.py          ← correct (no bugs)
└── tests/
    ├── test_calculator.py    ← catches calculator bug
    └── test_payment.py       ← catches payment bug
```