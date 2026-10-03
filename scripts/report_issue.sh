#!/usr/bin/env bash
# Open, update or close the issue that carries a health report.
# Usage: report_issue.sh <title> <findings> <report file>
set -euo pipefail

title=$1
findings=$2
report=$3

number=$(gh issue list --state open --limit 200 --json number,title \
  --jq "map(select(.title == \"$title\")) | .[0].number // empty")

if [ "$findings" != "0" ]; then
  if [ -n "$number" ]; then
    gh issue edit "$number" --body-file "$report"
    echo "updated issue #$number"
  else
    gh issue create --title "$title" --body-file "$report"
  fi
elif [ -n "$number" ]; then
  gh issue close "$number" --comment "All entries pass the health check."
  echo "closed issue #$number"
else
  echo "nothing to report"
fi
