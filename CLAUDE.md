# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a game client asset repository for **open-wyd** (WYD / Wizard's Heart), an open-source MMORPG. There is no source code, build pipeline, or test suite — the repository contains the game client binary (`WYD.exe`) and all data/assets it loads at runtime.

The repository is Portuguese-language (all in-game text, configuration comments, and documentation are in PT-BR).

## Running the Client

```cmd
WYD.exe
```

For debug mode with pre-set credentials:
```cmd
test.cmd
```
This launches `WYD-debug.exe` with hardcoded username/password/sessionid from `test.cmd`.

## Architecture

The client reads binary data files and assets from specific directories relative to `WYD.exe`. All paths are relative — do not restructure directories.

### Binary Game Data (`*.bin`, `*.dat`)
Serialized databases loaded at startup:
- `Itemlist.bin` / `Itemname.bin` — item definitions and display names
- `Mixlist.bin` — crafting recipes
- `SkillData.bin` — skill definitions
- `MountData.bin` — mount/pet data
- `object.bin` — world object definitions
- `HeightMap.dat` / `AttributeMap.dat` — terrain data
- `Env/Field*.dat` / `Env/Field*.trn` — map field data
- `Env/Character.dat` — character appearance data
- `serverlist.bin` — server connection list

### Asset Directories
- `Mesh/` (335MB) — 3D models (`.msa`, `.msh`); indexed by `Mesh/MeshList.txt`
- `UI/` (65MB) — interface textures (`.wyt`) and layout data; `UI/command.txt` documents in-game slash commands
- `Effect/` (18MB) — visual effects (`.wys`, `.msa`)
- `Sound/` (38MB) — audio effects (`.wav`); indexed by `Sound/soundlist.txt`
- `music/` (79MB) — background music (`.mp3`, `.wav`)
- `Env/` (16MB) — environment textures and map data
- `NUI/` (4.7MB) — new UI resources
- `shader/` — GPU shader programs (`.bin`)

### Configuration
`Config.ini` controls display mode, resolution, volume, and gameplay settings. Currently configured for windowed mode with classic controls.

## Available Skills (PT-BR + EN)

Use the skills below for targeted tasks to reduce token usage while keeping output quality high.

| Skill | Use when | Keywords |
|-------|----------|----------|
| `wyd-navigation` (`.claude/skills/wyd-navigation/`) | Locate meshes, sounds, effects, configs, and language strings | `find mesh`, `find sound`, `find effect`, `read config`, `search WYD assets` |
| `config-text-query` (`.claude/skills/config-text-query/`) | Query `Config.ini`, `Lang.txt`, `UI/command.txt` with minimal reads | `config key`, `lang string`, `slash command`, `resolution` |
| `index-health-check` (`.claude/skills/index-health-check/`) | Validate `MeshList.txt` and `soundlist.txt` consistency | `audit index`, `duplicates`, `invalid lines`, `broken path` |
| `asset-inventory` (`.claude/skills/asset-inventory/`) | Directory size/count audit and broken-reference checks | `asset inventory`, `directory size`, `broken references` |

**Search rule:** always use `grep_search` before `read_file`. For assets, prefer indexes (`Mesh/MeshList.txt`, `Sound/soundlist.txt`) over large directory listing.

**Output language:** final user-facing responses should stay in PT-BR unless explicitly requested otherwise.

## Claude Automation

### Dependency

- **Required**: `python3` - used by hooks and by the environment validator.

The hook in `.claude/settings.json` blocks accidental edits to binary asset files (`.bin`, `.dat`, `.wyt`, `.wys`, `.msa`, `.msh`, `.trn`, `.wav`, `.mp3`). It tries `python3` first and uses `py -3` as a Windows fallback.

### Validate Environment

```bash
python3 .claude/scripts/validate-claude-env.py
```

On Windows, if `python3` is not in PATH:
```cmd
py -3 .claude/scripts/validate-claude-env.py
```

If Python is not installed, the validation script provides installation guidance.

## File Format Notes

- `.bin` files are proprietary binary formats specific to WYD; they are not standard formats
- `.wyt` are WYD texture files (not standard image formats)
- `.wys` are WYD effect definition files
- `.msa` / `.msh` are WYD mesh/skeleton formats
- Text files (`.txt`) within asset directories are plain-text index/list files, not source code

## Known Issues

`clientlogs.log` shows `Error in Init Render Target Texture` on startup — this is a pre-existing rendering initialization issue.
