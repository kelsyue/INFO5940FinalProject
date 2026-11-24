# BigRedRoutes — Requirements Clarification Questions

**Status:** Six responses received and recorded from the conversation. Q2/Q4/Q6 resolved; Q1 lacks requested facts, Q3 lacks model test status, and Q5 conflicts with local-only deployment. See `requirements-final-clarification-questions.md`. These answers are not stage approval.

Your option text maps unambiguously to the original choices, so it has been recorded with the corresponding letters. Q7 is recorded as your custom answer: return a partial plan, explain unmet constraints and ask which constraints the user wants to change before applying changes. No need to repeat those decisions.

This follow-up addresses missing details in original Q1/Q3/Q9 and additional decisions required after enabling the extensions. Answer with a letter and the requested details. You may explicitly defer unknown operational details rather than invent them.

## Question 1 — Review date, operator and meeting format (original Q1)
You confirmed all four members reviewed and agreed to the inputs, roles and cadence, but the response repeated the request for the date/operator/format without supplying them. How should those details be recorded?

A) Record the actual details now: provide the review date, workflow session operator, and whether meetings are in person or online, including location/platform. The agreed cadence remains two 45-minute meetings per week plus GitHub Issues/PR comments.

B) Record the whole-team agreement as reported, explicitly leave the review date/operator/meeting format unconfirmed, and track confirmation before submission. Do not claim a meeting date or format.

X) Other (please describe after [Answer]: tag below)

[Answer]: A) Record the actual details now: provide the review date, workflow session operator, and whether meetings are in person or online, including location/platform. The agreed cadence remains two 45-minute meetings per week plus GitHub Issues/PR comments.

## Question 2 — Named source-data reviewer (original Q3)
Who owns source permission review, Registrar/provider verification and checking feed coverage before the demo?

A) Dyllan Hofflich, consistent with the proposed transport/data role you accepted.

B) Another team member: provide their name and any split of responsibilities.

X) Other (please describe after [Answer]: tag below; explicitly deferring the owner is acceptable if tracked as a delivery task)

[Answer]: A) Dyllan Hofflich, consistent with the proposed transport/data role you accepted.

## Question 3 — Demo laptop and actual model test status (original Q9)
How should the intended laptop and model feasibility check be recorded?

A) The machine is chosen: provide owner, OS, RAM and actual `qwen3:4b` test status (not tested / attempted with observed issue / tested with observed result). No benchmark is inferred from selecting a laptop.

B) Machine selection and model test are not yet confirmed. Track both as Construction prerequisites; the 120-second performance target remains unmeasured until a machine is declared and tested.

X) Other (please describe after [Answer]: tag below)

[Answer]: A) The machine is chosen: provide owner, OS, RAM and actual qwen3:4b test status (not tested / attempted with observed issue / tested with observed result). No benchmark is inferred from selecting a laptop. Owner: Kelly Yue (macOS Tahoe 26.5.2) Memory 16gb

## Question 4 — Security baseline versus minimal local setup (original Q14)
You enabled every SECURITY rule. The supplied technical environment proposes SQLite, loopback HTTP and no user accounts, but the enabled baseline also requires encrypted persistence (SECURITY-01), centralized structured logging and protected audit logs (SECURITY-03/14), HTTP security headers (SECURITY-04), and resource authorization (SECURITY-08). Local-only operation does not by itself make those application/storage rules inapplicable. Which requirement set should govern?

A) Keep full enforcement of applicable SECURITY rules and accept the extra local setup/design work. Require encrypted persistent stores/backups with OS-managed or equivalent keys, protected centralized local logs with defined retention, an HTTPS-capable local serving setup with required headers, and authorization for saved-plan operations (a local bootstrap/session identity is allowed; no Cornell login or external accounts). Detailed mechanisms will be proposed for approval during Application Design. Cloud-only controls are N/A only with an explicit rationale; no implementation compliance is claimed yet.

B) Revise original Q14 to disable the optional SECURITY baseline for this course prototype. Retain the product-specific safeguards already agreed in the inputs: loopback binding, schema validation, restricted tools/origins, no raw chat persistence, safe errors, no secrets in Git and no provider credentials or bookings. Document the change rather than pretending full baseline compliance.

X) Other (describe the exact requested scope or exceptions after [Answer]: below; any exception must be explicit and cannot be reported as full baseline compliance)

[Answer]: A) Keep full enforcement of applicable SECURITY rules and accept the extra local setup/design work. Require encrypted persistent stores/backups with OS-managed or equivalent keys, protected centralized local logs with defined retention, an HTTPS-capable local serving setup with required headers, and authorization for saved-plan operations (a local bootstrap/session identity is allowed; no Cornell login or external accounts). Detailed mechanisms will be proposed for approval during Application Design. Cloud-only controls are N/A only with an explicit rationale; no implementation compliance is claimed yet.

