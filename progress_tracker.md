# Progress Tracker

## Audit Log QA Process

1. Run `audit.py` to summarize failures:
   ```bash
   python -m ebr_zoning_strategist.audit audit_log.csv rules.yaml fixed_audit.csv
   ```
2. Review `fixed_audit_summary.csv` for most frequent errors.
3. Update `rules.yaml` to map common `reason` strings to manual fixes.
4. Re-run the command to produce a patched audit log with a `fix` column.
5. Import the fixed entries back into the parser or dataset as needed.
