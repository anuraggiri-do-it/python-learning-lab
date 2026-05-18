ARC task utilities

- `1.py`: CLI helper to list and load ONNX models placed in `submission/`.
- `arc_solver.py`: solver scaffolding; implements `task001` as an example.
- `run_arc_task.py`: demo runner to exercise solvers.

Quick run (from the folder):

```bash
python -m virtualization.arc_tasks.run_arc_task task001
```

List available ONNX task models:

```bash
python -m virtualization.arc_tasks.run_arc_task --list
```

Or from this folder:

```bash
python run_arc_task.py task001
```
