# Interview Preparation

My single, long-term knowledge base for technical interview preparation — DSA, core CS fundamentals, and system design. Built to be revisited months or years from now, not just for the next interview.

**Background:** 4+ years as a Python backend / GenAI engineer (Django, REST APIs, AWS Bedrock, RAG systems). Learning DSA from the ground up — following the [Apna College](https://www.apnacollege.co/) DSA course in C++, then reimplementing every concept in Python, since Python is my primary/target language.

## How this repo is organized

- **`dsa/`** and **`interview-questions/`** — allowed to contain only `README.md` files; code lives in fenced blocks (C++ first, Python second) inside them.
- **`c++/`** and **`python/`** — the only folders allowed to hold real source files (`.cpp`, `.py`) alongside their own `README.md`.
- Every other folder (`oop/`, `dbms/`, `sql/`, `operating-systems/`, `computer-networks/`, `system-design/`, `software-engineering/`, `behavioral-interview/`, `resources/`) — concept notes in Markdown, code in fenced blocks where relevant.
- **`progress/`** — `leetcode-log.md` (chronological problem log) and `study-log.md` (tracks progress against the monthly roadmap below).
- **`CV/`** — resume + notes, gitignored, never pushed to GitHub. Local only.

## Navigation

| Section | Purpose |
|---|---|
| [`dsa/`](dsa/README.md) | Data structures & algorithms, organized by topic/pattern |
| [`c++/`](c++/README.md) | C++ fundamentals, STL, memory management |
| [`python/`](python/README.md) | Python fundamentals, data structures, OOP, stdlib |
| [`oop/`](oop/README.md) | OOP principles, SOLID, design patterns |
| [`dbms/`](dbms/README.md) | Database fundamentals, normalization, transactions |
| [`sql/`](sql/README.md) | Query writing, joins, window functions |
| [`operating-systems/`](operating-systems/README.md) | Processes, threads, scheduling, memory |
| [`computer-networks/`](computer-networks/README.md) | OSI/TCP-IP, HTTP, DNS, REST |
| [`system-design/`](system-design/README.md) | Scalability, caching, CAP theorem, real-world design |
| [`software-engineering/`](software-engineering/README.md) | SDLC, testing, CI/CD, Agile practices |
| [`behavioral-interview/`](behavioral-interview/README.md) | STAR framework, common behavioral questions |
| [`interview-questions/`](interview-questions/README.md) | Categorized Q&A across all topics |
| [`progress/`](progress/README.md) | LeetCode log and study tracking |
| [`resources/`](resources/README.md) | Courses, books, links worth keeping |

## Roadmap (6 months: Sep 2026 – Feb 2027)

Full plan lives in the [6-Month Roadmap artifact](https://claude.ai/code/artifact/959eddcb-8b51-4b87-a6c7-bdaa17ca66f6). DSA track summary:

| Month | Focus | LeetCode target |
|---|---|---|
| 1 (Sep '26) | Python/C++ basics, arrays & strings | 15 |
| 2 (Oct '26) | Patterns, hashing, recursion | 30 |
| 3 (Nov '26) | Linked list, stack, queue, trees | 50 |
| 4 (Dec '26) | Trees deep-dive, backtracking | 75 |
| 5 (Jan '27) | Graphs, DP | 100 |
| 6 (Feb '27) | Advanced topics, revision, interview prep | 120+ |

## Study order (recommended)

1. Complexity analysis → Arrays → Strings → Hashing
2. Recursion → Sorting → Searching
3. Two pointers / Sliding window / Prefix sum
4. Linked List → Stack → Queue
5. Trees → BST → Heaps
6. Backtracking → Graphs
7. Greedy → Dynamic Programming
8. Bit Manipulation
9. Fill in CS fundamentals (OOP, DBMS, OS, CN, SQL, System Design) in parallel once DSA basics are solid
10. Interview questions + behavioral prep in the final month

## Checklist before an interview

- [ ] Comfortable explaining time/space complexity of every solution
- [ ] Solved problems across all major DSA patterns, not just one topic
- [ ] Can explain 2–3 projects from experience in STAR format
- [ ] Reviewed core CS fundamentals relevant to the role
- [ ] Practiced at least one mock system design round

## Progress tracking

See [`progress/study-log.md`](progress/study-log.md) for monthly check-ins and [`progress/leetcode-log.md`](progress/leetcode-log.md) for the problem-by-problem log.
