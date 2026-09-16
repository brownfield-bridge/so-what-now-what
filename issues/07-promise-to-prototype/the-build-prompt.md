# Repair or replace — build prompt

Build a single-page web tool. No account, no backend, no sign-in.

## The job

A householder is standing in a kitchen. Their washing machine has broken after the guarantee ran out, a repairer has quoted them, and they have to say yes or no today.

The tool exists so that this is true for them afterwards:

> **"I know whether it is worth fixing, instead of guessing."**

## What the user enters

Five things, and nothing else: the make, the age, what the machine is doing wrong, the repair quote, and the price of a comparable new machine.

Then one more, which is theirs and not ours: **their own rule.** Most people have one and have never written it down - replace above half the price of a new machine, repair below a quarter, argue with yourself in between. Ask for it. Do not assert one.

Optionally: whether they are moving house or replacing the kitchen within two years, which shortens the time the repair has to cover.

Ask for nothing else. No email, no address, no account. Every field collected is a field computed on.

## What it computes, and what from

A set of past repair jobs: make, age, fault, what was done, what it cost, and whether the same machine came back. **This data is invented for the demonstration.** Use makes that are obviously not real brands. Never use the name of a real manufacturer anywhere in the tool.

**Every figure the tool shows comes from those records or from the user. Nothing is looked up.** There are no lifespan tables, no reliability averages, no typical-cost figures and no constants standing in for how machines behave. If a number has no source in the records or in what the user typed, the tool does not show it.

From those records, for this fault on this make at this age:

- what the repair has historically cost
- how long it has held
- **whether something else tends to fail soon afterwards, and what that follow-on has cost**

The third is the point. Anyone can divide a quote by the price of a new machine. Nobody can tell you that on a machine like this, something else usually goes within the year. Add the likely follow-on to the quote and show the user both numbers: what they were quoted, and what it is likely to cost in total.

Then place that figure against **their** rule and tell them which side of their own line it falls on.

The forecast does not move. Only the line does.

## The walk-away price

Also compute the most it is worth paying to fix this machine, given the years it has left.

Three conditions on how this appears:

1. **It appears only after the user has entered their quote.** Never before.
2. **It is a stop-loss during the job, not a fair price before it.** The case it exists for is the engineer opening the machine and finding more. Word it that way: *if the total passes this while the job is open, stop there.*
3. **The screen says what it is not:** this is not an estimate of what the repair should cost.

## Running cost

An old machine uses more electricity than a new one, and over the years a repair buys, that can matter more than the repair bill.

Let the user type in the annual energy figure from the label of the new machine they are actually considering, as an optional field. It is their candidate machine and their label; the tool holds no energy figures of its own and invents none.

**Show what the old machine draws as unknown, because it is.** Do not estimate it, do not age it by a rule of thumb, do not put a number on it. Tell the user the two ways to find out: the machine's own energy label, or a plug-in meter. The unknown must look like a real property of the problem, not like a field the user forgot to fill in.

Running cost is shown alongside the verdict. It is never a term in it.

## Currency

The records have a currency. **Report it; do not offer the user a choice of currency.** A tool that lets someone pick a currency the data is not in is displaying a unit error as a feature.

## When it must not answer

**Thin data.** If there are only a handful of matching jobs, do not give a percentage. A percentage off five jobs is a guess wearing a percentage sign. Show the jobs themselves, say the sample is too small, and tell the user to ring a second repairer. Record the question as one the tool could not answer.

**Safety.** A burning smell, scorch marks, a gas smell, a shock, or water near the electrics stops everything - before the tool has even asked what the machine is. No arithmetic, no verdict. Unplug it and get a qualified engineer.

**Empty.** The tool opens with no records at all, because that is the honest starting state. The demonstration data is something the user switches **on**, not something they switch off. With it off, every question comes back the same way: ring a second repairer, that is the call this tool exists to save you, and on this machine it has not earned it.

## What it will not claim

The tool makes no claims about how appliances behave. It has no opinion on which parts are cheap, how long a make lasts, or what usually goes wrong with a brand. It reports what is in the records and nothing else.

Anything it tells the user to ask about is about **the transaction**, not the machine. Before agreeing to a job: is the call-out fee credited against the repair, does the repair carry twelve months on parts and labour, and is the part still manufactured.

## What it says about itself

On screen, not buried in a footer: the records are invented for demonstration, the sample is one repair business in one town, and here is what the comparison leaves out.

Scope is one appliance category - washing machines - the five most common faults, and three makes. The tool does not pretend to cover more.

## Left to you

How confidence is expressed: numbers, words or a band. What the thin-data screen shows beyond saying it is thin. Whether the reasoning sits inline or behind a control. Interaction, layout and flow throughout.

Make it good to look at. Make the refusals as well designed as the answers - they are the screens the tool is for.
