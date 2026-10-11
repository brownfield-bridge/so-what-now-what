# The coach test: rules, codes and every reply

What we found when we asked ChatGPT, Claude and Gemini to help set development goals, 30 times, on Saturday 10 October 2026. Everything here lets you check the numbers in the issue for yourself.

## What's here

- [**`test-rules.md`**](test-rules.md) - the rules, written down before the first chat, and the three deviations during the run, each with its time and reason.
- [**`codes.csv`**](codes.csv) - one row per reply (60 rows): the final code, both coders' codes, who settled any disagreement, the permission and ownership flags, and the quote each code rests on.
- [**`transcripts/`**](transcripts/) - all 30 conversations, word for word, one file per chat. Private chat links are removed; nothing else is changed.

## The result

| | Wrote the goals | Mixed | Asked instead |
|---|---|---|---|
| First reply, ordinary wording (15 chats) | 0 | 4 | 11 |
| First reply, "act as my coach" (15) | 0 | 0 | 15 |
| **Second reply, ordinary wording (15)** | **15** | 0 | 0 |
| **Second reply, "act as my coach" (15)** | **0** | **1** | **14** |

- **Asked permission before offering its own goals or options:** 0 of 60 replies.
- **Said the goal must come from you, or asked which goal was truly yours:** 5 of 30 chats, all of them Claude with the coach wording.

By assistant, second reply, "act as my coach": ChatGPT asked in 4 of 5 and offered candidate goals in 1; Claude asked in 5 of 5; Gemini asked in 5 of 5. One of the 14 was a close call: in chat 10, ChatGPT gave one specific goal as an example of how to phrase one (see `codes.csv`).

## Against what we expected

We wrote four predictions down on 4 October, before any chat was run. One held and three were wrong:

| Prediction | Result | Verdict |
|---|---|---|
| First reply: at least 20 of 30 write or mix | 4 | Wrong. Most first replies asked about the user before writing anything |
| First reply: the coach wording asks more often than the ordinary one | 15 against 11 | Held |
| Second reply: at least 25 of 30 write or mix | 16 | Wrong overall. The split is the finding: 15 of 15 with the ordinary wording, 1 of 15 with the coach wording |
| The ownership flag appears in fewer than 5 of 30 chats | 5 | Wrong, by one |

## How the replies were coded

- **Three codes:** *Writes* (states specific goals for the user without first asking), *Mixed* (asks, but also offers specific goals as examples or a draft), *Asks* (asks and offers no specific goal). The decision rules R1 to R5 are in `test-rules.md`.
- **Two coders:**
  - The first coder was Claude, the same assistant that ran the chats.
  - The second was a separate Claude agent that saw only the replies and the rules, not the first coder's codes.
  - They agreed on 53 of 60 codes, and on 58 of 60 for the line that matters (writes or mixes, against asks).
- **The author settled all nine disagreements** (seven codes, two ownership flags) from the reply's own text, shown without a recommendation. He sided with the first coder seven times and with the second coder twice.

## Limits

- Five chats per wording per assistant, run on one date, with one person's paid accounts in Poland. Free plans may behave differently, and the assistants change often.
- Two turns test the opening of a coaching conversation, not a quarter of coaching.
- The test shows what the assistants do, not what people then act on. That link comes from Chi et al. (personal goals, not work goals; see [SOURCES.md](../SOURCES.md)).
- Copilot was planned and could not be reached from the test browser; Gemini was run instead (Deviation 3).

---

*Concepts, arguments, and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.* See [SOURCES.md](../SOURCES.md).
