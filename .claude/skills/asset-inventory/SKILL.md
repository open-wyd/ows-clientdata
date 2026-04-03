---
name: asset-inventory
description: "Audit WYD asset inventory: summarize directory size/count and validate index references in Mesh/MeshList.txt and Sound/soundlist.txt."
---

Run each step and report findings clearly in English.

## 1. Directory Size Summary
```bash
du -sh Mesh/ UI/ Effect/ Sound/ music/ Env/ NUI/ shader/
```

## 2. File Count By Directory
```bash
for dir in Mesh UI Effect Sound music Env NUI shader; do
  count=$(find "$dir" -type f | wc -l)
  echo "$dir: $count files"
done
```

## 3. Check Broken References In Mesh/MeshList.txt
Read the file `Mesh/MeshList.txt`, extract all file references, normalize each path before checking it on disk, and only then report broken references. The normalization must:
- convert Windows separators `\\` to `/`
- treat prefixes case-insensitively
- remove a leading `mesh/` prefix when present and resolve the file under `Mesh/`
- map a leading `effect/` prefix to the `Effect/` directory and resolve the remaining relative path there

After normalization, check whether each referenced file exists in the correct base directory (`Mesh/` for `mesh/...`, `Effect/` for `effect/...`). Report only entries that still have no matching file on disk after this normalization.

## 4. Check Broken References In Sound/soundlist.txt
Read the file `Sound/soundlist.txt`, extract all file references, normalize each path before checking it on disk, and only then report broken references. The normalization must:
- convert Windows separators `\\` to `/`
- treat prefixes case-insensitively
- remove a leading `sound/` prefix when present and resolve the file under `Sound/`

After normalization, check whether each referenced file exists in the correct base directory (`Sound/`). Report only entries that still have no matching file on disk after this normalization.

## Expected Output
Provide a summary with:
- Directory size and file-count table
- Broken-reference list for `Mesh/MeshList.txt` after path normalization and correct `Mesh/` or `Effect/` resolution (or "none found")
- Broken-reference list for `Sound/soundlist.txt` after path normalization and correct `Sound/` resolution (or "none found")
