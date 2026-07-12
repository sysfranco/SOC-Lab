#!/usr/bin/env python3
"""
Generate SOC-Lab graphs from a real Wazuh CSV export.

This script intentionally does NOT generate simulated data.
If the input CSV does not exist or lacks usable columns, it exits with an error.

Usage:
    python analysis/generate_graphs.py data/wazuh_alerts_export.csv reports/figures
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


def find_column(df: pd.DataFrame, candidates: list[str]) -> str | None:
    normalized = {col.lower().strip(): col for col in df.columns}
    for candidate in candidates:
        key = candidate.lower().strip()
        if key in normalized:
            return normalized[key]
    return None


def save_bar(series: pd.Series, title: str, xlabel: str, ylabel: str, output: Path) -> None:
    if series.empty:
        raise ValueError(f"No data available for {title}")

    ax = series.plot(kind="bar")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output)
    plt.close()


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python analysis/generate_graphs.py <wazuh_csv> <output_dir>", file=sys.stderr)
        return 2

    csv_path = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])

    if not csv_path.exists():
        print(f"ERROR: CSV not found: {csv_path}", file=sys.stderr)
        print("Export real alerts from Wazuh first. Do not use simulated data.", file=sys.stderr)
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(csv_path)

    if df.empty:
        print("ERROR: CSV is empty. Export real Wazuh alerts first.", file=sys.stderr)
        return 1

    generated = []

    level_col = find_column(df, ["rule.level", "rule_level", "level", "severity"])
    if level_col:
        counts = df[level_col].value_counts().sort_index()
        output = output_dir / "alerts_by_rule_level.png"
        save_bar(counts, "Alerts by rule level", "Rule level", "Alert count", output)
        generated.append(output)

    agent_col = find_column(df, ["agent.name", "agent_name", "agent", "host", "hostname"])
    if agent_col:
        counts = df[agent_col].value_counts().head(15)
        output = output_dir / "alerts_by_agent.png"
        save_bar(counts, "Alerts by agent", "Agent", "Alert count", output)
        generated.append(output)

    mitre_col = find_column(
        df,
        [
            "rule.mitre.technique",
            "rule_mitre_technique",
            "mitre.technique",
            "mitre_technique",
            "technique",
        ],
    )
    if mitre_col:
        counts = df[mitre_col].dropna().astype(str).value_counts().head(15)
        output = output_dir / "alerts_by_mitre_technique.png"
        save_bar(counts, "Alerts by MITRE technique", "Technique", "Alert count", output)
        generated.append(output)

    if not generated:
        print("ERROR: No supported columns found.", file=sys.stderr)
        print("Expected one of: rule.level, agent.name, rule.mitre.technique", file=sys.stderr)
        print("Available columns:", ", ".join(df.columns), file=sys.stderr)
        return 1

    print("Generated figures:")
    for path in generated:
        print(f"- {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
