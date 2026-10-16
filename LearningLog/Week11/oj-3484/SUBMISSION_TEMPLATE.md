# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3484
```

OJ submission ID, if submitted:

```text
683909
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```text
1-3 hours
```

Choose one:

```text
0-15 minutes
15-30 minutes
30-60 minutes
1-3 hours
3-6 hours
6-24 hours
1-3 days
4-7 days
1-4 weeks
More than 4 weeks
```

How to count this time:

- Count only the time you actively worked on this problem independently.
- Start counting from when you first read the problem.
- Do not include breaks, meals, classes, sleep, time spent on other problems, or time when you were not working on this problem.
- If you used AI, count only the independent time before your first AI prompt.
- If you asked a friend, TA, or instructor for help, count only the independent time before your first help request.
- If you used both AI and human help, count only the independent time before the first outside help of any kind.
- If you did not use AI or human help, count the time before writing this `submission.md`.
- An estimate is acceptable, but it must be honest.

---

## 2. My Understanding

Write the problem in your own words.

Also explain the input, output, and important constraints.

If you do not fully understand the problem yet, write what you currently understand. Your understanding may be incomplete or incorrect, but you must make a genuine attempt.

```text
โจทย์ต้องการให้สร้างโปรแกรมวิเคราะห์ผลการตรวจสอบกระเบื้องในพื้นที่ตารางขนาด n*n โดยรับค่าขนาดตาราง, ค่าปรับต่อจุดที่ชำรุด, และข้อมูลจำนวนจุดที่พบเสียงผิดปกติของกระเบื้องแต่ละแผ่น (0–5 จุด) จากนั้นให้โปรแกรมสรุปจำนวนกระเบื้องที่ชำรุด (แผ่นที่มีจุดเสียมากกว่า 0) และผลรวมจุดที่ชำรุดแยกตามรายแถวและรายคอลัมน์ พร้อมทั้งคำนวณจำนวนกระเบื้องที่ชำรุดทั้งหมด จำนวนจุดที่ชำรุดรวมทั้งหมด และคิดเป็นเงินค่าปรับรวมทั้งสิ้นกี่บาท (แสดงทศนิยม 2 ตำแหน่ง)
```

---

## 3. My First Plan

Write your first plan before getting help from AI, a friend, a TA, an instructor, or before finalizing your code.

If you used AI, write the plan you had before your first AI prompt.

If you asked a friend, TA, or instructor for help, write the plan you had before asking for help.

If you did not use AI or human help, write the plan you had before or while you started coding.

This can be rough. It may be incomplete or different from your final solution.

You may write pseudocode, a flowchart idea, or step-by-step thinking.
```text
Step 1: รับ input บรรทัดแรกแยกเป็นขนาดพื้นที่ n (จำนวนเต็ม) และค่าปรับต่อจุด p (ทศนิยม) จากนั้นรับข้อมูลจุดที่ไม่สมบูรณ์ทั้ง n แถว เก็บไว้ใน list 2 มิติ grid
Step 2: วนลูปทีละแถวใน grid เพื่อคำนวณหาจำนวนกระเบื้องที่มีปัญหาในแถวนั้น (นับเฉพาะช่องที่มีค่ามากกว่า 0) และผลรวมจุดที่มีปัญหาในแถวนั้น (sum(row)) พร้อมบวกสะสมเข้าตัวแปรรวมทั้งหมด (total_tiles, total_spots) แล้ว output ข้อมูลของแถวนั้นตามด้วยค่าทั้งสองออกมา
Step 3: คำนวณหาจำนวนกระเบื้องที่มีปัญหาและผลรวมจุดที่มีปัญหาแบบแยกตามคอลัมน์ (ตั้งแต่คอลัมน์แรกถึงคอลัมน์ที่ n) เก็บไว้ใน col_tiles และ col_spots
Step 4: output ค่า col_tiles ในบรรทัดที่ N+1 และค่า col_spots ในบรรทัดที่ N+2 โดยคั่นแต่ละค่าด้วยช่องว่าง
Step 5: output จำนวนกระเบื้องที่มีปัญหาทั้งหมด (total_tiles), จำนวนจุดที่มีปัญหาทั้งหมด (total_spots), และค่าปรับรวม (total_spots * p จัดทศนิยม 2 ตำแหน่ง) ในบรรทัดสุดท้าย
```
---
## 4. My Final Approach

