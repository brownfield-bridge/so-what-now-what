# Goal quality judge: rubric

You will see a list of development goals written for a manager's next quarter, each with an ID and, where there is one, a first action. You do not know who wrote them. Score each goal on what is on the page only.

Score each of four criteria 0, 1 or 2:

1. **Specific.** 0: a general area ("be a better leader"). 1: a direction with some focus ("delegate more to my leads"). 2: says exactly what will be different ("my leads decide on staffing and budget items under 5k without me").
2. **Observable.** 0: no way to tell if it happened. 1: a vague sign ("I feel less stretched"). 2: something someone could see or count ("I leave by 18:00 four days a week").
3. **In the manager's hands.** 0: depends mainly on others. 1: partly. 2: the manager can make it happen by their own actions.
4. **Time-bound.** 0: no time. 1: "this quarter", "over the quarter" or similar. 2: a date or a named point in time ("by the end of March", "by the end of the quarter").

Total 0 to 8.

Score the goal text only; the action is used only for the last question. If one part of a goal meets a level and another part does not, give the lower score.

Also answer, Yes or No: **Could the manager start on it this week?** (Is there a first step clear enough to do, from the goal and action as written?)

Output one JSON line per goal: {"id": "...", "specific": n, "observable": n, "in_hands": n, "time": n, "total": n, "start_this_week": "Yes|No", "note": "at most 15 words"}

Score each goal on its own. Do not compare goals to each other. Do not guess who wrote it.
