# L02 · Procedural Programming (Part 1)

<div dir="rtl" align="right">

**الفكرة:** بدل ما ننسخ نفس الخطوات في كل مكان، بنكتبها **مرة واحدة** في **procedure** (في Python اسمها function) ليها اسم، وبنستدعيها بالاسم كل ما نحتاجها.
**الـ call والـ return:** لما نستدعي الـ function، التنفيذ بيدخل جواها، ولما تخلص بيرجع للسطر اللي بعد الاستدعاء. والـ function ممكن تاخد **parameters** وترجّع نتيجة بـ `return`.
**خلي بالك:** الـ `def` لوحدها بتعرّف الـ function بس… مافيش حاجة بتتنفذ غير لما نستدعيها.

</div>

**Idea:** instead of copying the same steps everywhere, write them **once** in a named **procedure** (a function in Python) and call it by name whenever it is needed.
**Call and return:** a call jumps into the function; when it finishes, execution returns to the line after the call. A function can take **parameters** and send a result back with `return`.
**Watch out:** `def` only defines the function. Nothing inside it runs until it is called.

| File | What it shows | بيوضّح إيه |
|---|---|---|
| `examples/01_call_return.py` | First procedure: call, then return to the caller | أول procedure: الاستدعاء والرجوع |
| `examples/02_parameter.py` | Parameter and argument: one function, different values | الـ parameter والـ argument: نفس الـ function بقيم مختلفة |
| `examples/03_return.py` | `return`: keep the result and use it | الـ return: نحتفظ بالنتيجة ونستخدمها |
| `examples/04_two_values.py` | One `return`, two values (a tuple) | return واحد بيرجّع قيمتين في tuple |
| `examples/05_quiz_add_fee.py` | Lesson quiz: what is printed, and in what order? | سؤال الدرس: إيه اللي هيتطبع وبأي ترتيب؟ |
| `examples/06_short_define_only.py` | Short: the function is defined but never called | الـ Short: الـ function اتعرّفت بس ما اتستدعتش |
| `examples/07_short_one_call.py` | Short: one more line, the call | الـ Short: سطر واحد زيادة، الاستدعاء |
| `exercise/exercise_start.py` | Exercise: write `stock_after(trays, stock)` for the sugar stock | التمرين: اكتب `stock_after` لمخزن السكر |
| `solution/solution.py` | Solution | الحل |

Try the quiz yourself before you run `05_quiz_add_fee.py` · جاوب على السؤال الأول قبل ما تشغّل الملف.

Part 2 of this lesson will be added here when it is released · الجزء التاني هيتضاف هنا لما ينزل.

Prices are illustrative · الأسعار للتوضيح فقط · Python 3.13 · 2026 · FILE VERSION 1 · 2026-11-11
