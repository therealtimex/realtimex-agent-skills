---
name: timestamp-utc
description: Return a structured UTC timestamp payload using the skill script and config.
---

# UTC Timestamp Payload

## When to Use
- The user asks for a structured UTC timestamp payload.
- The user mentions UTC metadata, precision, or weekday.

## Workflow
- [ ] Read `references/config.json` to confirm precision and timezone
- [ ] Run the skill script from `references/` with the shell tool
- [ ] Return the script output exactly as JSON

## Execution
- Read the config:
```
read_file "/absolute/path/to/skills/timestamp-utc/references/config.json"
```
- Run the script:
```
python "/absolute/path/to/skills/timestamp-utc/references/utc_payload.py"
```

## Response Format
- Return the JSON output exactly as printed by the script
- Do not add extra keys

## Notes
- Do not compute the timestamp manually.
- Do not change precision or timezone values from config.
