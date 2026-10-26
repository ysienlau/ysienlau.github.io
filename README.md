# Ysien Lau

**About Me**

I'm an MPA candidate in Data Science for Public Policy at the London School of Economics (2025–2027), and hold a BA (Hons) in History at Yale-NUS (2016-2020). Before LSE, I spent five years in government affairs and policy research across Southeast Asia, turning regulatory and political developments into analysis and recommendations for senior decision-makers.

I'm now combining that policy background with data science to work on questions where analytical rigour and stakeholder insight both matter.

**Website:** [ysienlau.github.io](https://ysienlau.github.io) · **LinkedIn:** [ysien-lau](https://www.linkedin.com/in/ysien-lau)

---

## Featured work

### Frontier Industry Potential in South Yorkshire: group project (Data Science for Public Policy) - presented to the LSE Growth Lab
Which local conditions are correlated with the UK Industrial Strategy's high-growth (IS-8) sectors, and what should South Yorkshire do about it? We analysed 355 English local authorities and 171 South Yorkshire neighbourhoods using ONS and Nomis data (2019–2024).

- **Methods:** lasso and elastic net for variable selection, PCA and k-means clustering to compare regions, and spatial clustering analysis (Moran's I, LISA)
- **Key finding:** all 15 IS-8 employment hotspots are in Sheffield, and proximity to anchor institutions accounts for about a third of the clustering
- **Recommendation:** a differentiated "Deepen, Extend, Enable" strategy for the region's four districts
- **My role:** cleaned and merged the local authority panel; built the lasso and elastic net models with grouped cross-validation; co-developed the policy recommendations

**Tools:** Python (pandas, scikit-learn, GeoPandas)

### PP434 Automated Data Visualisation: portfolio
Weekly challenges in building, publishing and critiquing charts with Vega-Lite, including:
- **Policy commentary:** the fiscal and household impact of scrapping the UK's two-child limit on Universal Credit (OBR, IFS data)
- **Replication:** recreating and improving a *Financial Times* chart on income tax rates for high earners

[View the portfolio →](https://ysienlau.github.io/pp434/) · [Class exercises →](https://ysienlau.github.io/pp434/exercises.html)

---

## Skills

- **Data analysis:** Python (pandas, NumPy, scikit-learn), Stata; working with JSON/API data
- **Visualisation:** Vega-Lite, Matplotlib, Seaborn, plotnine
- **Statistical methods:** regression analysis, causal inference, data cleaning, spatial analysis (Moran's I)
- **Machine learning:** regularised regression (lasso, elastic net), tree-based models (decision trees, random forests), unsupervised learning (clustering, PCA)
- **Tools:** Git/GitHub, HTML/CSS

---

## Repository structure

This repo hosts my personal site via GitHub Pages.

```
├── index.html          # Home page
├── about.html          # About / CV
├── css/                # Stylesheets
└── pp434/              # PP434 Automated Data Visualisation (LSE)
    ├── index.html      # Portfolio (challenges 1–4)
    ├── exercises.html  # Weekly class exercises
    ├── week1/ … week4/ # Chart specs (Vega-Lite JSON), data and notebooks
    └── project/        # Individual project (in progress)
```
