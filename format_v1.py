#!/usr/bin/env python3
"""Formata B_relatorio_assistente_v1.md colado como bloco único."""
import re
from pathlib import Path

SRC = Path(__file__).parent / "B_relatorio_assistente_v1.md"
OUT = SRC

def format_text(text: str) -> str:
    text = text.strip()
    if not text:
        raise SystemExit("Arquivo vazio. Cole o conteúdo e salve antes de rodar.")

    text = re.sub(
        r"Brasil(\d)\.\s*",
        r"# Relatório de Pesquisa Documental: Ecossistema de Atores, Sistemas e Jornada do Passaporte Comum no Brasil\n\n## \1. ",
        text,
        count=1,
    )
    text = re.sub(
        r"(\d)\.\s*(Mapeamento de Atores|Matriz de Mendelow|Pontos de Fricção|Lacunas de Evidência|Tabela-Resumo)",
        r"\n\n## \1. \2",
        text,
    )
    text = re.sub(r"Etapa (\d+):", r"\n\n### Etapa \1:", text)
    text = re.sub(r"Camada de ", r"\n\n### Camada de ", text)
    text = re.sub(
        r"(Canais e Sistemas de TI Envolvidos:)",
        r"\n\n**\1**",
        text,
    )
    text = re.sub(
        r"(Contingência de Falha do Sistema Web:)",
        r"\n\n**\1**",
        text,
    )
    text = re.sub(r"(Fricção Estrutural)(As barreiras)", r"\n\n### \1\n\n\2", text)
    text = re.sub(r"(Fricção de Design)(As barreiras)", r"\n\n### \1\n\n\2", text)
    text = re.sub(
        r"(Análise de Demanda Falha \(Failure Demand\))(A demanda falha)",
        r"\n\n### \1\n\n\2",
        text,
    )
    text = re.sub(
        r"(Análise Sistêmica dos Drivers Operacionais)(Como inferência)",
        r"\n\n### \1\n\n\2",
        text,
    )
    text = re.sub(
        r"(Avaliação do Índice de Satisfação)(A Polícia)",
        r"\n\n### \1\n\n\2",
        text,
    )
    text = re.sub(
        r"Tabela (\d+):",
        r"\n\n### Tabela \1:",
        text,
    )
    # Quebras antes de rótulos de camada/atores em lista
    labels = [
        "Cidadão Comum", "Cidadão em Renovação", "Menores de Idade",
        "Pessoas com Deficiência", "Analfabetos Digitais",
        "Atendentes Terceirizados", "Policiais Federais", "Chefias dos Postos",
        "Divisão de Passaportes", "Direção-Geral", "Ministério da Justiça",
        "Ministério da Gestão", "Controladoria-Geral", "Tribunal de Contas",
        "Ouvidoria da Polícia", "SERPRO:", "Dataprev:", "Casa da Moeda",
        "Fornecedores de Tecnologia", "Despachantes e Assessorias",
        "Agências de Turismo", "Conselhos de Usuários", "Poder Judiciário:",
        "Obrigatoriedade da Biometria", "A Rigidez de Verificação",
        "Ritos Protetivos", "Cancelamento Automático",
        "Exclusão Digital", "Assimetria Informativa", "Janela de Agendamento",
        "Lentidão no Registro", "Impossibilidade de Retificação",
        "Geração de Passaportes Triturados",
    ]
    for label in labels:
        text = re.sub(rf"({re.escape(label)})", r"\n\n- **\1**", text, count=1)

    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text + "\n"

if __name__ == "__main__":
    raw = SRC.read_text(encoding="utf-8")
    formatted = format_text(raw)
    OUT.write_text(formatted, encoding="utf-8")
    words = len(re.findall(r"\S+", formatted))
    print(f"Formatado: {OUT} ({words} palavras, {len(formatted)} chars)")
