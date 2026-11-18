# L03 · Modular Programming

<div dir="rtl" align="right">

**الفكرة:** بدل ملف واحد كبير، بنقسّم البرنامج لـ **modules**: كل module ملف ليه شغلانة (الحسابات، المخزن)، فيه الـ procedures بتاعته وبياناته. والـ main program (`shop.py`) بيستخدمهم بـ `import` وبيستدعي بالاسم الكامل: `billing.make_bill(...)`، `stock.report()`‎.
**الـ namespace:** كل module ليه namespace خاص بيه، فنفس الاسم `report` يتكتب في الملفين من غير تصادم.
**خلي بالك:** `from billing import *`‎ بيجيب أغلب أسماء الـ module مباشرة في `shop.py`، فممكن اسم يغطي على اسم، وترجع مشكلة الدرس اللي فات.

</div>

**Idea:** instead of one big file, split the program into **modules**: each module is a file with one job (billing, stock), holding its procedures and its data. The main program (`shop.py`) imports them and calls by full name: `billing.make_bill(...)`, `stock.report()`.
**Namespace:** each module has its own namespace, so the same name `report` can live in both files without a clash.
**Watch out:** `from billing import *` puts most of the module's names straight into `shop.py`; one name can hide another and the name clash of the last lesson comes back.

## How to run

Open a terminal **inside the example's folder** (the modules must sit next to `shop.py`) and run `python shop.py` on Windows, or `python3 shop.py` on macOS/Linux (Python 3.13).
In this lesson, do **not** add `-I` (used in Lesson 2): `-I` stops Python from finding `billing.py` and `stock.py` in the same folder, and you get `ModuleNotFoundError`.

<div dir="rtl" align="right">‏شغّل الأمر من جوه فولدر المثال نفسه: <code>python shop.py</code> على Windows، أو <code>python3 shop.py</code> على macOS/Linux. في الدرس ده من غير ‎<code>-I</code>، لأنها بتمنع Python إنه يلاقي الـ modules اللي جنب <code>shop.py</code>.‏</div>

## Files

| Folder | What it shows | <div dir="rtl" align="right">‏بيوضّح إيه‏</div> |
|---|---|---|
| `examples/01_modules/` | `billing.py` + `stock.py` + `shop.py`: two `report()` functions, no clash | <div dir="rtl" align="right">‏ملفين فيهم report، من غير تصادم‏</div> |
| `examples/02_import_star_mistake/` | Common mistake: `from … import *` → `TypeError` | <div dir="rtl" align="right">‏الخطأ الشائع: import star‏</div> |
| `examples/03_quiz_import_only/` | Lesson quiz: `import stock`, then `report()` with no dot: what happens? (no output file: the answer comes at the start of Lesson 4) | <div dir="rtl" align="right">‏سؤال الدرس: إيه اللي هيحصل؟ (من غير ملف output: الإجابة في أول الدرس الرابع)‏</div> |
| `exercise/` | Exercise start (= `01_modules`); `shop.output.txt` is the output **before** your change | <div dir="rtl" align="right">‏بداية التمرين (زي ‎01_modules)؛ و shop.output.txt هو الناتج قبل ما تعدّل‏</div> |
| `solution/` | Solution: new `menu.py` holds the price (35); `billing.py` reads `menu.price` | <div dir="rtl" align="right">‏الحل: menu.py فيه السعر (35)، و billing.py بياخده من menu.price‏</div> |
| `handout/L03_handout.pdf` | Lesson handout (AR + EN, 6 pages; no quiz answer) | <div dir="rtl" align="right">‏ملخص الدرس (PDF)‏</div> |

## Exercise

Make a third module `menu.py` and move the price into it. Let `billing.py` read it with `import menu` and `menu.price`. Change the price to **35** in `menu.py` only, then run `shop.py` from the same folder and compare with `solution/shop.output.txt`.

<div dir="rtl" align="right">‏اعمل module تالت اسمه menu.py، وانقل فيه السعر. خلّي billing.py ياخد السعر منه بـ import menu و menu.price. غيّر السعر لـ 35 في menu.py بس، وشغّل shop.py من نفس الفولدر، وقارن بـ solution/shop.output.txt.‏</div>

## Quiz (answer at the start of Lesson 4)

In `examples/03_quiz_import_only/shop.py` there is a line `import stock` on its own… and after it `report()` with no dot. What happens when you run it… and why? Answer first, then run the file.

<div dir="rtl" align="right">‏سؤال الدرس (الإجابة في أول الدرس الرابع): في <code>examples/03_quiz_import_only/shop.py</code>‎، سطر import stock لوحده… وبعده report من غير نقطة. إيه اللي هيحصل وقت التشغيل… وليه؟ جاوب الأول، وبعدين شغّل الملف.‏</div>

Each other folder has `shop.output.txt` with the real output (in tracebacks the folder path is shortened to `…`).

<div dir="rtl" align="right">‏الأسعار للتوضيح فقط.‏</div>

Prices are illustrative · Python 3.13 · 2026 · FILE VERSION 4 · 2026-11-17 (V4: code next to Arabic shown left-to-right, «most of the module's names», the Arabic quiz names its file; V3: handout PDF; V2: right-to-left Arabic blocks, run without `-I`, exercise steps, quiz output held back until Lesson 4; V1 2026-11-15)
