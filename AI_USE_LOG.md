# AI USE LOG

Shared AI-use log for SECB3203 Assignment 1.

- Course: SECB3203
- Assessment: Assignment 1
- Student name: GUO KEXIN
- Matric no: X26EC0009
- Group ID: G09
- AI level: Level 1, AI as tutor
- Tools cited: OpenAI (2026). Codex (GPT-5). Retrieved 21 November 2026 from https://chatgpt.com/codex

## Declaration

- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and
  complete.

## Entry 1: GitHub Desktop setup and basic Git workflow

- Date: 20-21 November 2026, Asia/Kuala_Lumpur
- Tool: OpenAI Codex (GPT-5), accessed 21 November 2026,
  https://chatgpt.com/codex
- Purpose: explain and debug GitHub Desktop
- Prompt: "帮我下载github"; "这个是用来干嘛的"; "下一步该怎么做"; "这个软件怎么用";
  "为什么我在浏览器里打开不是这个样子"
- Output: Explained the difference between GitHub, Git, GitHub Desktop and Visual Studio Code.
  Described the workflow Fetch/Pull, edit in VS Code, inspect Changes, Commit and Push.
- Verified by: Following the instructions in GitHub Desktop and checking that the remote repository
  was cloned successfully.
- My change: Accepted the recommended GitHub Desktop workflow and used it to clone the group
  repository.
- Used in: Git collaboration setup; no submitted source code.

## Entry 2: Assignment task interpretation and task selection

- Date: 21 November 2026, Asia/Kuala_Lumpur
- Tool: OpenAI Codex (GPT-5), accessed 21 November 2026,
  https://chatgpt.com/codex
- Purpose: explain
- Prompt: "他说的T1T2是啥意思"; "给我挑两个简单的"; "你能给我讲解一下作业具体是什么还有这个软件怎么用吗"
- Output: AI explained the seven assignment work packages, summarised the six ordered triage rules,
  and suggested T3 and T5 as the two smallest self-contained coding tasks.
- Verified by: Comparing the explanation with SECB3203_assignment1_student.docx and data/params.json.
- My change: Selected T3 and T5 and used those task boundaries to decide which functions to implement.
- Used in: Group task allocation; decision_counts, impact_counts, gene_summary, results_to_csv and
  build_report.

## Entry 3: Reference implementation of T3 and T5

- Date: 21 November 2026, Asia/Kuala_Lumpur
- Tool: OpenAI Codex (GPT-5), accessed 21 November 2026,
  https://chatgpt.com/codex
- Purpose: generate-code
- Prompt: "协助我写这些代码";
- Output: AI provided a reference implementation for the five T3/T5 functions and explained how the
  functions count decisions and impacts, summarise genes, produce CSV text and build the report.
- Verified by: Read the function specification, ran targeted checks for empty input, normalised
  gene/impact text, mean depth, CSV newlines and report formatting, and ran ruff.
- My change: Accepted the reference implementation after checking it and saved it in
  src/a1_triage.py.
- Used in: a1_triage.py: decision_counts, impact_counts, gene_summary, results_to_csv and
  build_report.

## Entry 4: Code review and correction

- Date: 21 November 2026, Asia/Kuala_Lumpur
- Tool: OpenAI Codex (GPT-5), accessed 21 November 2026,
  https://chatgpt.com/codex
- Purpose: review and debug
- Prompt: "帮我检查一下我在VS code 里面我负责的部分的代码写的有没有什么问题"
- Output: AI found incorrect docstring indentation and a missing StringIO import, corrected those
  issues, and confirmed that the full test suite was still blocked by unimplemented T2/T4 functions.
- Verified by: Python syntax parsing, ruff, targeted T3/T5 assertions and inspection of the Git diff.
- My change: Accepted the corrections and committed the corrected file.
- Used in: a1_triage.py imports and the five T3/T5 functions.

## Entry 5: Git submission verification

- Date: 21 November 2026, Asia/Kuala_Lumpur
- Tool: OpenAI Codex (GPT-5), accessed 21 November 2026,
  https://chatgpt.com/codex
- Purpose: explain
- Prompt: "我现在怎么把我的代码传到github上"; "你帮我看看我提交成功了吗"
- Output: AI explained the difference between Commit and Push and verified that commit 68e99f2 was
  present on the remote main branch.
- Verified by: Comparing the local HEAD, origin/main and the GitHub remote branch identifier.
- My change: Committed and pushed the T3/T5 implementation with the commit message
  "Implement variant summary and report functions".
- Used in: Git history; no additional source-code change.
## Entry 6: Task division and GitHub Desktop setup

- Date: 20 November 2026, Asia/Singapore
- Tool: Anthropic (2026). Claude (Opus 5.5). Retrieved 20 November 2026 from https://claude.ai
- Purpose: explain
- Prompt: "Ini adala assignment group prog bio ku, bantu aku agar mudah melakukan pembagian tugas ,dan apakah bisa ,menggunakan github dekstop untuk setup tugas agar mudah dilakukan"
- Output: Suggested a split of T1 to T7 between members and gave step-by-step GitHub Desktop instructions (create, publish, invite collaborators, clone, pull before work, commit and push).
- Verified by: Following the steps in GitHub Desktop and checking the repository on github.com.
- My change: Used the split as a starting point; the final roles were agreed in the group.
- Used in: Group organisation and Git setup; no submitted code.

## Entry 7: Repository structure check

- Date: 21 November 2026, Asia/Singapore
- Tool: Anthropic (2026). Claude (Opus 5.5). Retrieved 21 November 2026 from https://claude.ai
- Purpose: review
- Prompt: "coba cek file ku aku baru melakukan pull"
- Output: Pointed out that my first commit contained Lab 6 files and that the assignment sat in a subfolder; explained how to move the files to the repository root.
- Verified by: Running python -m pytest (5 passed, 1 failed on rank_variants) and ruff check src after the move.
- My change: Removed the Lab 6 files and moved the assignment files to the root myself.
- Used in: Commit "Repo restructure"; no code change.

## Entry 8: Review of our own tests

- Date: 22-23 November 2026, Asia/Singapore
- Tool: Anthropic (2026). Claude (Opus 5.5). Retrieved 22 November 2026 from https://claude.ai
- Purpose: review
- Prompt: "coba cek kode ku di file tst"
- Output: Reviewed tests I wrote; said the file must be named test_a1_triage.py, pointed out a duplicate import, typos in test names and trailing whitespace; confirmed my expected values.
- Verified by: Running python -m pytest and ruff check.
- My change: Renamed the file and fixed the issues myself.
- Used in: tests/test_a1_triage.py.

## Entry 9: Request to write the AI log and README

- Date: 23 November 2026, Asia/Singapore
- Tool: Anthropic (2026). Claude (Opus 5.5). Retrieved 23 November 2026 from https://claude.ai
- Purpose: other
- Prompt: "buatkan aku ai log nya , dan readme please"
- Output: Drafted entries 6 to 9 of this log from our chat history. Declined to write the README text (Level 1) and gave a checklist of facts and commands instead.
- Verified by: Checking each entry against the chat history.
- My change: Checked and edited the log entries; wrote the README myself.
- Used in: AI_USE_LOG.md entries 6 to 9; README.md structure only.
## Group signatures

Each group member must add their own signature after reviewing the complete log.

- Signed: GUO KEXIN, X26EC0009, 2026-11-21
- Signed: Aloysius PRobo, X26EC0012, 2026-11-23