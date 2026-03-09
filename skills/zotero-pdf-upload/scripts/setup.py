#!/usr/bin/env python3
"""One-line setup: generate runtime config from a Zotero URL.

Usage:
    python scripts/setup.py "https://www.zotero.org/groups/123456/my-group/library"

This creates a ready-to-use config file (config.json) in the skill root.
The Zotero API key is read from the ZOTERO_API_KEY environment variable at runtime.
"""

import json
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = SKILL_ROOT / "config.json"
TEMPLATE = {
    "zotero": {
        "url": "",
        "libraryType": "",
        "libraryId": "",
        "apiKeyEnv": "ZOTERO_API_KEY",
        "apiKeyPath": "",
        "apiKey": "",
        "timeoutSec": 30,
        "allowPdfUpload": True,
    }
}


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("Usage: python scripts/setup.py <ZOTERO_LIBRARY_URL>")
        print()
        print("Example:")
        print('  python scripts/setup.py "https://www.zotero.org/groups/123456/my-group/library"')
        print('  python scripts/setup.py "https://www.zotero.org/myusername/library"')
        print()
        print("Then set your API key:")
        print("  export ZOTERO_API_KEY='your-key-here'")
        return 0

    url = sys.argv[1].strip()
    if not url:
        print("Error: URL cannot be empty.")
        return 1

    config = TEMPLATE.copy()
    config["zotero"] = {**TEMPLATE["zotero"], "url": url}

    if CONFIG_PATH.exists():
        print(f"⚠️  Config already exists at {CONFIG_PATH}")
        answer = input("   Overwrite? [y/N] ").strip().lower()
        if answer not in ("y", "yes"):
            print("   Aborted.")
            return 0

    CONFIG_PATH.write_text(json.dumps(config, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"✅ Config written to {CONFIG_PATH}")
    print()
    print("Next step — set your Zotero API key:")
    print("  export ZOTERO_API_KEY='your-key-here'")
    print()
    print("Then try:")
    print(f'  python scripts/zotero_workflow.py list-collections --config {CONFIG_PATH}')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
