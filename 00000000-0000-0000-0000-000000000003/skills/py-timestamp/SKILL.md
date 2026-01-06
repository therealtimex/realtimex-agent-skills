---
name: py-timestamp
description: Print a UTC timestamp by running a short Python script via the shell tool.
---

# Python Timestamp

## When to Use
- The user asks for a timestamp or current time and wants it produced by a Python script.

## Workflow
Use this checklist for the task:
- [ ] Locate the script in the skill's `references/` directory
- [ ] Run the script with the `shell` tool
- [ ] Return the output in the required format

## Example
Command (replace the path with the absolute skill path from the skills list):
```
python "/absolute/path/to/skills/py-timestamp/references/py-timestamp.py"
```

## Execution Notes
- The script lives in `references/py-timestamp.py` within this skill directory.
- Use the absolute path from the skills list to run the script.
- Respond exactly in this format: `TIMESTAMP=<value>` (no extra text).
