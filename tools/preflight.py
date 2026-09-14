import json
import os
import platform
import shutil
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
lock = json.loads((root / "upstream.lock.json").read_text())
issues = []
if platform.system() != "Linux" or platform.machine() != "x86_64":
    issues.append("An x86_64 Linux runner is required")
disk = shutil.disk_usage(root)
if disk.free < 300 * 1024 ** 3:
    issues.append("At least 300 GiB free is required by this full-build workspace budget")
if not shutil.which("docker"):
    issues.append("Docker is required")
if lock["tag"] != "android-9.0.0_r61" or len(lock["manifest_commit"]) != 40:
    issues.append("Unexpected upstream lock")
board = (root / "device/xiaomi/x08c/BoardConfig.mk").read_text()
for setting in ("TARGET_USES_64_BIT_BINDER := true", "BOARD_SYSTEMIMAGE_PARTITION_SIZE := 2147483648"):
    if setting not in board:
        issues.append("Missing board contract: " + setting)
report = {
    "result": "blocked" if issues else "ready_to_attempt_build",
    "free_gib": round(disk.free / 1024 ** 3, 2),
    "architecture": platform.machine(),
    "cpu_count": os.cpu_count(),
    "source_commit": os.environ.get("GITHUB_SHA"),
    "errors": issues,
    "device_compatibility_verified": False
}
artifacts = root / "artifacts"
artifacts.mkdir(exist_ok=True)
(artifacts / "preflight.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2), flush=True)
sys.exit(1 if issues else 0)
