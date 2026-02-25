# Computational Analysis of Naguib Mahfouz's Cairo Trilogy

A computational literary analysis of Naguib Mahfouz's iconic **Cairo Trilogy** — *Palace Walk*, *Palace of Desire*, and *Sugar Street* — using Python-based data visualization to explore patterns across the three novels.

---

## About the Project

Naguib Mahfouz's Cairo Trilogy (1956–57) is one of the greatest works of Arabic literature, following three generations of the Al-Sayyid Abd al-Jawad family in Cairo from WWI through Egypt's 1952 revolution. This project applies computational methods to analyze and visualize textual or structural data across the trilogy, surfacing patterns that would be difficult to detect through close reading alone.

The analysis produces heatmaps that allow comparison across the three books, highlighting how themes, characters, or linguistic features shift over the course of the saga.

---

## Repository Structure

```
├── heatmap.py                      # Main analysis and visualization script
├── Book1.xlsx                      # Data for Palace Walk
├── Book2.xlsx                      # Data for Palace of Desire
├── Book3.xlsx                      # Data for Sugar Street
├── cairo_trilogy_heatmap.png       # Heatmap visualization across all three books
├── palace_of_desires_heatmap.png   # Heatmap visualization for Palace of Desire
└── LICENSE                         # MIT License
```

---

## Getting Started

### Prerequisites

- Python 3.7+
- The following Python libraries:
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `openpyxl`

Install dependencies with:

```bash
pip install pandas matplotlib seaborn openpyxl
```

### Running the Analysis

```bash
python heatmap.py
```

This will read the three Excel data files and generate heatmap visualizations as `.png` outputs.

---

## Visualizations

| Visualization | Description |
|---|---|
| `cairo_trilogy_heatmap.png` | Comparative heatmap across all three novels |
| `palace_of_desires_heatmap.png` | Detailed heatmap for *Palace of Desire* |

---

## The Cairo Trilogy

| Book | Original Title | Year |
|---|---|---|
| *Palace Walk* | بين القصرين | 1956 |
| *Palace of Desire* | قصر الشوق | 1957 |
| *Sugar Street* | السكرية | 1957 |

Mahfouz was awarded the Nobel Prize in Literature in 1988, in part due to the enduring significance of this trilogy.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Author

**Zoya Muneeb** — [GitHub Profile](https://github.com/ZoyaMuneeb)
