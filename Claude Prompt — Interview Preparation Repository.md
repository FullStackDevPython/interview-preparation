I want you to help me design and build a long-term GitHub repository that will serve as my **single Interview Preparation Knowledge Base**.

The repository should be named:

`interview-preparation`

The purpose of this repository is to keep everything I may need for technical interviews and future job preparation in one place. It should not be limited to DSA. I want to continuously expand it over time and be able to reference it from anywhere through GitHub.

## Core Philosophy

Treat this repository as a **personal interview-preparation handbook**, not simply a collection of coding problems.

The content should be:

- Easy to understand
- Well structured
- Beginner-friendly but technically accurate
- Useful for revision before interviews
- Suitable for repeated reference months or years later
- Written in clear Markdown
- Practical rather than unnecessarily theoretical
- Organized consistently across topics
- Easy to navigate from GitHub

Avoid creating unnecessary files or overengineering the repository.

---

# Repository Structure

Use the following high-level structure:

```text
interview-preparation/
│
├── README.md
│
├── dsa/
├── c++/
├── python/
├── oop/
├── dbms/
├── operating-systems/
├── computer-networks/
├── system-design/
├── software-engineering/
├── sql/
├── behavioral-interview/
├── interview-questions/
└── resources/
```

You may recommend additional high-value categories if they are genuinely useful for software/technical interviews, but do not add categories merely for the sake of having more folders.

---

# IMPORTANT FILE RULE

There is one important repository rule:

### C++ and Python

The `c++/` and `python/` folders are allowed to contain actual source-code files.

For example:

```text
c++/
├── README.md
├── basics/
│   ├── README.md
│   └── examples.cpp
└── STL/
    ├── README.md
    └── examples.cpp
```

and similarly for Python.

### Every other category

For every category other than `c++/` and `python/`, use **README.md files for the topics**.

Do NOT create separate `.cpp`, `.py`, `.java`, `.sql`, `.txt`, etc. files merely to demonstrate code.

Instead, put code examples directly inside the relevant README using fenced Markdown code blocks.

For example:

```text
dsa/
└── arrays/
    └── README.md
```

The README can contain:

```cpp
// C++ example
...
```

and:

```python
# Python example
...
```

when appropriate.

The purpose is to keep the repository clean and GitHub-friendly.

---

# DSA SECTION

The `dsa/` section is one of the most important parts of the repository.

Organize DSA into logical topics rather than randomly creating files for individual problems.

A good initial structure would be:

```text
dsa/
├── README.md
├── arrays/
│   └── README.md
├── strings/
│   └── README.md
├── hashing/
│   └── README.md
├── linked-list/
│   └── README.md
├── stack/
│   └── README.md
├── queue/
│   └── README.md
├── trees/
│   └── README.md
├── binary-search-tree/
│   └── README.md
├── heaps/
│   └── README.md
├── graphs/
│   └── README.md
├── recursion/
│   └── README.md
├── backtracking/
│   └── README.md
├── sorting/
│   └── README.md
├── searching/
│   └── README.md
├── greedy/
│   └── README.md
├── dynamic-programming/
│   └── README.md
├── bit-manipulation/
│   └── README.md
├── sliding-window/
│   └── README.md
├── two-pointers/
│   └── README.md
├── prefix-sum/
│   └── README.md
└── complexity-analysis/
    └── README.md
```

You can modify this structure if there is a better industry-standard organization.

---

# DSA README FORMAT

Every DSA topic README should follow a consistent structure.

Use this general format:

## 1. Topic Overview

Explain:

- What the topic is
- Why it matters
- Where it is used
- What interviewers commonly test

## 2. Core Concepts

Explain the important concepts in simple language.

## 3. Important Patterns / Techniques

List the major problem-solving patterns associated with the topic.

For example, for arrays:

- Two pointers
- Sliding window
- Prefix sum
- Kadane's algorithm
- Binary search
- Sorting-based approaches

## 4. Important Algorithms

Explain each important algorithm clearly.

For every algorithm include:

- Idea
- Step-by-step explanation
- Example
- Time complexity
- Space complexity
- When to use it

## 5. Code Examples

Include clean, interview-ready code inside the README.

Prefer C++ for DSA unless there is a strong reason to include Python as well.

Code should be:

- Clean
- Readable
- Correct
- Efficient
- Interview-friendly

## 6. Common Interview Problems

Maintain a list of representative problems.

For each problem include:

- Problem name
- Main concept/pattern
- Difficulty
- Short explanation
- Solution/code where appropriate
- Time complexity
- Space complexity

Do not blindly dump hundreds of LeetCode problems.

