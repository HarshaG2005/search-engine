# CurryScope 🥘
### A Sri Lankan Recipe Information Retrieval System with Singlish Query Expansion

CurryScope is a domain-specific search engine built for Sri Lankan recipes. 
It addresses a real vocabulary gap — someone searching "kukulmas cariya" or 
"isso hodi" gets zero results on conventional search engines because the 
Singlish/Sinhala terminology isn't mapped to English recipe vocabulary. 
CurryScope solves this through a manually curated query expansion thesaurus 
built specifically for Sri Lankan food terminology.

Built following Croft et al. *Search Engines: Information Retrieval in Practice*.

---

## Architecture

CurryScope follows two core pipelines:

### Indexing Pipeline
Runs offline to build the search structures.

- **Text Acquisition** — raw recipe data gathered and stored
- **Text Transformation** — tokenization, stopword removal, stemming
- **Index Creation** — inverted index with TF, positions, and field metadata

### Query Pipeline
Runs at search time against the built index.

- **Query Transformation** — spell correction, Singlish query expansion
- **Ranking** — BM25 with field boosting and proximity scoring
- **Results** — ranked list with titles and scores
 
