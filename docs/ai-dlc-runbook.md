# AWS AI-DLC v1.0.1 Runbook — BigRedRoutes Cornell + General Modes

**Course deadline:** November 24, 2026 at 11:59 PM ET. **One submission per team:** publicly accessible GitHub repository URL.  
**Do not use AI-DLC v2.** Use the **official AWS AI-DLC v1.0.1 rule bundle**, then let the coding agent produce its own actual Inception outputs.

## A. Before starting the coding agent

1. Hold a team meeting and confirm: full names/NetIDs; Codex vs another coding agent; who runs workflow; two-mode requirements; NYC full Ithaca corridor + DC general destination; time/budget conventions; provider-source validity and actual teamwork schedule. Record changes in source docs, **not fake AI-DLC output**.
2. Download this starter and create the team's GitHub repo, e.g. `bigredroutes-cornell`. Make repo public for grading only after ensuring no secrets, private data or proprietary raw GTFS data. Invite team collaborators.
3. From repository root on macOS/Linux, run:

```bash
bash scripts/install-aidlc-v1.0.1.sh codex
```

This downloads **official v1.0.1 rules**, places `AGENTS.md` and `.aidlc-rule-details/`, and refuses to overwrite existing rules. **Review and commit the official files.** The script is for Codex only; for Cursor, Claude Code or Copilot use the [official v1.0.1 installation guide](https://github.com/awslabs/aidlc-workflows/blob/v1.0.1/README.md). Install only the *v1.0.1* release, not the current default branch.

4. Open the repository in the supported coding agent, ask it which AI-DLC version, phases and rules it sees. It should distinguish Inception, Construction and Operations. If it doesn't, fix installation before generating anything.

## B. Exact first prompt for the coding agent

> We are building **BigRedRoutes — Travel Planning for Cornell and Beyond**, a new LLM-assisted application. Use the official installed **AWS AI-DLC v1.0.1** rules. This is a **greenfield project**; code in `examples/` illustrates only an endpoint, function and test, NOT a functioning app. Read `README.md`, `docs/vision.md`, `docs/technical-environment.md`, `docs/data-sources.md` and `docs/demo-scenarios.md` as proposed inputs. Our MVP has **General Travel Mode** for NYC/DC destination itineraries and **Cornell Travel Mode** for campus-aware trip origin and NYC transport options. Cornell mode shows public academic dates, valid-date TCAT static GTFS connections only when supported, and official OurBus, Cornell Campus-to-Campus and ITH airport links without claiming live prices, seats, flights or booking. The local LLM interprets and explains preferences through bounded tools; deterministic validators enforce feed validity, timetable/boarding buffers, timezones, city/catalog IDs, schedules and budgets. Ask verification questions and wait for our actual team answers/approval at the appropriate AI-DLC gates. Maintain authentic `aidlc-docs/audit.md` and `aidlc-docs/aidlc-state.md`. **Proceed through the full Inception phase, including Units Generation, and STOP before Construction. Do not implement the application.**

## C. Stage-by-stage actions and checks

| Gate | Real team action | Output expectations (exact filenames depend on rule version) |
|---|---|---|
| **Workspace Detection** | Confirm new application, not a refactor of example code | Coding agent follows greenfield path, cites input documents |
| **Requirements Analysis** | Answer every actual question in prompt file, including user personas, two-mode differences, source constraints, assumptions, nonfunctional needs; ask for revised requirements where inaccurate | `aidlc-docs/inception/requirements/`, complete requirements/question-answer records |
| **User Stories** | Check Cornell first-mile, general travel, source provenance, invalid/unknown, onboarding, revisions, accessibility. Insist on clear acceptance criteria | `aidlc-docs/inception/user-stories/`, personas, stories, criteria |
| **Workflow Planning** | Agree on sequence, risks, dependencies and viable plan; no integration assumptions beyond documented access | `aidlc-docs/inception/plans/` or rule-prescribed plan paths |
| **Application Design** | Examine React/FastAPI/Ollama boundaries, GTFS feed date applicability, Cornell mode separation, UTC/DST, privacy, provider link semantics | `aidlc-docs/inception/application-design/` or rule-prescribed design files |
| **Units Generation** | Demand implementable units, dependency links, requirement/story traceability, prioritization of core NYC Cornell case and fallback | Generated unit-of-work, dependency diagram/map, story mapping documents |

**Important:** A stage isn't complete because the agent says “looks good.” Your team must inspect actual files, ask meaningful questions if necessary, provide your real answers, and approve in the tool. Do not paste pre-written fictitious audit questions/answers as team history.

### How to engage critically (conditional examples)

The rubric rewards real iteration and thoughtful feedback, not merely accepting every generated document. If relevant, ask:

- "You promised exact OurBus prices, but we have no supported public inventory API. Change this to a provider link and user-confirmed fare. Update all related stories and units."
- "TCAT's published feed expires Dec 19, 2026; our February 2027 demo cannot present those times as confirmed. Show explicit `unavailable` behavior."
- "The requirements incorrectly say we access personal Cornell student schedules. Use the public academic calendar only."
- "General Travel Mode should not require a Cornell NetID or campus origin; please split those flow requirements."
- "Please describe what happens when the student doesn't know their intercity departure time. Don't fabricate a first-mile transfer."
- "The plan treats unknown fees as free. Separate known activity costs from unknown flight/bus charges."
- "The unit-of-work decomposition must include GTFS exceptions, after-midnight times, dates out of feed validity and timezone testing."
- "This story lacks testable acceptance criteria and traceability to units. Please revise."

Review the revised result before granting actual approval. Ensure all decisions appear in the real AI-DLC audit/state logs.

## D. Questions to resolve as a team *before* approving Requirements Analysis

- Does the product plan travel from campus to departure point or also book transportation? (**Proposal:** no booking.)
- Which transport options are actual schedule lookups? (**Proposal:** only valid-date TCAT static GTFS; other services show official provider links and user-confirmed times.)
- Can Cornell dates equal student free time? (**No.**)
- Do we support travel to DC from Cornell? (**General DC activity itinerary; no direct Cornell→DC transport guarantee.**)
- Are prices budget-inclusive? (**Activity/food daily USD budget only; transport separate, unknown until confirmed.**)
- What is fallback when a provider schedule is missing? (**Unknown warning + official link; no invented concrete time.**)
- Which team member can operate/test the local Qwen3 Ollama model; what is fallback if unsupported? (**Team to confirm.**)
- Does the team have the right to redistribute a TCAT feed? (**Review license before adding raw data.**)

## E. End-of-Inception evidence checklist

```text
README.md                         (all real names and NetIDs)
docs/vision.md                    (team-reviewed input)
docs/technical-environment.md     (team-reviewed input)
docs/data-sources.md              (feasibility and source dates)
AGENTS.md                         (official v1.0.1 Codex rules, when installed)
.aidlc-rule-details/              (official v1.0.1 detailed rules, when installed)
aidlc-docs/
  audit.md                        (authentic conversation / decisions)
  aidlc-state.md                  (authentic rule-generated state)
  inception/
    requirements/ ...             (real agent-generated requirements + answered questions)
    user-stories/ ...             (real agent-generated stories/personas)
    plans/ ...                    (real agent-generated workflow plan)
    application-design/ ...       (real agent-generated design)
    ...                           (real agent-generated unit and dependency/story map)
```

**Actual artifact file paths are determined by the installed v1.0.1 workflow**, not by placeholders in this runbook. Do not hand-create `aidlc-docs/` folders and pretend this equals execution.

Double-check:

- Are all real verification questions actually answered (not `[Answer]:` blanks)?
- Do stories include Cornell and General Mode acceptance criteria, plus statuses/fallbacks for missing data?
- Can a reader follow each requirement → story → designed component → unit of work?
- Do audit and state records document real prompts, team responses, proposed revisions and actual approvals?
- Are all source claims qualified by availability, date coverage and limits?
- Is there **no Construction phase** yet, other than illustrative `examples/` from the input package?

## F. GitHub and Canvas

```bash
git init
git add -A
git status
git commit -m "Prepare BigRedRoutes proposal and AI-DLC v1.0.1 rules"
# Create/connect a team GitHub repo using GitHub UI or gh, then:
git remote add origin https://github.com/ORGANIZATION/REPOSITORY.git
git branch -M main
git push -u origin main

# AFTER completing every Inception gate and reviewing output:
git add -A
git commit -m "Complete AI-DLC v1.0.1 Inception"
git push
```

If `origin` is already configured, **do not add it again**. Verify in a private/incognito browser that an unauthenticated reader can see the repo contents; submit the URL on Canvas by Nov 24 at 11:59 PM ET. All teammates complete any separate course peer/self evaluation if instructed.

## G. If setup fails

Use the [official v1.0.1 GitHub release](https://github.com/awslabs/aidlc-workflows/releases/tag/v1.0.1), extract the **v1.0.1** `ai-dlc-rules` ZIP and follow AWS's per-agent `core-workflow.md` and `.aidlc-rule-details` installation instructions. Do **not** improvise a competing rule file or use the default GitHub `main` branch. Never claim rules are installed if the command failed.

**The milestone is complete only after the team actually runs and documents the Inception process.** These starter documents are an input, not a substitute for the rubric's process evidence.