Prioritize problems that teach reusable patterns.

## 7. Common Mistakes

Mention mistakes candidates commonly make.

## 8. Interview Tips

Add practical interview tips where relevant.

## 9. Quick Revision

End each major README with a concise revision section containing the most important points.

---

# CODE QUALITY

All code should follow these principles:

- Prefer readable code over clever code.
- Use meaningful variable names.
- Avoid unnecessarily complicated syntax.
- Explain non-obvious logic.
- Always mention time and space complexity.
- Prefer optimal solutions where appropriate.
- If a brute-force solution is useful for understanding, explain it before the optimized solution.
- Do not present an optimized solution without explaining the intuition behind it.

For DSA, use **C++ as the primary interview language** unless otherwise specified.

Python examples can be included when they add value.

---

# OTHER TECHNICAL SECTIONS

The repository should eventually cover topics such as:

### C++

Language fundamentals, STL, memory management, pointers, references, classes, templates, modern C++, common interview questions, etc.

### Python

Python fundamentals, data structures, OOP, commonly used libraries/features, interview concepts, etc.

### OOP

Cover:

- Classes and objects
- Encapsulation
- Abstraction
- Inheritance
- Polymorphism
- SOLID principles
- Composition vs inheritance
- Common interview questions
- Practical examples

### DBMS

Cover:

- Database fundamentals
- Keys
- Normalization
- Transactions
- ACID
- Indexing
- Joins
- Transactions
- Concurrency
- Isolation levels
- Common interview questions

### SQL

Cover:

- SELECT
- WHERE
- GROUP BY
- HAVING
- ORDER BY
- JOINs
- Subqueries
- CTEs
- Window functions
- Aggregations
- Common interview queries

### Operating Systems

Cover:

- Processes
- Threads
- Scheduling
- Deadlocks
- Memory management
- Virtual memory
- Paging
- Synchronization
- File systems
- Common interview questions

### Computer Networks

Cover:

- OSI model
- TCP/IP
- TCP vs UDP
- HTTP/HTTPS
- DNS
- IP addressing
- Routing
- Cookies/sessions
- REST
- Common interview questions

### System Design

Cover:

- Scalability
- Availability
- Reliability
- Load balancing
- Caching
- Databases
- Message queues
- CAP theorem
- Sharding
- Replication
- Microservices
- API design
- Authentication/authorization
- Real-world system design examples

### Behavioral Interview

Include:

- Common behavioral questions
- STAR framework
- Leadership questions
- Conflict questions
- Failure questions
- Strengths/weaknesses
- Project discussion
- Resume-based questions

### Interview Questions

Maintain categorized interview questions for:

- DSA
- C++
- Python
- OOP
- DBMS
- SQL
- OS
- CN
- System Design
- Behavioral

---

# ROOT README

The root `README.md` should act as the homepage of the entire repository.

It should contain:

- Repository purpose
- Navigation to every major section
- Learning roadmap
- Recommended study order
- Quick links
- Interview preparation checklist
- Important resources
- Progress tracking section

Make the navigation easy to use on GitHub.

---

# ORGANIZATION PRINCIPLES

Follow these rules throughout the repository:

1. Do not duplicate information unnecessarily.
2. Link to another topic when the concept is already explained elsewhere.
3. Keep terminology consistent.
4. Use the same README structure across similar topics.
5. Use tables where they genuinely improve comparison or revision.
6. Use diagrams using Markdown/Mermaid only when they improve understanding.
7. Do not make README files unnecessarily huge.
8. Split topics into subtopics when a README becomes difficult to navigate.
9. Prefer depth and quality over quantity.
10. Never add content just to make the repository look large.

---

# LONG-TERM USAGE

This repository is intended to grow over multiple years.

Therefore, design it so that I can later add:

- New DSA patterns
- New interview questions
- Company-specific interview experiences
- New system design concepts
- New technologies
- Resume/project questions
- Important CS fundamentals
- Personal notes
- Revision checklists

without having to restructure the repository.

---

# YOUR TASK

First, analyze this requirement and propose the **best final repository architecture**.

Do not immediately generate hundreds of README files.

Instead:

1. Review the proposed architecture.
2. Improve it where necessary.
3. Explain why you made the changes.
4. Provide the final folder structure.
5. Define the README template that should be used for topics.
6. Define the naming conventions.
7. Define the rules for code placement.
8. Define how DSA problems should be organized.
9. Define a recommended learning roadmap.

After I approve the architecture, we will build the repository section by section.

The goal is to create a **clean, professional, long-term GitHub repository that I can use as my single source of truth for interview preparation.**