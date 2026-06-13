#!/usr/bin/env bash
# Headless weekly synthesizer. Schedule with cron, e.g.:
#   0 17 * * 0  /path/to/claude-code-recipe/run-weekly.sh >> briefs/cron.log 2>&1
cd "$(dirname "$0")"
claude -p "/synthesize" --allowedTools "WebSearch,Read,Write" --model claude-sonnet-4-6
