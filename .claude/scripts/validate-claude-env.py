#!/usr/bin/env python3
"""Validates that the environment has the dependencies needed for Claude automation."""

import platform
import shutil
import sys


def has_cmd(name: str) -> bool:
    return shutil.which(name) is not None


def has_python3() -> bool:
    # Already running under Python 3 if we got here, but verify alternatives for PATH.
    return has_cmd("python3") or has_cmd("py")


def has_bash() -> bool:
    if has_cmd("bash"):
        return True
    if platform.system().lower() != "windows":
        return False
    from pathlib import Path
    candidates = [
        Path(r"C:\Program Files\Git\bin\bash.exe"),
        Path(r"C:\Program Files (x86)\Git\bin\bash.exe"),
    ]
    return any(p.exists() for p in candidates)


SYSTEM = platform.system().lower()

checks = [
    ("python3", True, has_python3(), "Hooks e validação de ambiente"),
    ("bash", False, has_bash(), "Shell do Claude Code (recomendado no Windows via Git Bash)"),
]

print("Dependência   Obrigatório   Instalado   Propósito")
print("-" * 65)
for name, required, installed, purpose in checks:
    req = "sim" if required else "não"
    ins = "sim" if installed else "não"
    print(f"{name:<13} {req:<13} {ins:<11} {purpose}")

missing_required = [(n, p) for n, r, i, p in checks if r and not i]
missing_optional = [(n, p) for n, r, i, p in checks if not r and not i]

if missing_required:
    print("\nERRO: dependências obrigatórias ausentes:")
    for name, _ in missing_required:
        print(f"  - {name}")
    print("\nInstale Python 3:")
    if SYSTEM == "windows":
        print("  winget install --id Python.Python.3.13 --exact --source winget")
        print("  Ou baixe em: https://www.python.org/downloads/")
    elif SYSTEM == "darwin":
        print("  brew install python")
    else:
        print("  Instale python3 pelo gerenciador de pacotes da sua distribuição")
    sys.exit(1)

if missing_optional:
    print("\nAVISO: dependências opcionais ausentes:")
    for name, _ in missing_optional:
        print(f"  - {name}")
    if SYSTEM == "windows":
        print("\n  Para bash: winget install --id Git.Git --source winget")

print("\nOK: ambiente compatível com as automações Claude deste repositório.")
sys.exit(0)
