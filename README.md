# Feature Adoption Analysis

## Overview

This project analyses the adoption and behavioural impact of a newly launched product feature using event-based user data.

The goal was to evaluate:
- Feature adoption rate
- Adoption trends over time
- Revenue impact
- Adoption differences by device
- Time-to-adoption
- 7-day retention comparison

---

## Dataset

Synthetic event-based dataset including:
- 1000 users
- 5368 events
- Purchase revenue data (`order_value`)
- Feature usage events (`feature_used`)

---

## Key Results

- Adoption Rate: 41.4%
- Adoption increased steadily without a viral spike.
- Android users had the highest adoption count.
- Revenue impact varied between adopters and non-adopters.
- Retention analysis revealed behavioural differences.

---

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## Project Structure

---

## How To Run

1. Install dependencies from `requirements.txt`
2. Run `src/generate_dataset.py`
3. Open `notebooks/feature_adoption_analysis.ipynb`
4. Run all cells