## Question 5 — RTO/RPO Goals and Disaster Recovery Strategy (RESILIENCY-02)
What are your Recovery Time Objective (RTO) and Recovery Point Objective (RPO) goals? These determine the appropriate Disaster Recovery strategy and infrastructure redundancy level.

**Local-project note:** RTO is the maximum tolerated recovery time; RPO is the maximum tolerated loss of saved work. The official options below are cloud-oriented. For this local-only course app, use X to specify a local backup/restore policy or explicitly state that saved itineraries are disposable and recreation is acceptable. Do not choose a cloud topology solely to answer this question; cloud deployment remains outside the MVP.

A) RPO/RTO: Hours — Backup & Restore strategy. Lowest cost ($). Data backed up, no services deployed. Redeploy from IaC and restore from backups on failure. Suitable for non-critical workloads.

B) RPO/RTO: 10s of minutes — Pilot Light strategy. Cost: $$. Data live, services idle. Infrastructure deployed but not running, scaled up on failover. Suitable for important workloads.

C) RPO/RTO: Minutes — Warm Standby strategy. Cost: $$$. Data live, services run at reduced capacity. Scaled up during failover. Suitable for business-critical applications.

D) RPO/RTO: Near real-time — Multi-site Active/Active strategy. Highest cost ($$$$). Data live, live services in multiple regions simultaneously. Suitable for mission-critical, zero-downtime requirements.

E) N/A — Single-region deployment is acceptable, no cross-region DR needed. Rely on multi-zone availability within one region.

X) Other (please describe after [Answer]: tag below). One local proposal you may accept or change: recover the demo app within 30 minutes from a pinned known-good version; automated encrypted SQLite backups at least hourly while running; maximum one hour of saved-plan data loss; retain backups seven days; verify a restore before the final demo. No cloud SLA or regional redundancy. Deletion/reset must remove associated recoverable plan copies or explicitly resolve backup retention before approval.

[Answer]: E) N/A — Single-region deployment is acceptable, no cross-region DR needed. Rely on multi-zone availability within one region.

## Question 6 — Change Management Process (RESILIENCY-03)
How should production changes for this workload be governed? AI-DLC will conform the design to your answer rather than inventing a process. For this project, interpret changes as changes to the shared local demo release.

A) Use our existing organizational change management process — provide the name/tool (e.g., ServiceNow, Jira Change, internal CAB). AI-DLC will reference it and ensure deployable artifacts fit that process (change records, approval gates).

B) No formal process exists yet — AI-DLC should propose a lightweight change management process (change record + approval + rollback note) for the team to adopt.

C) N/A — this workload is exempt from formal change management (e.g., internal tooling). Document the exemption rationale.

X) Other (describe after [Answer]: tag below)

[Answer]: C) N/A — this workload is exempt from formal change management (e.g., internal tooling). Document the exemption rationale.

---

**Extension follow-through:** Security, Resiliency and full PBT are currently enabled per original Q14–Q16. Security applicability is being resolved by Q4; it has not been silently disabled. The resiliency questions specifically allowed during NFR Design (CI tooling, rollback, deployment style, incident response and testing) will be handled at that gate unless explicitly decided sooner. Multi-region infrastructure is outside the local-only MVP; topology applicability will be documented without inventing a cloud deployment. Full PBT remains enabled; framework selection, property identification and generated tests will be required at their applicable design/Construction gates, not falsely marked implemented now.


## Validation of follow-up answers

- Q1: A selected, but no review date/operator/meeting format supplied; not inferred.
- Q2: Dyllan Hofflich confirmed as data/source reviewer.
- Q3: Kelly Yue, macOS Tahoe 26.5.2, 16 GB RAM reported by user. Model test status not supplied. This OS description is recorded as reported, not independently verified.
- Q4: Full applicable SECURITY rules retained; additional local safeguards authorized for later design, not implemented or approved as a detailed design.
- Q5: E explicitly selects a cloud multi-zone configuration, while the established scope is local-only. No cloud topology or recovery targets inferred; local clarification required.
- Q6: Formal change-management exemption selected. Rationale: local educational prototype without a production service/organizational release process; existing Git history and AI-DLC gates remain required.


## Subsequent clarification outcome

See `requirements-final-clarification-questions.md` and the audit: the team reports the November 24 Zoom review, Qwen3 working on Kelly’s laptop, and explicitly requires a single-laptop/no-cloud MVP. This supersedes the earlier cloud multi-zone selection. All supplied answers remain preserved above; no approval of generated requirements is inferred. See the draft `requirements.md` for reconciled requirements and explicitly proposed local backup behavior.
