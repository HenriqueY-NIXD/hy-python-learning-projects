# Class Grade Calculator

> A command-line program that records students' grades and reports who passed, who needs a make-up exam and who failed.

| Status | Python | Started | Last updated | Tags |
|---|---|---|---|---|
| 💡 Idea <!-- 💡 Idea · 🟡 In progress · 🟢 Working · 🔵 Done · ⏸️ Paused · 🔴 Abandoned --> | 3.12 | 2026-11-25 | 2026-11-25 | `cli` `functions` `exercise` |

---

## 💡 The Idea

**Problem:** A teacher wants to record the grades of the students in a class and see, from the terminal, who passed, who needs a make-up exam and who failed.

### Data structure

```python
class_grades = {
    "Ana": [8.5, 7.0, 9.0],
    "Bruno": [6.0, 6.0],
}
```

### Features

- [ ] adds a student with an empty grade list. Raises `ValueError` if the name already exists.
- [ ] accepts only grades from 0 to 10 and only for students that exist. Raises `ValueError` in both error cases.
- [ ] returns the arithmetic mean of a list of grades, or `0.0` if the list is empty.
- [ ] returns a string based on the average:
  - average ≥ 7.0 → `"Passed"`
  - 5.0 ≤ average < 7.0 → `"Make-up exam"`
  - average < 5.0 → `"Failed"`
- [ ] average of all the students' averages.
- [ ] list of `(name, average)` tuples sorted from highest to lowest average.
- [ ] **Extra — Weighted average:** allow each grade to have a weight (e.g. exam weight 2, assignment weight 1).
- [ ] **Extra — CLI arguments:** accept direct commands with `argparse`, such as `python main.py report` or `python main.py grade Ana 8.5`.
- [ ] **Extra — Persistence:** save and load the class from a JSON file, so data survives between runs.

### Expected output

```text
Student name: Ana
✔ Student "Ana" added.

Student name: Ana
Grade: 8.5
✔ Grade 8.5 added for Ana.

Student name: Ana
Grade: 11
✘ Invalid grade: must be between 0 and 10.

--- Class report ---
1. Ana     | Average: 8.17 | Passed
2. Bruno   | Average: 6.00 | Make-up exam
3. Carla   | Average: 4.50 | Failed
Class average: 6.22
```

---

## 🚀 Getting Started

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# 2. Run
python main.py
```

---

## 📁 Project Structure

```text
class-grade-calculator/
├── main.py            # functions + main()
└── README.md
```

---

## 🔍 Observations

<!-- Key facts about the project's current state. -->


## 📝 Notes

<!-- Dev log: dated entries on lessons learned, problems and discoveries. Newest first. -->

### 2026-11-25
- Project created. Requirements defined.

---

## 🔗 References


---

## 🔙 Navigation

[⬅️ Back to hub](../README.md)