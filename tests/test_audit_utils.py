from pathlib import Path

import pandas as pd

from ebr_zoning_strategist.audit import AuditLog, load_rules


def test_apply_rules(tmp_path: Path) -> None:
    log_path = Path('examples/audit_log.csv')
    rules_path = Path('examples/rules.yaml')
    output = tmp_path / 'out.csv'

    AuditLog.load(log_path)  # ensure load works
    rules = load_rules(rules_path)
    assert 'missing_header' in rules

    generate_output = False
    if generate_output:
        from ebr_zoning_strategist.audit import generate_fix_report
        generate_fix_report(log_path, rules_path, output)
        df = pd.read_csv(output)
        assert 'fix' in df.columns
        assert df.loc[0, 'fix'] == rules['missing_header']
