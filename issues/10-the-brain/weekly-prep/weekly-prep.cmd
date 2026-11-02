cd /d %~dp0
claude -p "Read prep-prompt.md and do exactly what it says." --allowedTools "Read" "Glob" "Grep" "Edit(review/**)" > review\last-run.txt 2>&1
