# Software design and engineering study materials

A collection of Python examples, notebooks and presentations covering design patterns, architecture patterns, SOLID principles and test-driven development. These are study materials, not one deployed application.

## Contents

| Folder | Topics and files |
| --- | --- |
| `software design pattern/` | Factory, Singleton, Chain of Responsibility, Adapter and Decorator examples; presentation |
| `architecture pattern/` | MVC, MVP and MVVM-style examples; supporting document |
| `SOLID Principles/` | Principle-by-principle notebook, example code before/after changes, presentation |
| `Test Driven/` | Small TDD notebook, presentation and supporting image |
| `notebooks/` | Separate YOLOv12 training notebook, outside the main software-design topics |

## Use the examples

Clone the repository and open individual `.py` files or notebooks in the relevant folder. Start with the companion presentation or document for context.

```bash
git clone https://github.com/yousefshehab1/software_section_task.git
cd software_section_task
pip install jupyter
jupyter notebook
```

This is not a single installable package. Requirements vary by example. The YOLO notebook has a separate computer-vision environment and external dataset workflow; do not run it as part of the basic design-pattern examples or paste API keys into source cells.

## Scope and attribution

The repository includes team-name material and multiple teaching examples. It should be presented as a study collection, not as proof that one person authored every example or built a production system. Preserve any credits in the slides and documents when reusing material.

No automated test-suite coverage, production deployment, training result or benchmark is claimed by this README. Source examples and file structure were inspected for this documentation update; the notebooks and slide demonstrations were not executed.