Briefly explain the final algorithm or method you actually used in your submitted code.

This section is different from Section 3:

- Section 3 is your first plan before AI, human help, or before the final code.
- Section 4 is the final method used in your actual solution.
- If your final approach is the same as your first plan, write that it is the same and briefly explain why.

Do not copy AI's explanation.

Do not copy another person's explanation.

```text
เหมือนกับ first plan ไม่มีไรเปลี่ยน
```

---

## 5. My Tests

Write at least 3 test cases that you tried or designed by yourself.

Try to choose test cases that are different from each other.

For each test case, explain why you chose it.

If the input or output has many lines, write them inside the text blocks.

### Test Case 1

Why I chose this case:

```text
test ตามโจทย์
```

Input:

```text
6 500
0 4 3 0 1 0
0 5 2 0 1 0
0 1 0 0 0 0
4 0 0 0 0 0
5 1 0 1 0 0
0 0 0 2 0 0
```

Expected output:

```text
0 4 3 0 1 0 3 8
0 5 2 0 1 0 3 8
0 1 0 0 0 0 1 1
4 0 0 0 0 0 1 4
5 1 0 1 0 0 3 7
0 0 0 2 0 0 1 2
2 4 2 2 2 0
9 11 5 3 2 0
12 30 15000.00
```

Actual output:

```text
0 4 3 0 1 0 3 8
0 5 2 0 1 0 3 8
0 1 0 0 0 0 1 1
4 0 0 0 0 0 1 4
5 1 0 1 0 0 3 7
0 0 0 2 0 0 1 2
2 4 2 2 2 0
9 11 5 3 2 0
12 30 15000.00
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
test ค่าตามโจทย์
```

Input:

```text
3 100
0 0 0
0 0 0
0 0 0
```

Expected output:

```text
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0
0 0 0
0 0 0.00
```

Actual output:

```text
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0
0 0 0
0 0 0.00
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
test อื่นๆ
```

Input:

```text
4 100
0 0 2 0
0 4 0 0
0 0 0 0
0 0 0 0
```

Expected output:

```text
0 0 2 0 1 2
0 4 0 0 1 4
0 0 0 0 0 0
0 0 0 0 0 0
0 1 1 0
0 4 2 0
2 6 600.00
```

Actual output:

```text
0 0 2 0 1 2
0 4 0 0 1 4
0 0 0 0 0 0
0 0 0 0 0 0
0 1 1 0
0 4 2 0
2 6 600.00
```

Result:

```text
Pass
```

---

## 6. AI Use

Did you use AI for this problem?

```text
No
```

If yes, also complete:

```text
ai_reflection.md
```

If you only asked a friend, TA, or instructor and did not use AI, you do not need to complete `ai_reflection.md`.

---

## 7. Human Help / Collaboration

Did you ask a friend, TA, instructor, or another person for help on this problem?

```text
No
```

If yes, briefly explain what kind of help you received.

Allowed examples:

- explanation of the problem statement
- explanation of a programming concept
- hint about the approach
- debugging discussion
- test-case discussion
- help understanding an error message

Not allowed:

- copying another person's code
- submitting another person's solution
- asking another person to write the solution for you
- using another person's OJ submission
- asking another person to submit to the OJ for you

Who helped you?

```text

```

What did they help with?

```text

```

What did you still do by yourself?

```text

```

Did you copy any code from another person?

```text
No
```

---

## 8. Student Declaration

Write `Yes` for each statement.

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | Yes |
| I understand my final code. | Yes |
| I recorded the real OJ status. | Yes |
| I did not copy AI-generated text directly into this file. | Yes |
| I did not copy code from another person. | Yes |
| If I received human help, I disclosed it in this file. | Yes |
| I submitted the final code to the OJ by myself. | Yes |