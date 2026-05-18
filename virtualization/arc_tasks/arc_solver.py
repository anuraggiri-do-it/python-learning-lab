import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import onnxruntime as ort


ROOT = Path(__file__).parent
SUBMISSION_DIR = ROOT / 'submission'
EXPLANATIONS_PATH = ROOT / 'arc_explanations.json'
MODEL_CACHE: Dict[str, ort.InferenceSession] = {}


def load_explanations() -> dict:
    if not os.path.isfile(EXPLANATIONS_PATH):
        return {}
    with open(EXPLANATIONS_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


EXPLANATIONS = load_explanations()


def get_explanation(task_id: str) -> str:
    return EXPLANATIONS.get(task_id, '')


def task_model_path(task_id: str) -> Optional[Path]:
    candidate = SUBMISSION_DIR / f"{task_id}.onnx"
    if candidate.exists():
        return candidate

    normalized = task_id.lower().replace('.onnx', '')
    for path in SUBMISSION_DIR.glob('*.onnx'):
        if path.stem.lower() == normalized or normalized in path.stem.lower():
            return path
    return None


def load_task_model(task_id: str) -> Optional[ort.InferenceSession]:
    if task_id in MODEL_CACHE:
        return MODEL_CACHE[task_id]

    model_path = task_model_path(task_id)
    if model_path is None:
        return None

    session = ort.InferenceSession(str(model_path), providers=['CPUExecutionProvider'])
    MODEL_CACHE[task_id] = session
    return session


def encode_grid(grid: List[List[int]], channels: int = 10, height: int = 30, width: int = 30) -> np.ndarray:
    arr = np.zeros((1, channels, height, width), dtype=np.float32)
    if not grid or not grid[0]:
        return arr

    rows = len(grid)
    cols = len(grid[0])
    if rows > height or cols > width:
        raise ValueError(f"Grid size {rows}x{cols} exceeds model input {height}x{width}")

    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value is None:
                continue
            if 0 <= value < channels:
                arr[0, value, r, c] = 1.0
    return arr


def decode_model_output(output: Any, original_shape: Optional[Tuple[int, int]] = None) -> List[List[int]]:
    arr = np.asarray(output)

    if arr.ndim == 4 and arr.shape[0] == 1:
        arr = arr[0]

    if arr.ndim == 3 and arr.shape[0] > 1:
        grid = np.argmax(arr, axis=0)
    elif arr.ndim == 2:
        grid = arr.astype(np.int64)
    else:
        raise ValueError(f"Unsupported model output shape: {arr.shape}")

    if original_shape is not None:
        rows, cols = original_shape
        grid = grid[:rows, :cols]

    return grid.astype(int).tolist()


def solve_task001(grid: List[List[int]]) -> List[List[int]]:
    """Implements the Task001 rule described in explanations: expand each input cell into a 3x3 block.

    Expects a 3x3 input grid and returns a 9x9 output grid.
    """
    if not grid or not grid[0]:
        return []
    h = len(grid)
    w = len(grid[0])
    out = [[0 for _ in range(w * 3)] for _ in range(h * 3)]
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            for di in range(3):
                for dj in range(3):
                    out[i * 3 + di][j * 3 + dj] = c
    return out


def solve_with_model(task_id: str, grid: List[List[int]]) -> List[List[int]]:
    session = load_task_model(task_id)
    if session is None:
        raise FileNotFoundError(f"No ONNX model found for {task_id}")

    input_meta = session.get_inputs()[0]
    input_shape = input_meta.shape
    if len(input_shape) != 4:
        raise ValueError(f"Unexpected ONNX input shape: {input_shape}")

    channels = input_shape[1] if input_shape[1] is not None else 10
    height = input_shape[2] if input_shape[2] is not None else 30
    width = input_shape[3] if input_shape[3] is not None else 30

    model_input = encode_grid(grid, channels=channels, height=height, width=width)
    outputs = session.run(None, {input_meta.name: model_input})
    return decode_model_output(outputs[0], original_shape=(len(grid), len(grid[0])))


def solve(task_id: str, grid: List[List[int]]) -> Any:
    if task_id == 'task001' and len(grid) <= 9 and len(grid[0]) <= 9:
        return solve_task001(grid)

    session = load_task_model(task_id)
    if session is not None:
        return solve_with_model(task_id, grid)

    if task_id == 'task001':
        return solve_task001(grid)

    raise NotImplementedError(f"Solver for {task_id} not implemented")


if __name__ == '__main__':
    demo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    out = solve('task001', demo)
    for row in out:
        print(''.join(str(x) for x in row))
