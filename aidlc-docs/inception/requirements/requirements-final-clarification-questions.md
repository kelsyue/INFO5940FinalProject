# BigRedRoutes — Remaining Requirements Clarifications

**Status:** All three responses received. The cloud deployment contradiction is resolved by the user’s explicit single-laptop/no-cloud scope change. Requirements drafted for separate review; no stage approval is implied.

Only these three points remain. Reply with numbered choices and the requested facts; there is no need to paste the whole document again. The earlier recovery options were too cloud-focused for this local project; the choices here address local recovery directly.

## Question 1 — Actual meeting details or explicit deferral
Your last Q1 answer selected A but repeated the instructions without a review date, operator or meeting format. What should the record say?

A) Record actual details now: give the review date, current workflow operator's name, and meeting platform/location (for example: date; name; online via platform, or in person at location).

B) Proceed with those three details explicitly unconfirmed; track them as README/submission follow-up tasks. Whole-team agreement to the inputs/roles/cadence remains recorded as you reported it.

X) Other (please describe after [Answer]: tag below)

[Answer]: X) Nov 24, 2026, all members are present, online via Zoom

## Question 2 — Qwen3 test status on Kelly's laptop
Kelly Yue's laptop is recorded as macOS Tahoe 26.5.2 with 16 GB RAM, as you supplied it. What is the actual `qwen3:4b` test status?

A) Not tested yet; perform model setup and feasibility testing during Construction.

B) Tested or attempted: describe the observed result or issue. This does not establish that the performance target has been met without a benchmark.

C) Test status is not known; proceed with it explicitly unconfirmed and verify during Construction.

X) Other (please describe after [Answer]: tag below)

[Answer]: X) Qwen3:4b works

## Question 3 — Local recovery policy
Previous Q5 selected a cloud single-region/multi-zone option, but the agreed product runs on a laptop. A laptop has no cloud availability zones. Which local recovery policy should requirements use? Choosing A or B replaces that cloud-specific answer; no cloud deployment is introduced.

A) Local backup and restore: target recovery within 30 minutes from a known-good version; automated encrypted SQLite backups at least hourly while the app runs; maximum one hour of saved-plan data loss; retain backups seven days; verify a restore before the demo. If the only laptop and its backup copies are lost, these objectives are not guaranteed. Delete-plan/reset must also remove recoverable copies of deleted plan data, using a verified rewrite/purge or equivalent design, without restoring deleted plans later. No cloud uptime SLA or regional redundancy.

B) Another local backup/restore policy: specify maximum recovery time, maximum acceptable saved-plan data loss, backup frequency/location and retention. Security baseline still requires encrypted backups, and delete/reset behavior must cover recoverable copies. No cloud redundancy is assumed.

X) Other (please describe after [Answer]: tag below; explicitly describe any requested scope change or exception rather than implying local multi-zone availability)

[Answer]: X) We will need it to run on one laptop for the MVP. Change scope to not require cloud

---

**Already resolved:** Dyllan Hofflich owns source permissions/verification/coverage review. Kelly owns the intended demo laptop. Full applicable Security enforcement remains enabled, including the agreed extra local protections; detailed mechanisms await Application Design. Formal change management is exempt because this is a local course prototype with no production service or organizational release process; Git history and actual AI-DLC review/approval gates still apply. Resiliency and full PBT remain enabled. Once these three answers are validated (including any explicit deferrals), requirements can be drafted for a separate review and approval.


## Validation and scope reconciliation

- Q1: November 24, 2026, all members present online via Zoom, as reported. Current session operator not named; retain as administrative follow-up rather than repeatedly blocking product analysis. The previously agreed role identifies Ananya as designated operator, not proof of who operates this session.
- Q2: User reports Qwen3 4B works on Kelly’s declared laptop. No benchmark, tool-call validation or independent test is inferred.
- Q3: Custom answer explicitly replaces cloud multi-zone scope with a single-laptop MVP and no cloud requirement. Production cloud availability/recovery guarantees do not apply. No numeric local RTO/RPO was selected, and the earlier 30-minute/hourly/seven-day proposal is not adopted. Applicable local backup security remains required. The requirements draft presents a concrete automated latest-state snapshot/restore policy for review, not a fabricated prior decision.
- All product responses are recorded. The draft may now be reviewed; acceptance of its proposed local backup behavior must come from actual team approval or requested changes.
