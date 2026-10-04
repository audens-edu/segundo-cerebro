"""Bloqueia dados pessoais e segredos nos arquivos do repositório."""
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[2]
EXTENSOES = {".md", ".txt", ".csv", ".json", ".yml", ".yaml"}
IGNORAR_PASTAS = {".git", ".github"}
MARCA_IGNORAR = "verificacao:ignorar"
EMAILS_PERMITIDOS = ("@example.com", "@exemplo.com", "users.noreply.github.com")

PADROES = [
    ("CPF", re.compile(r"(?<!\d)\d{3}\.\d{3}\.\d{3}-\d{2}(?!\d)")),
    ("Telefone", re.compile(r"(?<!\d)(?:\+?55[\s.-]?)?\(?\d{2}\)?[\s.-]?9\d{4}[\s.-]?\d{4}(?!\d)")),
    ("E-mail", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")),
    ("Token GitHub", re.compile(r"gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{40,}")),
    ("Chave de API", re.compile(r"sk-ant-[A-Za-z0-9_-]{20,}|sk-[A-Za-z0-9_-]{32,}|AKIA[0-9A-Z]{16}")),
    ("JWT", re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}")),
    ("Chave privada", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
]
CPF_SEM_PONTOS = re.compile(r"(?<!\d)\d{11}(?!\d)")


def cpf_valido(numero: str) -> bool:
    if len(set(numero)) == 1:
        return False
    for tamanho in (9, 10):
        soma = sum(int(d) * (tamanho + 1 - i) for i, d in enumerate(numero[:tamanho]))
        digito = (soma * 10) % 11 % 10
        if digito != int(numero[tamanho]):
            return False
    return True


def verificar(caminho: pathlib.Path) -> list[str]:
    achados = []
    rel = caminho.relative_to(RAIZ)
    for n, linha in enumerate(caminho.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
        if MARCA_IGNORAR in linha:
            continue
        for nome, padrao in PADROES:
            for m in padrao.finditer(linha):
                if nome == "E-mail" and m.group().lower().endswith(EMAILS_PERMITIDOS):
                    continue
                achados.append(f"::error file={rel},line={n}::{nome} encontrado: remova ou troque pelo papel da pessoa")
        for m in CPF_SEM_PONTOS.finditer(linha):
            if cpf_valido(m.group()):
                achados.append(f"::error file={rel},line={n}::CPF encontrado: remova")
    return achados


def main() -> int:
    achados = []
    for caminho in sorted(RAIZ.rglob("*")):
        if not caminho.is_file() or caminho.suffix.lower() not in EXTENSOES:
            continue
        if IGNORAR_PASTAS & set(caminho.relative_to(RAIZ).parts):
            continue
        achados.extend(verificar(caminho))
    for a in achados:
        print(a)
    print(f"{len(achados)} problema(s) encontrado(s).")
    return 1 if achados else 0


if __name__ == "__main__":
    sys.exit(main())
