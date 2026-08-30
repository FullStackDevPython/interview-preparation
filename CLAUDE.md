# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A personal, long-term interview-preparation knowledge base — not a software project. There is no build, lint, or test tooling; content is Markdown notes plus a small amount of reference source code. Treat contributions as writing a handbook, not shipping features.

The original brief that defines this repo's design is `Claude Prompt — Interview Preparation Repository.md` at the root — read it before making structural changes.

## Core file-placement rule

This is the one rule that must never be violated when adding content:

- **`dsa/` and every topic folder except `c++/` and `python/`**: README-only. Never create `.cpp`, `.py`, `.sql`, etc. files here. All code goes inside the topic's `README.md` as fenced code blocks.
- **`c++/` and `python/`**: the only folders allowed to hold real source files (`.cpp`, `.py`) alongside their own `README.md`.
- **DSA code examples show both languages**: C++ first (matches the user's Apna College tutorial and general interview convention), Python second (the user's primary/target language, since they reimplement every C++ concept they learn in Python). Don't drop to C++-only or Python-only for DSA content.

## DSA README template

Every `dsa/<topic>/README.md` follows this structure — keep new topic READMEs consistent with it:

1. Topic Overview (what/why/where used/what interviewers test)
2. Core Concepts
3. Important Patterns / Techniques
4. Important Algorithms (idea → steps → example → time/space complexity → when to use)
5. Code Examples (C++ then Python)
6. Common Interview Problems (curated table: name | pattern | difficulty | link — not a dump of every LeetCode problem)
7. Common Mistakes
8. Interview Tips
9. Quick Revision (bullet summary)

## Naming and organization

- All folders/files: lowercase, kebab-case (`binary-search-tree/`, not `BST/`).
- Don't duplicate explanations across topics — link to the canonical topic instead.
- Split a topic into subtopics only when its README becomes hard to navigate; don't pre-split.
- `progress/leetcode-log.md` is the raw chronological problem log; `dsa/<topic>/README.md`'s "Common Interview Problems" section stays curated and pattern-focused — don't conflate the two.

## Git conventions

- Trunk-based: commit directly to `master` for normal content additions. Only branch for large structural reorgs (e.g. changing the README template repo-wide), then merge and delete the branch.
- **Do not add `Co-Authored-By: Claude` or `Claude-Session:` trailers to commits in this repo.** The user wants every commit to show only themself as author/contributor on GitHub, since this repo is public and viewed by recruiters.

## CV/ folder

`CV/` is git-ignored and must stay that way — it holds the user's resume drafts and is never pushed to GitHub. Don't remove it from `.gitignore`.

## Roadmap context

Content should track the user's 6-month DSA/GenAI/MBA roadmap (Sep 2026–Feb 2027), summarized in the root `README.md`. When asked to add DSA content, check which month/topic is current before assuming scope.
