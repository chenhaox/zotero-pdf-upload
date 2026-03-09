# zotero-pdf-upload

Standalone skill for practical Zotero operations.

## What it does

- Parse Zotero group/user URLs into `libraryType` + `libraryId`
- List and inspect existing collections
- Heuristically match an item to an existing collection
- Require explicit approval before creating collections/items
- Create Zotero item metadata
- Optionally upload/attach a PDF when enabled
- Load API key safely from env/path/config precedence

## Main scripts

- `scripts/zotero_workflow.py` — CLI entrypoint
- `scripts/zotero_client.py` — Zotero API client/utilities
- `tests/smoke_test_zotero_pdf_upload.py` — no-network smoke tests

## Quick start

1. Copy `references/config.example.json` to a local runtime file and fill values.
2. Export API key (recommended):

```bash
export ZOTERO_API_KEY='...'
```

3. Parse URL:

```bash
python scripts/zotero_workflow.py parse-url --url "https://www.zotero.org/groups/6320165/my-group/library"
```

4. List collections (read-only):

```bash
python scripts/zotero_workflow.py list-collections --config ./tmp.config.json
```

5. Choose collection (read-only):

```bash
python scripts/zotero_workflow.py choose-collection --config ./tmp.config.json --item-json references/item.example.json
```

6. Create collection (explicit write):

```bash
python scripts/zotero_workflow.py create-collection --config ./tmp.config.json --name "LLM Safety" --approve-create
```

7. Create item (explicit write):

```bash
python scripts/zotero_workflow.py create-item --config ./tmp.config.json --item-json references/item.example.json --auto-match-collection --approve-write
```
