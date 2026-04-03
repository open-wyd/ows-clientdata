---
name: asset-inventory
description: Summarize asset sizes per directory and check index files (MeshList.txt, soundlist.txt) for broken references
disable-model-invocation: true
---

Run each step and report the findings clearly in Portuguese.

## 1. Tamanho por diretório
```bash
du -sh Mesh/ UI/ Effect/ Sound/ music/ Env/ NUI/ shader/
```

## 2. Contagem de arquivos por diretório
```bash
for dir in Mesh UI Effect Sound music Env NUI shader; do
  count=$(find "$dir" -type f | wc -l)
  echo "$dir: $count arquivos"
done
```

## 3. Verificar referências quebradas em Mesh/MeshList.txt
Read the file `Mesh/MeshList.txt`, extract all file references, normalize each path before checking it on disk, and only then report broken references. The normalization must:
- convert Windows separators `\\` to `/`
- treat prefixes case-insensitively
- remove a leading `mesh/` prefix when present and resolve the file under `Mesh/`
- map a leading `effect/` prefix to the `Effect/` directory and resolve the remaining relative path there

After normalization, check whether each referenced file exists in the correct base directory (`Mesh/` for `mesh/...`, `Effect/` for `effect/...`). Report only entries that still have no matching file on disk after this normalization.

## 4. Verificar referências quebradas em Sound/soundlist.txt
Read the file `Sound/soundlist.txt`, extract all file references, normalize each path before checking it on disk, and only then report broken references. The normalization must:
- convert Windows separators `\\` to `/`
- treat prefixes case-insensitively
- remove a leading `sound/` prefix when present and resolve the file under `Sound/`

After normalization, check whether each referenced file exists in the correct base directory (`Sound/`). Report only entries that still have no matching file on disk after this normalization.

## Output esperado
Apresente um resumo com:
- Tabela de tamanho e contagem por diretório
- Lista de referências quebradas no MeshList.txt após normalização de caminho e resolução correta de `Mesh/` ou `Effect/` (ou "nenhuma encontrada")
- Lista de referências quebradas no soundlist.txt após normalização de caminho e resolução correta de `Sound/` (ou "nenhuma encontrada")
