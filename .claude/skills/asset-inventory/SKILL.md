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
Read the file `Mesh/MeshList.txt`, extract all file references, and for each one check if the file exists under `Mesh/`. Report any entries that have no matching file on disk.

## 4. Verificar referências quebradas em Sound/soundlist.txt
Read the file `Sound/soundlist.txt`, extract all file references, and for each one check if the file exists under `Sound/`. Report any entries that have no matching file on disk.

## Output esperado
Apresente um resumo com:
- Tabela de tamanho e contagem por diretório
- Lista de referências quebradas no MeshList.txt (ou "nenhuma encontrada")
- Lista de referências quebradas no soundlist.txt (ou "nenhuma encontrada")
