# Subsidiary AI Agent: Project Update

### To: Dr. Vlad Gatchev, Dr. Christo Pirinsky, Dr. Rodney Ndum
### From: Sri Vardhan Reddy Gutta, Sarayu Panditi
### Date: March 3, 2026

---

## 1. What We Have Accomplished
We have successfully initiated the **Agentic AI Subsidiary Project** and built the core technical foundation:

*   **Data Processing:** We securely downloaded, processed, and cleaned the `subs_all.sas7bdat` dataset using Python (`pandas`). We handled byte-string decoding and successfully exported functional CSV samples for analysis.
*   **Scale Discovery:** We analyzed the dataset and identified that it contains approximately **437,000 unique rows** of subsidiary records.
*   **AI Agent Prototype:** We designed and built the fully working "Agentic AI" prototype requested (`agentic_search_pipeline.py`).
    *   The script autonomously queries public web data (via Tavily Search API) using the parent and subsidiary names.
    *   It feeds the context to an LLM (OpenAI GPT-4o) and successfully extracts the exact variables requested: **`TimeIn`**, **`TimeOut`**, **`MainSource`**, and **`Type`** (Internal, External, or Restructuring).
    *   We have tested this on a small control group and verified that it outputs the expected, structured JSON format.
*   **Version Control:** We established a centralized GitHub repository to manage our code, documentation, and sample outputs securely: [subsidiary-agent Repository](https://github.com/vardhanreddy369/subsidiary-agent)

---

## 2. Technical Challenges & Proposed Strategy
While the AI agent performs exceptionally well on an individual row basis, running live API web queries across **all 437,000 rows** sequentially presents immediate scale limitations:
1.  **Rate Limiting:** We will be throttled by search engine and LLM API frequency caps.
2.  **Cost:** Processing 400k+ rows through an LLM will incur extremely high per-token API fees.
3.  **Execution Time:** Sequential AI execution at this scale would easily take weeks to run locally.

### Our Solution: The Hybrid Pipeline Approach
To mitigate cost and execution constraints, we propose a two-phase architecture:
*   **Phase 1 (Bulk Deterministic Matching):** We first cross-reference the 437,000 rows against bulk structural databases containing historical M&A and subsidiary data (e.g., historical SEC Exhibit 21 filings via EDGAR, or Compustat bulk datasets accessible via the university). This standard data-engineering step will deterministically extract dates for ~70-80% of the dataset at zero API cost.
*   **Phase 2 (Agentic AI Edge-Case Processing):** The remaining subset of ambiguous records and exact divestiture dates (`TimeOut`) will be passed into our Python AI Web Agent to synthesize news articles and press releases.

---

## 3. What is Next (Action Items)

**For Our Team (Sri & Sarayu):**
1.  Investigate accessing structured bulk datasets (SEC EDGAR, Compustat, or Capital IQ) through the university library.
2.  Write the Python scripts to fuzzy-match company names and perform the Phase 1 bulk-join.
3.  Finalize the prompts in the AI Agent so it can parse complex divestiture events reliably.

**What We Need From the Faculty:**
1.  **Approval:** Let us know if the proposed "Hybrid Pipeline" methodology aligns with your research goals, or if you prefer we constrain the dataset size and exclusively use the Agentic AI.
2.  **Sample Validation:** We can run the AI agent on a random 500-row sample of the dataset. Would you like us to generate this sample and send the resulting spreadsheet back to you to ensure the AI's accuracy meets your standards before we scale up?
