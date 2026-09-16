# Prompt it first. Then decide what it must never do.

**So What, Now What - Issue 7 · Saturday 19 September 2026**

Two prototypes of the same thing, an afternoon each. One was built from a single sentence typed into a chat window. The other was built from a prompt written after looking hard at what the first one produced.

This folder is everything it took, in the order it happened.

---

## Do this first, it takes five minutes

**1. Type one line into any assistant.** Badly. With typos. Here is mine, exactly as I sent it:

> Prepare a simple app for the user of house appliance which has broken after the guarantee period and he needs an advice to replace or to repair.

**2. Look at what comes back, and write down three lists.**

- Every number in it that has no source.
- Every place it gave a verdict it had no grounds for giving.
- Every threshold it picked on your behalf without asking.

**3. That is your specification.** You could not have written it before you saw the thing. Now prompt it again properly, and let the second build show you what you still got wrong.

That is the whole method. Everything below is the worked example.

---

## The two builds

| | Built from | What it does well | What it will not do |
|---|---|---|---|
| **[Build 1](builds/01-from-one-line.html)** | one sentence | cost per year of service, running cost, a walk-away price | say *I do not know* - not once, in any combination tried |
| **[Build 2](builds/02-from-the-prompt.html)** | [the prompt](the-build-prompt.md) | refuses on thin data, asks for your rule, shows the evidence, names its unknowns | cover more than one appliance, five faults, three makes |

Both open in a browser with no install and no backend. **Every record in both is invented** and labelled as invented on screen. No repair business's data was used and no manufacturer is named anywhere in either.

---

## The files

**[01 - the one line](the-one-line.md)** · what was typed, and what came back.

**[02 - the promise]()** · the filter everything went through.
- [the short form](promise-short-form.md) - one page. The promise sentence, the six fields, and the list of what the tool is never allowed to do. **Start here.**
- [promise.skill.md](promise.skill.md) - the full eighteen-question interview, if you want to run it properly on your own promise. Paste it into any assistant and say *run this on my promise*.
- [the brief behind build 2](the-brief.md) - the working document, with both gaps published rather than filled in.

**[03 - the build prompt](the-build-prompt.md)** · the clean prompt that produced build 2. Copy it, change the domain, keep the shape.

**[04 - what was taken and what was refused](taken-and-refused.md)** · the seven things on the table and the rule that struck three of them. **The most useful page here if you only read one.**

**[05 - build notes](BUILD-NOTES.md)** · what went wrong, including a contaminated run that had to be killed, and the one-number test that flips build 1 from repair to replace.

**[SOURCES.md](SOURCES.md)** · the two sources, how each was read, and what the issue does not claim.

**[the-long-way-round/](the-long-way-round/)** · the first brief, written before anything was built, and the build that came out of it. Kept as a record, not offered as a template. Read the issue before you read that folder.

---

## What this is not

**Not a venture.** Nobody is starting this. There is no company, no platform, no waiting list.

**Not a study.** One domain, one weekend, two artefacts. It shows what happened once.

**Not a substitute for talking to customers.** There is no discovery here, no interviews and no baseline. The promise scores five out of six, and the missing one is that nobody measured what people do today. That is in writing in the brief rather than quietly left out.

---

*Issue 7 of So What, Now What · CC-BY 4.0 · Arguments and voice are mine. Claude is used as an editing and scaffolding tool - and in this issue, as the builder of both prototypes.*
