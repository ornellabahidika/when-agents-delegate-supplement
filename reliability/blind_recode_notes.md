# Blind Recode: Method Notes

Date of coding: 2026-09-27
Coder: independent blind coder (no exposure to any prior verdicts, papers, repos, or notes about delegation-accountability audits; primary sources only).

## Pages fetched (all on 2026-09-27, via live fetch)

MCP (Model Context Protocol, spec revision 2026-07-28 unless noted):
- https://modelcontextprotocol.io/specification/2026-07-28 (spec index, incl. Security and Trust & Safety principles)
- https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization
- https://modelcontextprotocol.io/specification/2026-07-28/architecture
- https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices (served content self-identifies as the current best-practices document; includes Confused Deputy, Token Passthrough, Scope Minimization)

A2A (Agent2Agent 1.0.0):
- https://a2a-protocol.org/latest/specification/ (two passes: one broad across the five conditions, one focused on Section 7 authentication/authorization, task IDs, roles, AgentCard signing)
- https://a2a-protocol.org/latest/topics/enterprise-ready/

LangGraph / LangChain:
- https://docs.langchain.com/oss/python/langchain/multi-agent
- https://docs.langchain.com/oss/python/langgraph/graph-api
- https://docs.langchain.com/oss/python/langgraph/interrupts

AutoGen (AgentChat 0.7.x stable):
- https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/swarm.html
- https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/human-in-the-loop.html
- https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/termination.html
- https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/teams.html
- https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/framework/telemetry.html

OpenAI Agents SDK (Python):
- https://openai.github.io/openai-agents-python/handoffs/
- https://openai.github.io/openai-agents-python/tracing/
- https://openai.github.io/openai-agents-python/running_agents/
- https://openai.github.io/openai-agents-python/guardrails/
- https://openai.github.io/openai-agents-python/human_in_the_loop/
- https://openai.github.io/openai-agents-python/config/

## Method

1. Fetched each page with prompts asking for verbatim quotations (RFC-2119 keywords preserved) relevant to all five conditions, plus explicit "not mentioned" statements for absent topics.
2. Coded cells in the prescribed randomized order, applying the 3-level rubric:
   - satisfied only for mandatory MUST-level, chain-wide (multi-hop) mechanisms;
   - partial for optional/SHOULD-level, default-on-but-disableable, single-hop-only, or application-configuration-achievable mechanisms;
   - absent when no relevant provision was found (search recorded in quote_or_search).
3. For frameworks, judged guarantees (mandatory, always-on) rather than what an application could build; default-on-but-disableable mechanisms (OpenAI tracing, AutoGen OTel, LangGraph recursion_limit, OpenAI max_turns) were coded partial per rubric.

## Key interpretive decisions

- MCP-C1 partial, not satisfied: audience binding and the token-passthrough prohibition are MUST-level at every hop, but downstream hops obtain independent OAuth grants whose scopes are not derived from or bounded by the upstream grant; least privilege is SHOULD; authorization overall is OPTIONAL for MCP implementations.
- MCP-C2 partial: user-consent principles use lowercase "must" (outside BCP-14 capitalization), the spec states it "cannot enforce these security principles at the protocol level," and obligations bind the host-user hop only.
- Framework C1 cells partial rather than absent: per-agent tool assignment makes subset scopes achievable by application-level configuration (rubric's partial band), though no framework enforces a subset relation to the delegator.
- A2A-C2 and A2A-C5 absent: two spec passes plus the enterprise-ready page yielded no human-anchor or depth-limit provisions; ROLE_USER marks message direction only.
- No cell reached "satisfied": no artifact provides a mandatory, chain-wide mechanism for any condition.

## Tally

satisfied: 0; partial: 20; absent: 5 (MCP-C3, MCP-C4, MCP-C5, A2A-C2, A2A-C5).

## Limitations

Pages were fetched through a summarizing fetch tool; quotes are as returned by targeted extraction prompts against the live pages. The A2A specification is large, so it was queried in two targeted passes; absence claims for A2A reflect those passes plus the enterprise-ready page.
