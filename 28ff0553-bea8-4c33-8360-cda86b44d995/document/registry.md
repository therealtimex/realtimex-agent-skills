---
name: document-registry
description: This skill retrieves and manages document registry information, which classifies pages in PDF documents and splits them into smaller, organized documents with metadata.
---

## Tool Usage
Call tool `get_registry`

### `get_registry`
Retrieves the document registry for a given batch and file.

**Parameters:**
- `batch_id` (string): The unique identifier for the document batch
- `file_path` (string): The path to the PDF file

**Returns:**
A JSON object containing an array of document entries with the following structure:

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "description": "Registry Schema",
    "title": "registry",
    "type": "object",
    "properties": {
        "registry": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "doc_title": {
                        "type": "string",
                        "description": "Title of the document"
                    },
                    "doc_type": {
                        "type": "string",
                        "enum": [
                            "Commercial Invoice",
                            "Proforma Invoice",
                            "Packing List",
                            "Master B/L",
                            "House B/L",
                            "Master AWB",
                            "House AWB",
                            "CMR",
                            "Certificate of Origin",
                            "EUR.1",
                            "GSP Form A",
                            "USMCA Certification",
                            "FTA Certificate",
                            "Letter of Credit",
                            "DGD",
                            "Insurance Certificate",
                            "Inspection Report",
                            "Phytosanitary",
                            "Fumigation",
                            "ATA Carnet",
                            "Temporary Import Bond",
                            "Other"
                        ]
                    },
                    "page_start": {
                        "type": "integer"
                    },
                    "page_end": {
                        "type": "integer"
                    },
                    "key_identifiers": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                },
                "required": [
                    "doc_title",
                    "doc_type",
                    "page_start",
                    "page_end",
                    "key_identifiers"
                ],
                "additionalProperties": false
            }
            
        }
    },
    "required": [
        "registry"
    ],
    "additionalProperties": false
}
```

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `doc_title` | string | The title/name of the document |
| `doc_type` | string | Classification type (e.g., "Commercial Invoice", "Other") |
| `page_start` | number | Starting page number in the original PDF (0-indexed) |
| `page_end` | number | Ending page number in the original PDF (0-indexed) |
| `key_identifiers` | array | Important identifiers found in the document (IDs, amounts, dates, etc.) |
| `doc_name` | string | Generated filename for the extracted document |

## Example Usage


## Use Cases

1. **Document Splitting**: Automatically split large PDF files into individual documents based on page ranges
2. **Document Classification**: Identify document types within a batch upload
3. **Metadata Extraction**: Retrieve key identifiers for indexing and searching
4. **Document Tracking**: Map relationships between documents using shared identifiers (e.g., invoice numbers, contract IDs)
5. **Workflow Routing**: Route documents to appropriate processing pipelines based on `doc_type`

## Sample Response

```json
{
  "registry": [
    {
      "doc_title": "Commercial Invoice IPL211123",
      "doc_type": "Commercial Invoice",
      "page_start": 7,
      "page_end": 8,
      "key_identifiers": ["IPL211123", "23-11-2021", "36388,00"],
      "doc_name": "commercial_invoice.pdf"
    }
  ]
}
```

## Best Practices

- Always check if the registry array is not empty before processing
- Use `key_identifiers` to link related documents across the registry
- Page numbers are 0-indexed; add 1 for human-readable page numbers
- The `doc_type` field helps determine subsequent processing workflows