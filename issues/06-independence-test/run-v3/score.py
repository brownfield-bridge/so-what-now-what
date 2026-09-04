import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/github-issue-06")
import independence_test as it

cells = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cells.json")))
reviews = [it.Review(config_id=c["config_id"], verdict=c["verdict"], criticisms=c["criticisms"],
                     family=c["family"], framing=c["framing"], doc="vendor-sheet.md",
                     replicate=bool(c.get("replicate"))) for c in cells]
m = it.LexicalMatcher()
res = it.analyse(reviews, m)
it.report(res, reviews, m)
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "result-lexical.json"), "w"), indent=1, default=str)
