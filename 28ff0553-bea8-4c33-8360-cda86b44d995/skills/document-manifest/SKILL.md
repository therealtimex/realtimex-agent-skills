---

name: document-analyze
description: Skill for analyzing manifest documents and retrieving their registries.
------------------------------------------------------------------------------------

# Document Analyze Skill

This skill defines the standard workflow for analyzing **manifest documents**.

## When to Use This Skill

Use this skill when you need to:

* Analyze a manifest document
* Retrieve a document registry

## Analysis Workflow

Follow the steps in order:

### Step 0: Determine Document Batch ID

Use the **`document-batch`** skill defined in:

* `document/batch.md`

This step returns the **batch ID** for the document.

---

### Step 1: Get Document Registry

Use the **`document-registry`** skill defined in:

* `document/registry.md`

This step retrieves the registry metadata for the document batch.

---

### Step 2: Analyze Document

Use the **`document-general-analyze`** skill defined in:

* `branches/general/analyze.md`

This step performs the actual document analysis based on the registry and batch data.

## Available Tools

You have access to the following system tools:

* **`write_file`** — Save research plans and findings to local files
* **`read_file`** — Read local files (for example, findings saved by sub-agents)
* **`list_files`** — List files in a directory
* **`fetch_url`** — Fetch web pages and convert them to Markdown (use for URLs only)
* **`task`** — Spawn research sub-agents with web search capabilities

Additional MCP tools may also be available.

## Best Practices

* Always resolve the **batch ID** before accessing registries or analysis steps.
* Treat registry data as read-only input for analysis.
* Keep analysis outputs deterministic and reproducible.
* Store intermediate and final results using `write_file` when appropriate.
