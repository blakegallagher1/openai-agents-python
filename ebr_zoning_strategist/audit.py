from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterable

import pandas as pd
import yaml


class AuditLog:
    """Utility for analyzing and fixing audit logs."""

    def __init__(self, records: pd.DataFrame) -> None:
        self.records = records

    @classmethod
    def load(cls, path: Path) -> "AuditLog":
        df = pd.read_csv(path)
        if not {"source", "page", "reason"}.issubset(df.columns):
            missing = {"source", "page", "reason"} - set(df.columns)
            raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
        return cls(df)

    def summary(self) -> pd.DataFrame:
        """Return counts of failures grouped by reason."""
        return (
            self.records
            .groupby("reason")
            .size()
            .reset_index(name="count")
            .sort_values("count", ascending=False)
        )

    def apply_rules(self, rules: Dict[str, str]) -> None:
        """Append a 'fix' column using provided reason→fix rules."""
        self.records["fix"] = self.records["reason"].map(rules).fillna("")

    def to_csv(self, path: Path) -> None:
        self.records.to_csv(path, index=False)


def load_rules(path: Path) -> Dict[str, str]:
    with open(path, "r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, dict):
        raise ValueError("Rules file must define a mapping from reason to fix")
    return {str(k): str(v) for k, v in data.items()}


def generate_fix_report(log_path: Path, rules_path: Path, output: Path) -> None:
    log = AuditLog.load(log_path)
    rules = load_rules(rules_path)
    log.apply_rules(rules)
    log.to_csv(output)
    summary = log.summary()
    summary.to_csv(output.with_name(output.stem + "_summary.csv"), index=False)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Process audit log and apply fix rules")
    parser.add_argument("log", type=Path, help="Path to audit_log.csv")
    parser.add_argument("rules", type=Path, help="YAML file mapping reasons to fixes")
    parser.add_argument("output", type=Path, help="Destination for updated CSV")
    args = parser.parse_args()
    generate_fix_report(args.log, args.rules, args.output)
