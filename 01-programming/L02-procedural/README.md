# L02 · Procedural Programming (Part 1 + Part 2)

<div dir="rtl" align="right">

**الفكرة:** بدل ما ننسخ نفس الخطوات في كل مكان، بنكتبها **مرة واحدة** في **procedure** (في Python اسمها function) ليها اسم، وبنستدعيها بالاسم كل ما نحتاجها.
**الـ call والـ return:** لما نستدعي الـ function، التنفيذ بيدخل جواها، ولما تخلص بيرجع للسطر اللي بعد الاستدعاء. والـ function ممكن تاخد **parameters** وترجّع نتيجة بـ `return`.
**خلي بالك:** الـ `def` لوحدها بتعرّف الـ function بس… مافيش حاجة بتتنفذ غير لما نستدعيها.
**الجزء التاني:** الحسابات التلاتة بقت procedure واحدة اسمها `make_bill`، وأي تعديل في الحساب بيتكتب مرة واحدة. والبرنامج كله بقى سلسلة calls بنقدر نرسمها كشجرة (call tree).

</div>

**Idea:** instead of copying the same steps everywhere, write them **once** in a named **procedure** (a function in Python) and call it by name whenever it is needed.
**Call and return:** a call jumps into the function; when it finishes, execution returns to the line after the call. A function can take **parameters** and send a result back with `return`.
**Watch out:** `def` only defines the function. Nothing inside it runs until it is called.
**Part 2:** the three bills become one procedure, `make_bill`; a change to the calculation is written once. The whole program becomes a sequence of calls you can draw as a call tree.

## Part 1

| File | What it shows | <div dir="rtl" align="right">‏بيوضّح إيه‏</div> |
|---|---|---|
| `examples/01_call_return.py` | First procedure: call, then return to the caller | <div dir="rtl" align="right">‏أول procedure: الاستدعاء والرجوع‏</div> |
| `examples/02_parameter.py` | Parameter and argument: one function, different values | <div dir="rtl" align="right">‏الـ parameter والـ argument: نفس الـ function بقيم مختلفة‏</div> |
| `examples/03_return.py` | `return`: keep the result and use it | <div dir="rtl" align="right">‏الـ return: نحتفظ بالنتيجة ونستخدمها‏</div> |
| `examples/04_two_values.py` | One `return`, two values (a tuple) | <div dir="rtl" align="right">‏return واحد بيرجّع قيمتين في tuple‏</div> |
| `examples/05_quiz_add_fee.py` | Lesson quiz: what is printed, and in what order? | <div dir="rtl" align="right">‏سؤال الدرس: إيه اللي هيتطبع وبأي ترتيب؟‏</div> |
| `examples/06_short_define_only.py` | Short: the function is defined but never called | <div dir="rtl" align="right">‏الـ Short: الـ function اتعرّفت بس ما اتستدعتش‏</div> |
| `examples/07_short_one_call.py` | Short: one more line, the call | <div dir="rtl" align="right">‏الـ Short: سطر واحد زيادة، الاستدعاء‏</div> |
| `exercise/exercise_start.py` | Exercise: write `stock_after(trays, stock)` for the sugar stock | <div dir="rtl" align="right">‏التمرين: اكتب `stock_after` لمخزن السكر‏</div> |
| `solution/solution.py` | Solution | <div dir="rtl" align="right">‏الحل‏</div> |

Try the quiz yourself before you run `05_quiz_add_fee.py`.

<div dir="rtl" align="right">‏جاوب على السؤال الأول قبل ما تشغّل الملف.‏</div>

## Part 2

| File | What it shows | <div dir="rtl" align="right">‏بيوضّح إيه‏</div> |
|---|---|---|
| `examples/08_make_bill.py` | The bill in one place: one procedure, three calls | <div dir="rtl" align="right">‏الحساب في مكان واحد: procedure واحدة وتلات calls‏</div> |
| `examples/09_discount.py` | A new discount rule written once, inside the function | <div dir="rtl" align="right">‏قاعدة خصم جديدة بتتكتب مرة واحدة جوه الـ function‏</div> |
| `examples/10_name_clash.py` | Common mistake: one name defined twice, no error | <div dir="rtl" align="right">‏خطأ شائع: نفس الاسم مرتين، ومفيش رسالة خطأ‏</div> |
| `examples/11_two_names.py` | Quick fix: one name per procedure | <div dir="rtl" align="right">‏الحل السريع: اسم مختلف لكل procedure‏</div> |
| `examples/12_short_same_name.py` | Short: the sales report disappeared… why? | <div dir="rtl" align="right">‏الـ Short: تقرير المبيعات اختفى… ليه؟‏</div> |
| `exercise/exercise_part2_start.py` | Exercise: add a party bill with ONE call, set the price to 35, count your edits | <div dir="rtl" align="right">‏التمرين: أضف حساب عزومة بـ call واحد، وغيّر السعر لـ 35، وعدّ الأسطر اللي عدّلتها‏</div> |
| `solution/solution_part2.py` | Solution: only 2 lines edited | <div dir="rtl" align="right">‏الحل: سطرين بس اتعدّلوا‏</div> |

Part 2 quiz (answer at the start of Lesson 3): in `08_make_bill.py`, when `print` finishes inside `make_bill`, where exactly does execution go?

<div dir="rtl" align="right">‏سؤال الجزء التاني (الإجابة في أول الدرس التالت): في <code>08_make_bill.py</code>، لما <code>print</code> تخلص جوه <code>make_bill</code>… التنفيذ بيرجع فين بالظبط؟‏</div>

Every `.py` file has its real output next to it in `.output.txt` (Python 3.13, `python3 -I`).

<div dir="rtl" align="right">‏الأسعار للتوضيح فقط.‏</div>

Prices are illustrative · Python 3.13 · 2026 · FILE VERSION 2 · 2026-11-16 (V1 2026-11-11: Part 1 only; git keeps V1)
