---
name: document-analyze
description: Use this skill for requests related to document manifest; it provides abilities: 
---

# Analyze Document Skill

This skill provides an approach to analyze manifest document.

## When to Use This Skill

Use this skill when you need to:
- Analyze document
- Get document registry

## Analyze Process

### Step 0: Determine document batch id

Use skill `document-batch` at `document/batch.md` to get batch id of document.

### Step 1: Get registry

Use skill `document-registry` at `document/registry.md` to get registry of document.

### Step 2: Analyze document

Use skill `document-general-analyze` at `branches/general/analyze.md` to analyze document.

## Available Tools

You have access to some system tools:
- **write_file**: Save research plans and findings to local files
- **read_file**: Read local files (e.g., findings saved by subagents)
- **list_files**: See what local files exist in a directory
- **fetch_url**: Fetch content from URLs and convert to markdown (use this for web pages, not read_file)
- **task**: Spawn research subagents with web_search access

And other mcp tools.

## Best Practices

