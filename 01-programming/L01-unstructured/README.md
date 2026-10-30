# L01 · Unstructured Programming

<div dir="rtl" align="right">

**الفكرة:** البرنامج كله **main program** واحد، أوامره بتتنفذ بالترتيب من أول سطر لآخر سطر، وبتتعامل مباشرة مع **global data** متاحة لكل سطر في الملف.
**المشكلة:** لما نحتاج نفس مجموعة الأوامر في أكتر من مكان، بننسخها. ولو عدّلنا نسخة ونسينا التانية، البرنامج بيشتغل من غير أي رسالة خطأ… بس بنتيجة غلط.

</div>

**Idea:** the whole program is one main program. Its statements run in order, from the first line to the last, and they work directly on global data.
**Problem:** when the same group of statements is needed in several places, it gets copied. If one copy is updated and another is missed, the program still runs with no error, but the result is wrong.

| File | What it shows | بيوضّح إيه |
|---|---|---|
| `examples/01_global_variable.py` | One line writes a global variable, another reads it | سطر بيغيّر الـ global variable وسطر بيقراه |
| `examples/02_opening_day.py` | Three bills, the same three steps | تلات حسابات بنفس الخطوات |
| `examples/03_price_increase.py` | The price changes; the delivery copy is missed | السعر اتغيّر ونسخة التوصيل ماتعدّلتش |
| `examples/04_replace_all_mistake.py` | Common mistake: Replace All also changes the stock | خطأ شائع: الـ Replace All غيّر كمية الرز |
| `examples/05_review_each_match.py` | The right way: review each search match | الطريقة الصحيحة: Find Next ومراجعة كل نتيجة |
| `examples/06_price_in_a_variable.py` | One price variable, but the steps are still copied | السعر في variable واحد والخطوات لسه مكررة |
| `examples/07_no_goto_in_python.py` | Python has no `goto` | Python مافيهاش `goto` |
| `exercise/exercise_start.py` | Exercise: add a takeaway bill, change the price, count your edits | التمرين: أضف حساب سفري، غيّر السعر، وعدّ التعديلات |
| `solution/solution.py` | Solution | الحل |

Prices are illustrative · الأسعار للتوضيح فقط · Python 3.13 · 2026
