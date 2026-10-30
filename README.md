# LeehWeEzay Courses · كورسات ليه وإزاي

<div dir="rtl" align="right">

كود كورسات علوم الحاسب على قناة **ليه وإزاي** على يوتيوب.
الشرح بالعربي المصري، والمصطلحات التقنية بالإنجليزي.
كل مثال اتشغّل فعلًا على Python 3.13، والناتج الحقيقي محفوظ جنبه في ملف `.output.txt`.

</div>

Code for the computer-science courses on the **LeehWeEzay (ليه وإزاي)** YouTube channel.
The lessons are narrated in Egyptian Arabic, with technical terms in English.
Every example was actually run on Python 3.13, and its real output is saved next to it as `.output.txt`.

## Courses · الكورسات

| # | Course | الكورس | Status |
|---|---|---|---|
| 01 | [Why Programming Changed](01-programming/) | ليه البرمجة اتغيرت؟ | In production |
| 03 | [Design Patterns as a Story](03-design-patterns/) | الـ Design Patterns كحكاية | In production |
| 02 | [AI Agents with Python and MCP](02-ai-agents-mcp/) | إزاي تبني AI agent بـ Python و MCP | In production |

Recommended order: 01 → 03 → 02.

## How to run · طريقة التشغيل

```bash
python --version                        # 3.13 or newer
cd 01-programming/L01-unstructured/examples
python 02_opening_day.py
```

## Folder layout · ترتيب الفولدرات

```
<NN>-<course>/
  L<NN>-<topic>/
    README.md      lesson summary (AR + EN)
    examples/      NN_name.py + NN_name.output.txt
    exercise/      exercise_start.py
    solution/      solution.py
```

## License

Code: MIT (see `LICENSE`). Videos, slides and narration © Mohammed Helly, all rights reserved.
