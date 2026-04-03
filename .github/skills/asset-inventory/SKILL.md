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
Read the file `Mesh/MeshList.txt`, extract all file references, and for each one check if the file exists under `Mesh/`. Report any entries that have no matching file on disk.

## 4. Check Broken References In Sound/soundlist.txt
Read the file `Sound/soundlist.txt`, extract all file references, and for each one check if the file exists under `Sound/`. Report any entries that have no matching file on disk.

## Expected Output
Provide a summary with:
- Directory size and file-count table
- Broken-reference list for `Mesh/MeshList.txt` (or "none found")
- Broken-reference list for `Sound/soundlist.txt` (or "none found")
