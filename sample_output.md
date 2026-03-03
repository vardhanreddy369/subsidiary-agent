# Sample Final Output Format

This document demonstrates the target outcome of the Agentic AI Subsidiary Research Project. 

The goal is to append 4 new columns (`TimeIn`, `TimeOut`, `MainSource`, `Type`) to the original dataset using a combination of deterministic database matching and AI-powered web searching.

## Example Data Transformation

### Before Processing (Original Data format)
| CIK | FDATE | COMP_NAME | SUB_NAME |
| :--- | :--- | :--- | :--- |
| `1652044` | `2016-01-31` | `Alphabet Inc.` | `Google LLC` |
| `00146xx` | `2014-06-15` | `Facebook Inc.` | `WhatsApp` |
| `0001010551` | `2000-03-30` | `AE Properties` | `2677 Main Street Associates` |

---

### After Processing (Final Deliverable format)
| CIK | FDATE | COMP_NAME | SUB_NAME | **TimeIn** | **TimeOut** | **MainSource** | **Type** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `1652044` | `2016-01-31` | `Alphabet Inc.` | `Google LLC` | **`2015-10-02`** | **`N/A`** | **`https://www.sec.gov/Archives/edgar/...`** | **`Restructuring`** |
| `00146xx` | `2014-06-15` | `Facebook Inc.` | `WhatsApp` | **`2014-02-19`** | **`N/A`** | **`TechCrunch: Facebook acquires WhatsApp`** | **`External (Acquisition)`**|
| `0001010551` | `2000-03-30` | `AE Properties` | `2677 Main Street` | **`1998-05-12`** | **`2005-11-01`** | **`Compustat M&A Database`** | **`Internal`** |

## Explanations of Added Columns
*   **TimeIn:** The exact date or year the subsidiary relationship began (e.g., when it was incorporated, acquired, or restructured).
*   **TimeOut:** The exact date or year the subsidiary was divested, sold, or dissolved. If it remains an active subsidiary, this is marked as `N/A`.
*   **MainSource:** The primary data source used to verify these dates. This could be a direct link to an SEC filing, a news article URL found by the AI Web Agent, or a reference to a bulk financial database (like Capital IQ or Compustat).
*   **Type:** Categorization of how the subsidiary was formed (Internal registration, External acquisition, or Corporate Restructuring).
