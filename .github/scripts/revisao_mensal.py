"""Lista os documentos com revisão vencida, agrupados por dono."""
import datetime
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[2]
PRAZOS = {"processo": 90, "contexto": 180, "glossario": 180}


def cabecalho(caminho: pathlib.Path) -> dict:
    linhas = caminho.read_text(encoding="utf-8").splitlines()
    if not linhas or linhas[0].strip() != "---":
        return {}
    dados = {}
    for linha in linhas[1:]:
        if linha.strip() == "---":
            break
        if ":" in linha:
            chave, valor = linha.split(":", 1)
            dados[chave.strip()] = valor.strip()
    return dados


def main() -> int:
    hoje = datetime.date.today()
    vencidos: dict[str, list[str]] = {}
    for caminho in sorted(RAIZ.rglob("*.md")):
        rel = caminho.relative_to(RAIZ)
        if rel.parts[0] in {".github", "ferramentas"} or caminho.name.startswith("_") or caminho.name in {"README.md", "AGENTS.md", "CLAUDE.md"}:
            continue
        dados = cabecalho(caminho)
        prazo = PRAZOS.get(dados.get("tipo", ""))
        if prazo is None:
            continue
        dono = dados.get("dono", "sem dono")
        try:
            revisado = datetime.date.fromisoformat(dados.get("revisado_em", ""))
        except ValueError:
            vencidos.setdefault(dono, []).append(f"- [ ] `{rel}`: sem data de revisão válida")
            continue
        dias = (hoje - revisado).days
        if dias > prazo:
            vencidos.setdefault(dono, []).append(f"- [ ] `{rel}`: {dias} dias sem revisão (prazo {prazo})")
    if not vencidos:
        return 0
    print("Documentos com revisão vencida. Para cada um, peça à IA para revisar: se nada mudou, basta atualizar `revisado_em`.\n")
    for dono in sorted(vencidos):
        print(f"## {dono}\n")
        print("\n".join(vencidos[dono]) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
