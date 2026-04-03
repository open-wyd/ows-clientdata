---
name: index-health-check
description: "Check WYD asset index health with focus on consistency and low cost: Mesh/MeshList.txt and Sound/soundlist.txt. Detects invalid lines, duplicates, and potentially broken paths."
argument-hint: "Audit mesh, sound, or both?"
---

# Index Health Check

## Targets
- `Mesh/MeshList.txt`
- `Sound/soundlist.txt`

## Checks
1. Invalid-format lines.
2. Duplicate IDs.
3. Duplicate paths.
4. Suspicious entries (extra spaces, inconsistent case).
5. References without corresponding files.

## Token-Efficient Strategy
- Work with pattern search instead of opening full files when possible.
- Read line ranges only when context validation is needed.

## Output
- Overall status per index
- List of detected issues
- Suggested corrective actions
