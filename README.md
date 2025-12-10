# Agent Skills Repository

Central repository for agent skill definitions with automated release packaging.

**DEMONSTRATE ONLY** - This repository contains template skills for testing the release workflow.

## Repository Structure

```
repo-root/
  {agent-uuid}/
    skills/
      {skill-name}/
        SKILL.md
    docs/
      {skill-name}/
        readme.md
  .github/
    workflows/
      release-packaging.yml
```

## Agent Folder Structure

Each agent folder:
- Named with a valid UUID (format: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`)
- Contains `skills/` directory with skill subfolders, each having a `SKILL.md` file
- Contains `docs/` directory with documentation subfolders matching skills structure

## Adding a New Agent

1. Generate a UUID:
   ```bash
   uuidgen | tr '[:upper:]' '[:lower:]'
   ```

2. Create the folder structure:
   ```bash
   mkdir -p {uuid}/skills/{skill-name}
   mkdir -p {uuid}/docs/{skill-name}
   ```

3. Add your files:
   - `skills/{skill-name}/SKILL.md` - Agent skill definition
   - `docs/{skill-name}/readme.md` - Documentation

4. Commit and push:
   ```bash
   git add {uuid}
   git commit -m "Add agent: {uuid}"
   git push
   ```

## Release Process

1. Create and push a tag:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

2. Create a release on GitHub using the tag

3. The workflow automatically packages each agent into `{uuid}.zip` and uploads as release assets

## Downloading Agents

```
https://github.com/{owner}/{repo}/releases/download/{tag}/{uuid}.zip
```

## Sample Agents

- **00000000-0000-0000-0000-000000000001**: Customer Support (customer-support, ticket-management)
- **00000000-0000-0000-0000-000000000002**: Creative Tools (algorithmic-art, canvas-design)

All sample content is for demonstration only.