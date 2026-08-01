# Connect it to your tools

The `sources/` folder is the simplest place to start, and the right one: it works today, it is fully in your control, and it makes the agent's rule concrete, every figure traces to a file you can open. But the agent does not have to live on a folder. It can read straight from the tools your sources already sit in, and it can hand the finished pack back to you through one of them. Two kinds of tool touch, both safe by design.

## 1. Read from where the sources already live (read-only)
In an agent app that has a read-only connection to your systems, point the agent at the tool instead of the folder and it pulls the sources itself.

- **Email.** Point it at the monthly finance thread, or the label you file the reports under, and it reads the latest numbers from there.
- **Drive or SharePoint.** Point it at the folder your team drops the exports in, and it reads them live.
- **CRM, ERP, BI, data warehouse.** If your app has the integration, it reads the figures directly.

Nothing else changes: the brief, the template, and the self-check pass stay exactly as they are. Only *where the sources come from* changes. No connector for your system? Have it drop a scheduled read-only export into `sources/` just before the run, and the agent reads a folder that is kept current for you.

## 2. Deliver the finished pack back to you
The agent takes exactly one action out in the world, and it is aimed at you. On a run, especially a scheduled one, it delivers the sign-off-ready draft and the red-pen review straight to you: emails it to yourself, drops it in your review folder, or posts it to your own channel, so it is waiting the morning it is due. It delivers to **you**, never to the recipients of the report.

## The guardrails that do not move
- **It reads; it never writes back.** It pulls figures and produces a draft. It never edits, sends into, or deletes anything in a source system (CRM, ERP, ledger, inbox, calendar). Read-only in, a checked draft out.
- **It delivers to you, never for you.** The one outbound action is handing the finished draft to the owner. It never sends the report onward to its recipients, and it never approves its own work. Your name goes on the result.
- **Everything else holds.** Every figure still cites its origin, the self-check still assumes the draft is wrong until a source proves it right, and financial and forward-looking lines still route to a named human.

Start on the folder. Connect a tool the moment refilling the folder by hand is the only thing slowing you down.
