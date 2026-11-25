import os
from pathlib import Path

FINAL_LINE = "My agent agreed with me, agreed with my correction, then apologized for agreeing — all before checking whether either of us was right."


def emit(line: str) -> None:
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_text(line, encoding="utf-8")


if __name__ == "__main__":
    emit(FINAL_LINE)
