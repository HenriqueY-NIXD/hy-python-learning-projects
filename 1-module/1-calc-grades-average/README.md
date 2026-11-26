# Class Grade Calculator

> A command-line program that records students' grades and reports who passed, who needs a make-up exam and who failed.

| Status | Python | Started | Last updated |
|---|---|---|---|
| 💡 Idea | 3.12 | 2026-11-25 | 2026-11-26 |

---

## 💡 The Idea

**Problem:** A teacher wants to record the grades of the students in a class and see, from the terminal, who passed, who needs a make-up exam and who failed.

---

### Expected output


#### Selection screen
```text
Students 1/1

1 - Bruno
2 - Carla
3 - Marcelo

Type student or command (Type -h for manual): _
```

#### Help screen
```text
Student: -h
- Type a student by name or "ID:<id>" to select a student by ID
- Type ">" to next page 
- Type "<" to previous page 
- Type "!" to delete a student
- Type "?" to summarize grades
- Type "-h" for help manual

Type "exit" to leave manual: 
```

#### Creation
```text
Create student: ANA
Do you want to create student "ANA"? (Y/n)

✔ Student "ANA" added.
Type student or command (Type -h for manual): _
```

#### Deletion
```text
Delete student: ANA
Do you want to delete student "ANA"? (Y/n)

✔ Student "ANA" deleted.
Type student or command (Type -h for manual): _
```

#### Select student
```text
Type student or command (Type -h for manual): ANA

Select student "ANA"? (Y/n)

Student: ANA
Math: 0.0
English: 0.0

Average: 0.0

Do you want to change ANA's grade (Y/n)? _
```

#### Change student grade
```text
Do you want to change ANA's grade (Y/n)? Y

Math: 0.0 <-
English: 0.0
[ Save grades ]

Math: _
✘ Invalid grade: must be between 0 and 10.
Math: 10.0

Math: 10.0 
English: 0.0
[ Save grades ] <-
```

#### Summary
```text
--- Class report ---

1. ANA     | Average: 8.17 | Passed
2. BRUNO   | Average: 6.00 | Make-up exam
3. CARLA   | Average: 4.50 | Failed

Class average: 6.22
```

---

### Features

- [ ] student selection screen (max 10 students)
- [ ] help screen 
- [ ] student creation
- [ ] student deletion
- [ ] student selection
- [ ] student's grade change
- [ ] students summary
- [ ] **Extra — Persistence:** save and load the class from a JSON file, so data survives between runs.

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

- average ≥ 7.0 → `"Passed"`
- 5.0 ≤ average < 7.0 → `"Make-up exam"`
- average < 5.0 → `"Failed"`


## 📝 Logs

<!-- Dev log: dated entries on lessons learned, problems and discoveries. Newest first. -->

### 2026-11-25
- Project created.

### 2026-11-26
- Requirements defined.
---

## 🔗 References


---

## 🔙 Navigation

[⬅️ Back to hub](../README.md)