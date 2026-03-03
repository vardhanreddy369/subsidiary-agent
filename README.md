# Subsidiary AI Agent

![Project Banner](project_banner.png)

This project contains research scripts to automate the extraction of historical subsidiary data (`TimeIn`, `TimeOut`, and `MainSource`) from public records using an Agentic AI pipeline.

## Project Context
Given a massive dataset of ~437,000 corporate subsidiaries (`subs_all.sas7bdat`), this project explores how to automatically fill in the timeline of when a subsidiary was formed/acquired and when it was divested. 

Because running an LLM web-search agent on 400k+ rows is cost and time-prohibitive, this repository demonstrates a **Hybrid Approach**: 
1. **Bulk Deterministic Matching (Planned):** Cross-referencing SEC EDGAR files for cheap, fast date-matching.
2. **Agentic Web Pipeline (`agentic_search_pipeline.py`):** A RAG-powered web-searching AI (via Tavily and OpenAI) to handle complex edge cases and find divestiture dates.

## Files
- `clean_dataset.py`: Utility script to process the massive SAS file, fix encoding, and export manageable CSV samples.
- `explore.py`: Basic script to peek inside the `.sas7bdat` format.
- `agentic_search_pipeline.py`: A complete prototype of the AI agent that searches the web, reads articles, and uses GPT-4 to output structured JSON dates.
- `subs_sample.csv`: A sample 100-row output to test the AI pipeline.

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/vardhanreddy369/subsidiary-agent.git
cd subsidiary-agent
```

2. (Optional) Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the requirements (like pandas, openai, requests):
```bash
pip install pandas numpy openai requests
```

4. Set your API Keys to run the AI agent:
```bash
export OPENAI_API_KEY="your-openai-key"
export TAVILY_API_KEY="your-tavily-key"
```

5. Run a test batch of 5 rows from the sample dataset:
```bash
python agentic_search_pipeline.py --batch 5
```
