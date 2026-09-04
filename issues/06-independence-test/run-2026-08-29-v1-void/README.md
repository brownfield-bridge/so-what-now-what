# VOID RUN, 29 August 2026, kept on purpose

This run is not valid and its numbers are not used anywhere. It is here because the way it failed is
the most likely mistake you will make, and because a kit that only publishes its clean runs is doing
the exact thing this issue argues against.

**What went wrong.** Two prompts went into the same chat window instead of two fresh ones. The model
had already answered the first, so the second answer was largely the first one restated. Nothing in
the process caught it. The panel looked more independent than it was, which is the failure that
matters here: the error runs in the direction that flatters the result.

**What changed because of it.** Every block now carries a cell id the model must echo back, so an
answer from the wrong chat is visible immediately, and `independence_test.py` stops and names the
cell if two answers claim the same id rather than quietly averaging them.

The valid run is in `run-v3/`.
