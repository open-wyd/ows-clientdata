# Readable Files In The WYD Repository

Complete list of text files that can be safely read.

## Project Root

| File | Content |
|------|---------|
| `Config.ini` | Display mode, resolution, volume, controls, gameplay |
| `Lang.txt` | Client language strings (PT-BR) |
| `README.md` | General documentation: project overview and contribution notes |
| `CLAUDE.md` | AI-agent guide: architecture, file formats, and run instructions |
| `test.cmd` | Debug script with preconfigured credentials |

## Mesh/

| File | Content |
|------|---------|
| `Mesh/MeshList.txt` | Mesh index and paths: `<ID> <path>` |

## Sound/

| File | Content |
|------|---------|
| `Sound/soundlist.txt` | Sound index: `<ID> <path> <type>` |

## UI/

| File | Content |
|------|---------|
| `UI/command.txt` | Available slash commands (PT-BR with hex-color prefixes) |

## docs/

Additional Markdown documentation. Use `list_dir docs/` to discover files.

## .github/

| File | Content |
|------|---------|
| `.github/copilot-instructions.md` | AI context instructions for this project |

## What NOT To Read

| Extension | Format | Reason |
|-----------|--------|--------|
| `.bin` | WYD proprietary serialized data | Unreadable, token waste |
| `.dat` | Terrain/binary data | Unreadable |
| `.wyt` | WYD texture format | Proprietary image format |
| `.wys` | WYD effect definition | Proprietary binary format |
| `.msa` / `.msh` | WYD mesh/skeleton format | Proprietary 3D binary |
| `.trn` | WYD terrain format | Proprietary binary |
| `.wav` | PCM audio | Binary audio file |
| `.mp3` | Compressed audio | Binary audio file |
