---
name: wyd-navigation
description: "Navigate the WYD asset repository efficiently without wasting tokens. Use to locate meshes by ID, find sounds, find visual effects, read client settings, check language strings, list asset directories, or answer WYD asset lookup requests."
argument-hint: "What do you want to locate? (e.g., mesh ID 42, monster sound, resolution setting)"
---

# WYD Client Data Navigation

## Core Rule

Never read binary files. Forbidden extensions: `.bin`, `.dat`, `.wyt`, `.wys`, `.msa`, `.msh`, `.trn`, `.wav`, `.mp3`

Opening them wastes tokens and returns unreadable data.

## Readable Files Map

See [readable-files.md](./references/readable-files.md) for the full readable-file list and descriptions.

## Procedures By Query Type

### Find A Mesh Or 3D Model
1. Use `grep_search` in `Mesh/MeshList.txt` to avoid full-file reads.
2. Index format: `<ID> <relative_path>`.
3. Physical files are under `Mesh/` or `Effect/` depending on indexed path.
4. If name lookup fails, use `read_file` on relevant line ranges.

### Find A Sound
1. Use `grep_search` in `Sound/soundlist.txt`.
2. Index format: `<ID> <relative_path> <type>`.
3. Example: `10 sound\\monster\\wgolatt.wav 1`.

### Find A Visual Effect
1. Use `grep_search` in `Effect/` for `.wys` names.
2. Alternatively, use `list_dir Effect/` to inspect available effects.
3. There is no effect index file, so navigate by filename.
4. `.wys` files are effect definitions; `.msa` files are effect geometry.

### Read In-Game Slash Commands
1. Read `UI/command.txt` (text file in PT-BR encoding).
2. Format: hex color followed by command text.

### Check Client Configuration
1. Read root `Config.ini`.

### Check Language Strings / Game Text
1. Use `grep_search` in `Lang.txt` to avoid full reads.
2. If broad context is required, read specific ranges with `read_file`.

### Explore Asset Directories
- `Effect/`: use `list_dir` to inspect available effects.
- `Mesh/`: prefer `grep_search` in `MeshList.txt`.
- `Sound/`: prefer `grep_search` in `soundlist.txt`.
- `UI/`: use `list_dir` for `.wyt` textures and other resources.
- `NUI/`: use `list_dir` for new UI resources.
- `music/`: use `list_dir` to inspect music filenames.

### Consult Project Documentation
1. For overview: read `CLAUDE.md` (architecture, formats, run info).
2. For additional docs: use `list_dir docs/` and read relevant files.

## Token-Efficient Strategy

| Task | Efficient Approach |
|------|--------------------|
| Search by name | `grep_search` before `read_file` |
| Confirm file exists | `file_search` with glob |
| List large directory | `list_dir` and filter manually |
| Read part of large file | `read_file` with line ranges |
| Check broken references | Use `asset-inventory` skill |
