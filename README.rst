WoWHellgarve bug tracker
=======================

Report, investigate and retest gameplay problems across all expansions.
Midnight is the current priority. Client target: **69587**.

* `Report a bug or request <https://github.com/WoWHellgarve-HolyDeeW/WoWHellgarve-Bugtracker/issues/new/choose>`_
* `All reports <https://github.com/WoWHellgarve-HolyDeeW/WoWHellgarve-Bugtracker/issues>`_
* `Needs info <https://github.com/WoWHellgarve-HolyDeeW/WoWHellgarve-Bugtracker/issues?q=is%3Aopen+label%3A%22needs+info%22>`_
* `Ready to test <https://github.com/WoWHellgarve-HolyDeeW/WoWHellgarve-Bugtracker/issues?q=is%3Aopen+label%3A%22ready+to+test%22>`_
* `Sniffs <https://github.com/WoWHellgarve-HolyDeeW/WoWHellgarve-Bugtracker/issues?q=is%3Aopen+label%3Asniff>`_
* `Coverage by scenario <https://github.com/WoWHellgarve-HolyDeeW/WoWHellgarve-Bugtracker/blob/main/coverage/scenarios.csv>`_
* `Existing capture catalogue <https://github.com/WoWHellgarve-HolyDeeW/WoWHellgarve-Bugtracker/blob/main/coverage/captures.csv>`_
* `Capture-to-scenario evidence links <https://github.com/WoWHellgarve-HolyDeeW/WoWHellgarve-Bugtracker/blob/main/coverage/evidence-links.csv>`_
* `Capture request table <https://github.com/WoWHellgarve-HolyDeeW/WoWHellgarve-Bugtracker/blob/main/coverage/requests.csv>`_
* `Issue table snapshot <https://github.com/WoWHellgarve-HolyDeeW/WoWHellgarve-Bugtracker/blob/main/reports/issues.csv>`_

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
Use one type label and, when useful, one status label:

* **bug**, **suggestion** or **sniff** describes the report.
* **needs info**, **in progress** or **ready to test** shows the next stage.

GitHub's Open/Closed state shows whether the report is resolved. Keep technical
findings, evidence, priority and the fix revision in the description or comments.
The staff reports what happened; maintainers handle the technical investigation.

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
requests. Issues and labels show the live state. CSV tables are a dated snapshot;
automatic export is prepared but currently inactive. Maintainers can refresh
the tables with ``python3 scripts/export_tracker.py`` and commit the result.
Never maintain a separate manual issue status in Excel.

Keep original PKTs, authentication logs, passwords, tokens and private library
paths outside this repository. Share raw captures through the existing private
library; public issues use capture IDs and sanitized observations.

Prefer current expansion content, while retaining useful older systems such as
Mythic+, Timewalking and Chromie. A newly captured client build does not update
the realm build. Realm upgrades require substantial content or an important fix.
