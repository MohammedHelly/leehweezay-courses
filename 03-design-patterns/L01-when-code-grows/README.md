# L01 · When the Code Grows · لما الكود يكبر

<div dir="rtl" align="right">

**الفكرة:** الـ polymorphism بطريقتين:
1. بالـ inheritance والـ override.
2. بالـ duck typing، يعني Python بتحكم على الـ object بسلوكه مش بنوعه.

</div>

**Idea:** polymorphism, done two ways:
1. with inheritance and override;
2. with duck typing: Python judges an object by its behaviour, not by its type.

| File | What it shows |
|---|---|
| `examples/01_if_elif_ladder.py` | The if/elif chain that breaks when a new vehicle is added (it raises an error on purpose) |
| `examples/02_polymorphism_inheritance.py` | Inheritance + override |
| `examples/03_duck_typing.py` | A bike with no base class still works |
| `examples/04_common_mistake.py` | Common mistake: `type()` vs `isinstance()` |
| `examples/05_protocol_runtime_check.py` | `typing.Protocol` with `@runtime_checkable` |
| `exercise/exercise_start.py` | Exercise |
| `solution/solution.py` | Solution |

Python 3.13 · 2026
