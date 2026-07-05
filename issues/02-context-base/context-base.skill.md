---
name: context-base
description: >
  Stand up a private context base: a folder of plain files an AI can reason over for one area of the
  user's work. Use when the user wants to build a personal or team knowledge base without a vector
  database or platform; triggers on "set up a context base", "build my second brain", "organise my
  files for AI", "stop re-explaining context to my AI", "make a knowledge base from my folders".
  Produces a folder structure, a root map (CONTEXT.md), and a retrieval prompt. CC-BY 4.0 - So What,
  Now What, Issue 02.
---

# Context Base - setup

> **How to run this (for the reader).** This runs inside your own AI, so the base stays in the account and storage you already use. In Claude or Cowork, add this file as a skill and say "set up a context base." In any other chat model, paste the prompt at the bottom. It goes faster if you talk instead of type, and it works as a group exercise with one person at the keyboard.

You are helping the user stand up a context base for **one area** of their work: a structure of plain files and folders their AI can reason over. The output is three things: a folder list, a one-page root map (`CONTEXT.md`), and a retrieval prompt they reuse. You do the structuring; they supply the few things only they can give.

## Operating rules

1. **Keep it tight. Propose, don't interrogate.** Ask only for the few things that are theirs to give, then do the structuring yourself and have them correct it. Aim for three or four short turns, not twenty.
2. **One area only.** If the user names several areas, pick the one they lead with and offer to repeat the process for the others later. One base, one area; a base that holds everything reasons well over nothing.
3. **Mirror how they work, not a generic taxonomy.** Folders should match the questions they actually ask. If a folder you propose would rarely be opened, drop it.
4. **Plain files only.** No vector database, no embeddings, no new platform. The whole point is that this is just folders.
5. **Reader agency.** You build the structure; they own it. Flag anything you are unsure about and let them decide.

## The interview (aim for three or four short turns)

**Turn 1 - the area.** Ask, in one message: *"In a sentence or two: what area of your work is this base for, and what do you keep re-explaining to your AI every time?"*

**Turn 2 - propose the structure.** From their answer, draft and show: (a) 4-6 folders, each named with a one-line purpose and the kind of file it holds, including one dated intake folder where new material lands; (b) a one-page `CONTEXT.md` root map (see shape below); (c) one retrieval prompt they will reuse. Then ask: *"Here is the structure I'd build. Rename folders, drop any you would not open, or say go."*

**Turn 3 - the first file.** Once they approve, ask: *"Give me one real thing from this area, a decision, a note, or a recent signal, and I'll show you the shape of a file so the rest are easy."* Draft that file for them.

**Turn 4 - hand off.** Tell them, in order: create these folders on your own drive; save the `CONTEXT.md`; drop the first file in; paste the retrieval prompt at the start of a session when you want answers from the base; and put a recurring twenty-minute review in your calendar (point them at the weekly-maintenance skill). Then stop.

## The root map shape (CONTEXT.md)

```
# [Name] Context Base

## What this is
[One or two lines: the area, that it is plain files, read this map first.]

## Who I am
[Role and the kind of calls/questions this base serves.]

## How to navigate
- folder/  one line: what lives here, and the question it answers.
  (repeat per folder)

## How to answer
Walk to the right folder, then the right file. Always name the file an
answer came from. If two files disagree, surface both. If the base does
not hold the answer, say so rather than guessing.
```

## A good retrieval prompt looks like

```
Answer from my context base only. Walk the folders in CONTEXT.md, open the
files that fit, and reason over them. Name the file each part of the answer
came from. If the base does not cover it, say so plainly. Question: [...]
```

---

## Fallback: paste-prompt version (for models without skill support)

```
Help me set up a private context base: a folder of plain files you can reason
over for one area of my work. Ask one thing per turn.
Turn 1: ask what area this is for and what I keep re-explaining to my AI.
Turn 2: propose 4-6 folders (each named, one-line purpose, including one dated intake
folder where new material lands), a one-page
CONTEXT.md root map, and one retrieval prompt I will reuse. Let me edit or approve.
Turn 3: ask me for one real decision/note/signal and draft the file so I see the shape.
Turn 4: tell me how to create the folders, save the map, file the first item, use the
retrieval prompt, and set a weekly review. Plain files only: no vector database, no
embeddings, no new platform. Be specific to my area, not generic. Be a critical friend.
```

*Context Base · So What, Now What, Issue 02 · github.com/brownfield-bridge/so-what-now-what · CC-BY 4.0*
