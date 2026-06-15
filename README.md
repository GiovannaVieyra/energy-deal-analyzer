# Energy Deal Analyzer

> Regional energy market analysis for data center procurement advisory - built a portfolio project simulating real-world Deal Analysis work in the energy consulting sector.

---

## Context

Energy costs represent -30% of data center operating expenses. For AI-focused facilities generating $11M/MW/year, delays in energy procurement directly translate to revenue loss. This project replicates the analysis an energy consultant would deliver to a client evaluating where in the US to procure power for a new data center.

---

## Key Question

**Which US energy market offers the best procurement conditions for a data center operator today?**

---

## Findings 

1. **ERCOT (Texas) is the clear top pick** - lowest wholesale prices in the country ($31.5/MWh in 2024) and fastest grid interconnection (2.5 years vs. 7+ years in PJM/MISO).
2. **MISO (Midwest) is a strong second option** - competitive pricing with growing renewable capacity, suitable for clients prioritizing long-term green energy commitments.
3. **CAISO (California) and ISO-NE (New England) should be avoided** - highest prices and long interconnection queues make energy procurement costly and slow.

---

## Project Structure

    energy-deal-analyzer/
    ├── data-raw/           # Raw datasets (EIA, NREL, industry reports)
    ├── data-processed/     # Scored and ranked output
    ├── src/
    │   ├── etl.py          # Data pipeline — loads and saves 4 datasets
    │   ├── analysis.py     # Regional scoring model (weighted index)
    │   └── dashboard.py    # Generates interactive HTML dashboard
    ├── outputs/
    │   └── dashboard.html  # Interactive Plotly dashboard
    └── requirements.txt

---

## Data Sources

| Dataset | Source |
|---|---|
| Wholesale electricity prices | EIA Electricity Monthly Update, Dec 2025 |
| Renewable capacity by state | EIA Electric Power Annual 2024 |
| Corporate PPA deals benchmark | Public press releases + EIA reports 2023–2026 |
| Data center economics | NREL ATB 2024, BloombergNEF 2025, EIA |

-----------------------------------------------------------------------

## Contexto

Los costos de energía representan aproximadamente el 30% de los gastos operativos de un data center. Para instalaciones de IA que generan $11M/MW/año, los retrasos en la obtención de energía se traducen directamente en pérdida de ingresos. Este proyecto replica el análisis que un consultor energético entregaría a un cliente que evalúa dónde en EE.UU. contratar suministro eléctrico para un nuevo data center.

---

## Pregunta central

**¿Qué mercado eléctrico de EE.UU. ofrece las mejores condiciones de aprovisionamiento energético para un operador de data center hoy?**

---

## Hallazgos

1. **ERCOT (Texas) es la opción más sólida** — precios mayoristas más bajos del país ($31.5/MWh en 2024) y la interconexión a la red más rápida (2.5 años vs. más de 7 años en PJM/MISO).
2. **MISO (Midwest) es una segunda opción competitiva** — precios accesibles y capacidad renovable en crecimiento, ideal para clientes que priorizan compromisos de energía verde a largo plazo.
3. **CAISO (California) e ISO-NE (Nueva Inglaterra) deben evitarse** — los precios más altos y las largas colas de interconexión hacen que el aprovisionamiento energético sea costoso y lento.

---

## Estructura del proyecto

    energy-deal-analyzer/
    ├── data-raw/           # Datasets crudos (EIA, NREL, reportes de industria)
    ├── data-processed/     # Output con scores y ranking por región
    ├── src/
    │   ├── etl.py          # Pipeline de datos — carga y guarda 4 datasets
    │   ├── analysis.py     # Modelo de scoring regional (índice ponderado)
    │   └── dashboard.py    # Genera dashboard interactivo en HTML
    ├── outputs/
    │   └── dashboard.html  # Dashboard interactivo con Plotly
    └── requirements.txt

---

## Fuentes de datos

| Dataset | Fuente |
|---|---|
| Precios mayoristas de electricidad | EIA Electricity Monthly Update, dic 2025 |
| Capacidad renovable por estado | EIA Electric Power Annual 2024 |
| Benchmark de deals corporativos (PPA) | Comunicados públicos + reportes EIA 2023–2026 |
| Economía de data centers | NREL ATB 2024, BloombergNEF 2025, EIA |