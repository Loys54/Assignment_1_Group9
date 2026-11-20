# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: <e.g. Lab 4>
- Student name: <Aloysius Probo Suryo Siswanto>
- Matric no: <X26EC0012>
- Group ID: <group work only, else n/a>
- AI level: <0, 1 or 2 - see the assessment brief>
- Tools cited: <UTM format, e.g. OpenAI (2026). ChatGPT (GPT-5). Retrieved 12 October 2026 from https://chat.openai.com>

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [X] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 19 November 2026, 01:43 and 12:28
- Tool: Anthropic (2026). Claude (Opus 5.5). Retrieved 19 November 2026 from https://claude.ai
- Purpose: explain
- Prompt: "Bantu aku menyelesaikan ini nanti pagi" (uploaded the Lab 6 brief and starter); "sekarang kita lakukan lab 6"
- Output: Summarised the tasks, a work order by marks, setup commands, and how a FASTA file is structured.
- Verified by: Read the brief and data files myself
- My change: Used it to plan the order of work
- Used in: Planning only

## Entry 2

- Date: 19 November 2026, 12:42-13:31
- Tool: Anthropic (2026). Claude (Opus 5.5). Retrieved 19 November 2026 from https://claude.ai
- Purpose: hint
- Prompt: "bisakah kita mengerjakan yang pendek dulu"; "ayo kita kerjakan yang lain, yang mudah dan cepat"; pasted my drafts of _finish, mean_phred, read_csv_records and write_csv
- Output: Word-pseudocode for _finish, mean_phred, read_csv_records, write_csv and read_fasta; pointed out errors in my drafts (join on a list, is None vs empty string, brackets around sum, len of an int, a typo in open).
- Verified by: python -m pytest and manual checks with python -c
- My change: Wrote and fixed the functions myself
- Used in: src/bio_io.py _finish, read_csv_records, write_csv; src/batch.py mean_phred

## Entry 3

- Date: 19 November 2026, 13:42
- Tool: Anthropic (2026). Claude (Opus 5.5). Retrieved 19 November 2026 from https://claude.ai
- Purpose: generate-text
- Prompt: "akan aku kumpulkan apa adanya dulu, buatkan readme dan ai log nya"
- Output: README.md text from the starter template and this AI use log.
- Verified by: Read both files
- My change: Filled in my name and matric number
- Used in: README.md, AI_USE_LOG.md

<!-- Copy the whole 'Entry' block for each extra interaction: ## Entry 2, ## Entry 3 ... -->
