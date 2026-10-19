# Retrieval-Augmented Generation (RAG)

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Chunking & Embeddings**: Documents split into 512-token chunks with overlap, vectorized via embedding models.
- **Dense Vector Search**: Approximate nearest neighbor (ANN) retrieval from vector database.
- **Context Injection**: Retrieved passages injected into system prompt to eliminate LLM hallucinations.
