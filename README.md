# AVYield - Analysis and Visualization of Crop Yield Trials

AVYield is a digital interactive decision dashboard for crop yield trials, enabling near-real-time exploration and comparison of multi-year, multi-location crop trial data. It overlays farmers' own data with formal trial results to guide genotype and management decisions.

Try it out at [AVYield](https://www.avyield.com)!

---

## Paper & Citation

- **Link**: [A digital interactive decision dashboard for crop yield trials](https://www.sciencedirect.com/science/article/pii/S0168169925001437)
- **Citation**:

```bibtex
@article{CISDELI2025110037,
  title = {A digital interactive decision dashboard for crop yield trials},
  journal = {Computers and Electronics in Agriculture},
  volume = {231},
  pages = {110037},
  year = {2025},
  issn = {0168-1699},
  doi = {https://doi.org/10.1016/j.compag.2025.110037},
  url = {https://www.sciencedirect.com/science/article/pii/S0168169925001437},
  author = {Pedro Cisdeli and Gustavo {Nocera Santiago} and Carlos Hernandez and Ana Carcedo and P.V. Vara Prasad and Michael Stamm and Jane Lingenfelser and Ignacio Ciampitti},
  keywords = {Digital tool, Yield data, Crop genotypes, Visualization, Data repository},
}
```

---

## Features

- Filter and visualize trial data by crop, location, year, genotype, and water regime.
- Overlay custom farmer data on trial benchmarks.
- Perform on-the-fly genotype comparison analyses.
- Download datasets and export plots.

---

## Installation & Local Setup

### Prerequisites

- Python 3.8 or higher
  - Tested in Python 3.11
- `pip`

### Clone Repository

```bash
git clone https://github.com/cisdeli/AVYield.git
cd AVYield
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Locally

Edit `app.py` to update the server startup call:

```python
app.run_server(host='0.0.0.0', port=8050)  # local-host
# Instead of:
# app.run_server(debug=True, host="0.0.0.0", port=8080,
#                use_reloader=False)  # Docker
```

Then run:

```bash
python app.py
```

Open your browser to `http://localhost:8050` to access the dashboard.

---

## License

This project is licensed under the [CC BY 4.0 License](LICENSE).

---

## Acknowledgements

Developed by Pedro Cisdeli and collaborators. For full details, see the paper linked above.
