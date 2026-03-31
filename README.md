# CurryScope 🥘
### A Sri Lankan Recipe Information Retrieval System with Singlish Query Expansion

CurryScope is a domain-specific search engine designed for Sri Lankan recipes.

It solves a real-world vocabulary gap: users often search using **Singlish/Sinhala terms** like *"kukulmas curry"* or *"isso hodi"*, which traditional search engines fail to understand due to lack of semantic mapping.

CurryScope bridges this gap using preprocessing, spell correction, and a custom-built Singlish → English query expansion system.

This project is inspired by concepts from *Search Engines: Information Retrieval in Practice* (Croft et al.).

---

## 🧠 System Overview

CurryScope is built around two main pipelines:

User Query → Query Pipeline → Ranked Results  
                             ↑  
                     Inverted Index  
                             ↑  
                    Indexing Pipeline  

---

## ⚙️ Indexing Pipeline (Offline)

The indexing pipeline prepares all data structures required for efficient search.

### 1. Text Acquisition
- Recipe data is collected using a Scrapy-based web crawler  
- Crawling is done responsibly following `robots.txt`

---

### 2. Text Transformation

Standard NLP preprocessing is applied:

- Tokenization  
- Lowercasing (Normalization)  
- Stopword Removal  
- Stemming  

**Example:**

"Sri Lankan Chicken Curry"  
→ ["sri", "lankan", "chicken", "curry"]  
→ ["sri", "lankan", "chicken", "curri"]  
→ ["chicken", "curri"]

---

### 3. Index Creation (Inverted Index)

An inverted index maps terms to documents.

Example:

```json
{
  "chicken": {
    "12": { "tf": 2, "positions": [1, 5] },
    "40": { "tf": 1, "positions": [3] }
  }
}
### 4. Additional Statistics (for Ranking)

During indexing, several auxiliary statistics are computed and stored to support efficient and accurate ranking at query time.

These include:

- **doc_len.json** — stores the length of each document  
- **avg_doc_len** — average document length across the collection  
- **doc_field_len.json** — length of specific fields (e.g., title, ingredients) per document  
- **avg_field_len.json** — average length for each field  
- **recipe_map.json** — metadata mapping used for fast result formatting and retrieval  

These statistics are essential for ranking algorithms like **BM25**, which rely on term frequency, document length normalization, and collection-level averages.

---

### 5. K-gram Index (for Spell Correction)

To efficiently handle misspelled queries, CurryScope builds a **K-gram index** during indexing.

A K-gram is a sequence of *k* consecutive characters. In this system, **bigrams (k = 2)** are used.

**Example:**"curry" → ["cu", "ur", "rr", "ry"]

This structure allows the system to quickly identify candidate words that share similar character patterns with a query term, significantly reducing the search space for spell correction.

---

## 🔍 Query Pipeline (Online)

The query pipeline handles user queries in real time and transforms them into ranked search results.

---

### 1. Query Transformation

#### a. Preprocessing

The query undergoes the same preprocessing steps used during indexing:

- Tokenization  
- Normalization (lowercasing)  
- Stopword removal  
- Stemming  

This ensures consistency between indexed data and incoming queries.

---

#### b. Spell Correction

CurryScope uses a **two-stage spell correction approach**:

##### 🔹 Step 1: Candidate Generation (K-grams)
The K-gram index is used to retrieve a set of candidate terms that are similar to the input query term based on shared character sequences.

##### 🔹 Step 2: Candidate Ranking (Levenshtein Distance)

Each candidate is then evaluated using **Levenshtein Distance (Edit Distance)**, which measures the minimum number of operations required to transform one word into another.

Allowed operations:
- Insertion  
- Deletion  
- Substitution  

**Example:**"curri" → "curry" → Edit Distance = 1

---

### Edit Distance Visualization

Comparing: `"curri"` → `"curry"`

|   |   | c | u | r | r | y |
|---|---|---|---|---|---|---|
|   | 0 | 1 | 2 | 3 | 4 | 5 |
| c | 1 | 0 | 1 | 2 | 3 | 4 |
| u | 2 | 1 | 0 | 1 | 2 | 3 |
| r | 3 | 2 | 1 | 0 | 1 | 2 |
| r | 4 | 3 | 2 | 1 | 0 | 1 |
| i | 5 | 4 | 3 | 2 | 1 | 1 |

**Final Edit Distance = 1**

Each cell represents the minimum number of operations required to transform prefixes of one word into another. The value in the bottom-right corner gives the final edit distance.

---

### 2. Singlish Query Expansion

To handle local language variations, CurryScope applies a manually curated query expansion step.

Examples:

- kukulmas → chicken  
- isso → prawn  
- hodi → curry  

This significantly improves recall for culturally specific queries that would otherwise fail in traditional search systems.

---

### 3. Retrieval from Inverted Index

After transformation, each query term is used to retrieve matching documents from the inverted index.

Two common processing strategies are supported:

- **TAAT (Term-at-a-Time)**  
- **DAAT (Document-at-a-Time)**  

Both approaches produce the same final results, differing only in how scores are accumulated during processing.I used TAAT strategy:)

---

### 4. Ranking

Documents are ranked using:

- **BM25 ranking algorithm**  
- Field-based weighting (e.g., title vs ingredients)  
- Term frequency and precomputed document statistics  

Documents are then sorted in descending order of relevance score.

---

### 5. Results

The system returns:

- A ranked list of recipes  
- Recipe titles  
- Relevance scores  

---

## 🚀 Features

- Domain-specific search (Sri Lankan recipes)  
- Singlish → English query expansion  
- Spell correction using K-grams + Levenshtein Distance  
- BM25 ranking with field-aware scoring  
- Efficient inverted index-based retrieval  

---

## 🛠️ Tech Stack

- Python  
- Scrapy  
- fastapi
- Javascript
- CSS
- HTML
---

## 📌 Future Improvements

- Evaluation metrics (Precision, Recall, MAP)  
- Autocomplete and query suggestions  
- Neural ranking models  
- Sinhala native language support  

---

## 📎 Project Status

Actively being developed as a learning and portfolio project.

---

## 💡 Author Note

This project is part of my journey in learning Information Retrieval and backend systems.

I am building everything from scratch to deeply understand how real-world search engines work.

Contributions, suggestions, and feedback are always welcome 🚀