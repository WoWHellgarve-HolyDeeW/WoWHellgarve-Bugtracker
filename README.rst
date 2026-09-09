WoWHellgarve bug tracker
=======================

Report, investigate and retest gameplay problems across all expansions.
Midnight is the current priority. Client target: **69587**.

* `Report a bug or request <https://github.com/WoWHellgarve-HolyDeeW/WoWHellgarve-Bugtracker/issues/new/choose>`_
* `All reports <https://github.com/WoWHellgarve-HolyDeeW/WoWHellgarve-Bugtracker/issues>`_
* `Needs reproduction <https://github.com/WoWHellgarve-HolyDeeW/WoWHellgarve-Bugtracker/issues?q=is%3Aopen+label%3A%22status%3Aneeds-reproduction%22>`_
* `Ready for staff retest <https://github.com/WoWHellgarve-HolyDeeW/WoWHellgarve-Bugtracker/issues?q=is%3Aopen+label%3A%22status%3Aretest%22>`_
* `Capture requests <https://github.com/WoWHellgarve-HolyDeeW/WoWHellgarve-Bugtracker/issues?q=is%3Aopen+label%3A%22kind%3Acapture%22>`_
* `Coverage by scenario <https://github.com/WoWHellgarve-HolyDeeW/WoWHellgarve-Bugtracker/blob/main/coverage/scenarios.csv>`_
* `Existing capture catalogue <https://github.com/WoWHellgarve-HolyDeeW/WoWHellgarve-Bugtracker/blob/main/coverage/captures.csv>`_
* `Capture-to-scenario evidence links <https://github.com/WoWHellgarve-HolyDeeW/WoWHellgarve-Bugtracker/blob/main/coverage/evidence-links.csv>`_
* `Capture request table <https://github.com/WoWHellgarve-HolyDeeW/WoWHellgarve-Bugtracker/blob/main/coverage/requests.csv>`_
* `Issue table <https://github.com/WoWHellgarve-HolyDeeW/WoWHellgarve-Bugtracker/blob/main/reports/issues.csv>`_

For staff
---------
Use one issue per distinct failure. Include actual and expected behavior,
numbered steps, client build, quest/NPC/map/dungeon IDs when known, difficulty,
character context and any GM commands. Unknown IDs are allowed; the report
will need reproduction. Report ordinary gameplay without progression skips
where possible, and identify any commands used.

Reports and tables are public. A GitHub account can open and comment on issues.
The repository owner administers the tracker. Additional maintainers need to
be added explicitly; reporting does not require access to the core repository.

For triage and fixes
-------------------
Keep workflow status, cause and evidence separate:

* Workflow: triage, needs reproduction, investigating, blocked, coding,
  awaiting deployment, retest, verified, or needs decision.
* Cause: unknown, core logic, port/database mapping, missing implementation,
  parser, missing data, configuration or a product request.
* Evidence: unreviewed, located, partial, missing after review, or not applicable.

Labels are the current issue state. The imported issue text records the initial
triage and its date. Update labels and add a dated finding when new evidence
changes the diagnosis. Keep one label per status, priority and cause.

Search existing captures, DB2, legacy databases and code before requesting more
sniffs. A parser failure is different from missing capture data. Link the bug,
coverage ID, capture IDs and fix revision. A commit or SQL import does not prove
gameplay success. Use RETEST_COMMENT.txt on the original issue, and close it
after the original steps pass on the installed revision.

Evidence and coverage
---------------------
The catalogue contains **278 unique captures**, deduplicated by SHA256.
The initial roadmap contains **19 known scenarios**; it is not a complete list
of every WoW quest or zone. A capture name or observed ID is a search lead.
Captured, parsed, integrated and verified in game are distinct states.
The capture links currently identify campsite/purchase requests located in the
full-pass inventory. They do not certify those systems' payloads or gameplay.

The coverage tables are curated by maintainers through GitHub edits or pull
requests. The issue table is exported from live issues by the repository's
issue-event workflow. Never maintain a separate manual issue status in Excel.

Keep original PKTs, authentication logs, passwords, tokens and private library
paths outside this repository. Share raw captures through the existing private
library; public issues use capture IDs and sanitized observations.

Prefer current expansion content, while retaining useful older systems such as
Mythic+, Timewalking and Chromie. A newly captured client build does not update
the realm build. Realm upgrades require substantial content or an important fix.
