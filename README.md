# 📎 zotero-pdf-upload

> Standalone skill for practical Zotero operations — upload PDFs, manage collections, and create items via the Zotero Web API.

## ⚡ Quick Setup (one-liner)

```bash
# 1️⃣  Set your Zotero API key (get one at https://www.zotero.org/settings/keys)
export ZOTERO_API_KEY='your-api-key-here'

# 2️⃣  Generate config from your Zotero library URL
python scripts/setup.py "https://www.zotero.org/groups/123456/my-group/library"

# ✅ Done! Try listing your collections:
python scripts/zotero_workflow.py list-collections --config config.json
```

Personal library? Just use your personal URL instead:

```bash
python scripts/setup.py "https://www.zotero.org/myusername/library"
```

---

## 🔧 What it does

- 🔗 Parse Zotero group/user URLs into `libraryType` + `libraryId`
- 📂 List and inspect existing collections
- 🎯 Heuristically match an item to an existing collection
- ✋ Require explicit approval before creating collections/items
- 📝 Create Zotero item metadata
- 📤 Optionally upload/attach a PDF when enabled
- 🔐 Load API key safely from env/path/config precedence

## 📁 Main scripts

| Script | Description |
|--------|-------------|
| `scripts/setup.py` | ⚡ One-line config generator |
| `scripts/zotero_workflow.py` | 🚀 CLI entrypoint |
| `scripts/zotero_client.py` | 🔌 Zotero API client/utilities |
| `tests/smoke_test_zotero_pdf_upload.py` | 🧪 No-network smoke tests |

## 📖 Detailed Usage

### 1️⃣ Parse URL

```bash
python scripts/zotero_workflow.py parse-url --url "https://www.zotero.org/groups/123456/my-group/library"
```

### 2️⃣ List collections (read-only)

```bash
python scripts/zotero_workflow.py list-collections --config config.json
```

### 3️⃣ Choose collection (read-only)

```bash
python scripts/zotero_workflow.py choose-collection --config config.json --item-json references/item.example.json
```

### 4️⃣ Create collection (explicit write)

```bash
python scripts/zotero_workflow.py create-collection --config config.json --name "LLM Safety" --approve-create
```

### 5️⃣ Create item + attach PDF (explicit write)

```bash
python scripts/zotero_workflow.py create-item \
  --config config.json \
  --item-json references/item.example.json \
  --auto-match-collection \
  --attach-pdf /path/to/paper.pdf \
  --approve-write
```

## 🧪 Tests

```bash
python tests/smoke_test_zotero_pdf_upload.py
```

## 📄 License

MIT
