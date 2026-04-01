# Swarmcore Prototype Specs (V2)

High-level ideas for future enhancements based on the Anthropic Claude Code leak.

## Planned Integrations

1. **Tripwire Layer (Anti-Distillation)**
   - Inject mock dangerous tools (e.g. delete_all_volumes)
   - Use iba-claw-starter to immediately block and flag malicious attempts

2. **Strict State Verification**
   - Executor must always verify current state with a READ/STAT before WRITE/EXECUTE
   - If dreamweave memory hint doesn't match reality → trigger re-analyze

3. **Enhanced Dream Loop (Kairos-style)**
   - Summarizer runs a "dream" pass after each task
   - Detect contradictions and merge into a single TRUTH_STATE

4. **Stronger IBA Enforcement**
   - Every environment-changing action must match a signed human intent
   - No auto-approved lateral movement

## Current Status
Basic coordinator + Dreamweave memory + Matey companion is working.
Advanced patterns above are for future iterations.

See also:
- grk-html-2 (IBA demo)
- iba-claw-starter (governance)
- dreamweave (memory)
- matey (companion)
