# WYD Client Data - Repository Context

WYD client asset repository (open-source MMORPG). This repository does not contain source code.
Primary project language is PT-BR.

## Never Read Binary Files

Proprietary/unreadable extensions that waste tokens:
`.bin` `.dat` `.wyt` `.wys` `.msa` `.msh` `.trn` `.wav` `.mp3`

## Readable Text Files

| File | Content |
|------|---------|
| `Config.ini` | Display, resolution, volume, gameplay settings |
| `Lang.txt` | Client language strings |
| `UI/command.txt` | In-game slash commands (PT-BR) |
| `Mesh/MeshList.txt` | Mesh index: `<ID> <path>` |
| `Sound/soundlist.txt` | Sound index: `<ID> <path> <type>` |
| `README.md`, `CLAUDE.md` | Project documentation |
| `docs/**/*.md` | Additional documentation |

## Directory Map

```
Mesh/        335 MB   3D models (.msa, .msh) -> use MeshList.txt as index
UI/           65 MB   Interface (.wyt) -> use command.txt for slash commands
Sound/        38 MB   Audio (.wav) -> use soundlist.txt as index
Effect/       18 MB   Effects (.wys, .msa) -> no index, use list_dir
Env/          16 MB   Maps and textures
music/        79 MB   Music (.mp3, .wav)
shader/       --      GPU shaders (.bin)
NUI/           5 MB   New UI resources
```

## Skills

Use these skills to keep context small and improve precision:

| Skill | Use when | Keywords |
|------|----------|----------|
| `wyd-navigation` | Locate meshes/sounds/effects/configs/strings | `find mesh`, `find sound`, `find effect`, `search WYD assets` |
| `config-text-query` | Query `Config.ini`, `Lang.txt`, `UI/command.txt` | `config key`, `lang string`, `slash command` |
| `index-health-check` | Check index consistency and broken paths | `audit index`, `duplicates`, `broken path` |
| `asset-inventory` | Audit folder size/count and index references | `asset inventory`, `directory size`, `broken references` |

Search rule: use `grep_search` before `read_file`. For assets, prefer text indexes over large directory scans.

## Running The Client

```cmd
WYD.exe
test.cmd
```
