# OpenWyd Client Data

> Assets e dados do cliente oficial da plataforma **OpenWyd®** — o ecossistema open-source que centraliza servidores e jogadores de WYD.

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
[![Discord](https://img.shields.io/badge/Discord-OpenWyd-5865F2?logo=discord&logoColor=white)](https://discord.gg/ZTQykgke)

Este repositório contém todos os recursos carregados pelo cliente WYD em runtime: bases de dados binárias do jogo (itens, skills, mapas, montarias), modelos 3D, texturas de interface, efeitos visuais, sons e músicas.

---

## Arquitetura

O cliente é composto por `WYD.exe` e um conjunto de diretórios de assets carregados em runtime. Os caminhos são resolvidos relativos ao executável — **a estrutura de diretórios não deve ser alterada**.

### Relação cliente ↔ servidor

O OpenWyd adota um modelo onde os mesmos dados de jogo existem em dois formatos paralelos — binário no cliente e XML no servidor. Alterações em dados compartilhados exigem atualização nos dois repositórios.

| Dado | Formato no cliente | Formato no servidor |
|------|--------------------|---------------------|
| Itens | `Itemlist.bin` | `Data/itemlist.xml` |
| Skills/efeitos | `SkillData.bin` | `Data/spells.xml` |
| Terreno | `HeightMap.dat`, `AttributeMap.dat` | `Data/HeightMap.dat`, `Data/AttributeMap.dat` |

> `serverlist.bin` é atualizado pela equipe OpenWyd ao adicionar ou modificar servidores disponíveis na tela de login.

### Dados do jogo

Arquivos `.bin` e `.dat` são bases de dados proprietárias serializadas:

| Arquivo | Conteúdo |
|---------|----------|
| `Itemlist.bin` / `Itemname.bin` | Definições e nomes dos itens |
| `SkillData.bin` | Skills e atributos |
| `Mixlist.bin` | Receitas de crafting |
| `MountData.bin` | Montarias e pets |
| `object.bin` | Objetos do mundo |
| `HeightMap.dat` / `AttributeMap.dat` | Dados de terreno *(sincronizar com o servidor)* |
| `Env/Field*.dat` + `Env/Field*.trn` | Mapas de campo |
| `serverlist.bin` | Lista de servidores disponíveis |

### Assets (somente cliente)

| Diretório | Conteúdo | Formato |
|-----------|----------|---------|
| `Mesh/` | Modelos 3D e esqueletos | `.msa`, `.msh` |
| `UI/` | Texturas de interface e textos do jogo | `.wyt`, `.txt` |
| `Effect/` | Efeitos visuais | `.wys`, `.msa` |
| `Sound/` | Efeitos sonoros | `.wav` |
| `music/` | Músicas de fundo | `.mp3`, `.wav` |
| `Env/` | Texturas de ambiente | `.wyt` |
| `NUI/` | Nova interface | `.wyt` |
| `shader/` | Shaders GPU | `.bin` |

Alguns diretórios possuem arquivos de índice que o executável usa para resolver referências em runtime: `Mesh/MeshList.txt` e `Sound/soundlist.txt`.

---

## Como Contribuir

O OpenWyd segue o modelo open-source do Google/Linux: o core é mantido pela equipe, e a comunidade contribui através de assets, textos e scripts.

### Tipos de contribuição aceitos

- **Assets visuais** — novos modelos, texturas, efeitos, sons
- **Textos e localização** — arquivos `.txt` em `UI/` (descrições de skills, comandos, quests)
- **Dados de jogo** — atualizações em arquivos `.bin`/`.dat` via ferramentas da equipe
- **Scripts de servidor** — contribuições via [`open-wyd-scripts`](https://github.com/open-wyd/open-wyd-scripts)

### Formatos proprietários

Os arquivos `.bin`, `.dat`, `.wyt`, `.wys`, `.msa` e `.msh` são formatos proprietários do WYD. **Não edite esses arquivos diretamente em texto** — use as ferramentas disponibilizadas pela equipe OpenWyd.

### Fluxo

1. Faça um fork do repositório
2. Crie uma branch descritiva (`feat/novo-efeito-boss`, `fix/textura-armadura`)
3. Abra um Pull Request descrevendo o que foi alterado e por quê
4. Participe da discussão no [Discord](https://discord.gg/ZTQykgke)

---

## Ecossistema

Este repositório faz parte da plataforma OpenWyd®:

| Repositório | Descrição |
|-------------|-----------|
| [`open-wyd-scripts`](https://github.com/open-wyd/open-wyd-scripts) | Scripts server-side em Lua 5.3 |
| `ows-clientdata` (este) | Assets e dados do cliente |

## Comunidade

Dúvidas, sugestões e discussões acontecem no Discord oficial:
👉 [discord.gg/ZTQykgke](https://discord.gg/ZTQykgke)
