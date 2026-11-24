#!/usr/bin/env bash
# Install the OFFICIAL pinned AI-DLC v1.0.1 rule files from AWS into the project.
# Usage (in repo root): bash scripts/install-aidlc-v1.0.1.sh codex
# For other agents, consult the v1.0.1 official README; don't reuse v2 commands.
set -euo pipefail
AGENT="${1:-codex}"
if [[ "$AGENT" != "codex" ]]; then
  echo "This bootstrap supports 'codex' only. Use the v1.0.1 official README for $AGENT." >&2
  exit 2
fi
if ! command -v curl >/dev/null || ! command -v unzip >/dev/null; then
  echo "Install curl and unzip first." >&2
  exit 2
fi
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMP="$(mktemp -d)"
trap 'rm -rf "$TEMP"' EXIT
URL="https://github.com/awslabs/aidlc-workflows/releases/download/v1.0.1/ai-dlc-rules-v1.0.1.zip"
echo "Downloading pinned AWS AI-DLC v1.0.1 release..."
curl --fail --location --retry 2 --output "$TEMP/rules.zip" "$URL"
unzip -q "$TEMP/rules.zip" -d "$TEMP/unpacked"
BASE="$(find "$TEMP/unpacked" -type f -path '*/aws-aidlc-rules/core-workflow.md' -print -quit)"
if [[ -z "$BASE" ]]; then echo "No core workflow found: verify archive layout" >&2; exit 1; fi
RULE_DIR="$(dirname "$BASE")"
DETAIL_DIR="$(dirname "$RULE_DIR")/aws-aidlc-rule-details"
if [[ ! -d "$DETAIL_DIR" ]]; then echo "No rule-details folder found" >&2; exit 1; fi
if [[ -e "$ROOT/AGENTS.md" ]]; then
  echo "AGENTS.md exists; backup before replacing it." >&2
  exit 2
fi
cp "$BASE" "$ROOT/AGENTS.md"
mkdir -p "$ROOT/.aidlc-rule-details"
cp -R "$DETAIL_DIR"/. "$ROOT/.aidlc-rule-details/"
if [[ ! -f "$ROOT/.aidlc-rule-details/common/process-overview.md" ]]; then
  echo "Expected common rules not found; inspect release archive." >&2
  exit 1
fi
printf 'Installed AWS AI-DLC v1.0.1 for Codex in %s\n' "$ROOT"
printf 'Next: review files, git add AGENTS.md .aidlc-rule-details, commit, then launch Codex.\n'
