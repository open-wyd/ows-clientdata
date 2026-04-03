---
name: config-text-query
description: "Fast, low-cost queries over WYD client text files: Config.ini, Lang.txt, and UI/command.txt. Use to locate settings, strings, and slash commands without reading whole files."
argument-hint: "What do you want to find? (e.g., resolution, command, PT-BR string)"
---

# Config And Text Query

## When To Use
- Find a key in `Config.ini`
- Search terms in `Lang.txt`
- Find commands in `UI/command.txt`

## Procedure
1. Use targeted search before full reads.
2. If there is a match, read only nearby lines.
3. Return value, context, and source file.

## Rules
- Do not open binary files.
- Avoid full-file reads when not required.

## Expected Output
- Queried file
- Matching excerpt
- Interpretation in PT-BR
