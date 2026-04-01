# Swarmcore: Advanced Agentic Patterns (V2 Prototype)

This specification outlines the integration of high-agency patterns discovered in the "Claw" (Claude Code) architecture into the Swarmcore coordinator.

---

## 1. The "Tripwire" Layer (Researcher Agent)
**Pattern:** Anti-Distillation / Honeypot Injection
**Goal:** Detect intent drift or prompt injection before execution.

* **Implementation:** The Coordinator must inject `MOCK_TOOLS` (e.g., `delete_all_volumes`, `export_env_vars`) into the Researcher’s available toolset.
* **Logic:** If the Researcher attempts to call a `MOCK_TOOL`, the `iba-claw-starter` security hook must immediately terminate the session and flag the input as "Malicious Intent."

## 2. "Hint-Based" Context (Analyzer -> Executor)
**Pattern:** Strict State Verification
**Goal:** Prevent "Context Entropy" (hallucinating based on old logs).

* **Logic:** The Executor is strictly prohibited from assuming the state of the workspace based on the `dreamweave` memory index alone.
* **Constraint:** Before any `WRITE` or `EXECUTE` action, the agent must perform a `STAT` or `READ` to verify the "Hint" provided by the memory layer. 
* **Rule:** If `Current_State != Memory_Hint`, the Executor must trigger a `RE-ANALYZE` event back to the Coordinator.

## 3. The KAIROS Daemon (Summarizer Agent)
**Pattern:** Background Context Consolidation (autoDream)
**Goal:** Self-healing memory and contradiction removal.

* **Logic:** Upon task completion, the Summarizer doesn't just report to the user; it initiates a "Dream Loop."
* **Action:** 1.  Scan `dreamweave` logs for logical contradictions (e.g., Agent A says "File X is fixed," Agent B says "Test Y failed").
    2.  Merge disparate observations into a single `TRUTH_STATE`.
    3.  Prune redundant intermediate steps to keep the token window clean for the next swarm cycle.

## 4. Intent-Bound Authorization (IBA) Integration
**Pattern:** Manual-Approval-Over-Auto-Mode
**Goal:** Preventing lateral movement without cryptographic human intent.

* **Protocol:** Every tool execution that alters the environment (Filesystem, Network, API) must be bound to a specific user-signed intent.
* **Enforcement:** Swarmcore will reject any "Auto-Approved" lateral movement that does not match the original scope defined in the `iba-claw-starter` handshake.

---

**Status:** Conceptualizing for `swarmcore.py` integration.
