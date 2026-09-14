import hashlib
import json
import struct
from pathlib import Path

root = Path("/workspace")
image = root / "aosp/out/target/product/x08c/system.img"
digest = hashlib.sha256()
with image.open("rb") as stream:
    header = stream.read(28)
    stream.seek(0)
    for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
        digest.update(chunk)
magic, major, minor, file_header, chunk_header, block_size, blocks, chunks, checksum = struct.unpack("<IHHHHIIII", header)
if magic != 0xED26FF3A or major != 1 or block_size == 0:
    raise RuntimeError("Expected Android sparse system image")
expanded = block_size * blocks
if expanded > 2147483648:
    raise RuntimeError("Expanded system image exceeds the X08C partition")
report = {
    "result": "compiled_candidate_not_device_validated",
    "sha256": digest.hexdigest(),
    "file_bytes": image.stat().st_size,
    "expanded_bytes": expanded,
    "device_vintf_verified": False,
    "boot_verified": False,
    "flash_authorized_by_ci": False
}
(root / "artifacts/image.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
