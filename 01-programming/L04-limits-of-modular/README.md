# L04 · The Limits of Modular Programming

<div dir="rtl" align="right">

**الفكرة:** الـ modules حلّت تصادم الأسماء، بس في البرامج الكبيرة ظهرت مشاكل أكبر. **قانون Brooks:** لو زوّدت ناس على مشروع متأخر، هيتأخر أكتر، لأن قنوات التواصل بتساوي <code>n * (n - 1) // 2</code>‎.

**المشكلة الأولى (البيانات):** كمية السكر بقت **global data**، فأي function تقدر تعدّلها، حتى لو مش مسؤولة عنها (<code>end_of_day</code> صفّرت المخزن من غير رسالة خطأ). ولو غيّرنا الـ data structure بتاعتها، لازم نعدّل كل function بتستخدمها.

**المشكلة التانية (العالم الحقيقي):** فرع الدقي مش موجود في الكود كحاجة واحدة.

**المشكلة التالتة (data types جديدة):** عملنا الفرع tuple، فبقينا نكتب <code>branch[1]</code>‎ ومحدش يعرف إن 1 يعني السكر، و Python بيقول إن نوعه tuple مش فرع.

</div>

**Idea:** modules fixed the name clash, but large programs show bigger problems. **Brooks's law:** adding people to a late project makes it later, because communication paths grow as `n * (n - 1) // 2`.

**Problem 1 (data):** the sugar stock is **global data**, so any function can change it, even one with no business there (`end_of_day` resets the stock with no error). Change its data structure and every function that uses it must change too.

**Problem 2 (the real world):** the Dokki branch does not exist in the code as one thing.

**Problem 3 (new data types):** a branch made as a tuple means writing `branch[1]`, and nothing says 1 is the sugar; Python says its type is tuple, not branch.

## How to run

Open a terminal **inside the example's folder** (the modules must sit next to `shop.py`) and run `python shop.py` on Windows, or `python3 shop.py` on macOS/Linux (Python 3.13). In `examples/01_team_paths/` the file is `team.py`. As in Lesson 3, do **not** add `-I`: it stops Python from finding `stock.py` and `reports.py` in the same folder.

<div dir="rtl" align="right">‏شغّل الأمر من جوه فولدر المثال نفسه: <code>python shop.py</code> على Windows، أو <code>python3 shop.py</code> على macOS/Linux. في <code>examples/01_team_paths/</code>‎ الملف اسمه <code>team.py</code>. ومن غير ‎<code>-I</code>، زي الدرس التالت.‏</div>

## Files

| Folder | What it shows | <div dir="rtl" align="right">‏بيوضّح إيه‏</div> |
|---|---|---|
| `examples/01_team_paths/` | `paths(n)` = `n * (n - 1) // 2` for teams of 2, 5, 10, 20 → 1, 10, 45, 190 | <div dir="rtl" align="right">‏قنوات التواصل في الفريق‏</div> |
| `examples/02_shared_data/` | `reports.end_of_day()` sets `stock.sugar_kg = 0`: 15 kg → 0 kg, no error | <div dir="rtl" align="right">‏function مش مسؤولة صفّرت المخزن‏</div> |
| `examples/03_layout_change/` | `sugar_kg` becomes a dict (one stock per branch) → `TypeError` in `use` | <div dir="rtl" align="right">‏الـ data structure اتغيّرت، فالـ functions اللي معتمدة عليها لازم تتغيّر‏</div> |
| `examples/04_no_global_mistake/` | Common mistake: no `global` line in `use` → `UnboundLocalError` | <div dir="rtl" align="right">‏الخطأ الشائع: من غير global‏</div> |
| `examples/05_global_everywhere_mistake/` | The "easy fix": `global` in every function; it runs, but `report` can now change the stock too | <div dir="rtl" align="right">‏الحل السهل الغلط: global في كل function‏</div> |
| `examples/06_branch_tuple/` | A branch as a tuple: `branch[0]`, `branch[1]`, a new tuple to use 5 kg, `type()` says tuple | <div dir="rtl" align="right">‏فرع من غير data type خاص بيه‏</div> |
| `exercise/` | Exercise start (= `02_shared_data`); `shop.output.txt` is the output **before** your change | <div dir="rtl" align="right">‏بداية التمرين (زي ‎02_shared_data)؛ و shop.output.txt هو الناتج قبل ما تعدّل‏</div> |
| `solution/` | Solution: sugar in grams; 5 code lines changed in 2 files (`stock.py`, `reports.py`; comments aside) | <div dir="rtl" align="right">‏الحل: السكر بالجرام؛ 5 سطور كود اتغيّرت في ملفين (من غير الـ comments)‏</div> |
| `handout/L04_handout.pdf` | Lesson handout (AR + EN; no quiz answer) | <div dir="rtl" align="right">‏ملخص الدرس (PDF)‏</div> |

Right way (Lesson 4): `global` only in the function whose job is to change the data (`use` in `examples/02_shared_data/stock.py`); `report` only reads. This is an agreement between programmers: any other file can still write `stock.sugar_kg`.

<div dir="rtl" align="right">‏الصح: global بس في الـ function اللي شغلانتها تغيّر البيانات (use)، والباقي يقرا بس. وده اتفاق بين المبرمجين، لأن أي ملف تاني لسه يقدر يكتب <code>stock.sugar_kg</code>‎.‏</div>

## Exercise

Start from the files in `exercise/`. Change sugar from kilograms to grams: `sugar_kg = 20` becomes `sugar_g = 20000`, and `use(kg)` still takes kg. Make the program run correctly, then count how many lines you changed and in how many files. Compare with `solution/shop.output.txt`.

<div dir="rtl" align="right">‏ابدأ من ملفات <code>exercise/</code>‎. غيّر وحدة السكر من كيلو لجرام: <code>sugar_kg = 20</code> تبقى <code>sugar_g = 20000</code>، و use لسه بتاخد kg. خلّي البرنامج يشتغل صح، وعدّ كام سطر غيّرت وفي كام ملف، وقارن بـ solution/shop.output.txt.‏</div>

## Quiz (answer at the start of Lesson 5)

A team has 4 programmers and we add 2. How many communication paths will there be, and how many were added? You can check with `paths(n)` in `examples/01_team_paths/team.py`. Answer in the video comments first.

<div dir="rtl" align="right">‏سؤال الدرس (الإجابة في أول الدرس الخامس): فريق فيه أربع مبرمجين، وزوّدنا عليه اتنين. قنوات التواصل هتبقى كام… وزادت كام؟ تقدر تتأكد بـ paths في <code>examples/01_team_paths/team.py</code>‎. اكتب إجابتك في التعليقات الأول.‏</div>

## Notes

`//` is integer division (floor division): `5 // 2` is `2`. Since `n * (n - 1)` is always even, `// 2` here gives the exact number.

<div dir="rtl" align="right">‏‎<code>//</code>‎ معناها قسمة صحيحة (integer division · floor division): ‎<code>5 // 2</code>‎ بتساوي 2. وبما إن ‎<code>n * (n - 1)</code>‎ دايمًا رقم زوجي، فالـ ‎<code>// 2</code>‎ هنا بتدّي الرقم بالظبط.‏</div>

Each folder has its `.output.txt` with the real output (in tracebacks the folder path is shortened to `…`).

Python 3.13 · 2026 · FILE VERSION 2 · 2026-11-21 (V2: Fable 5.2 review V1 fixes)
