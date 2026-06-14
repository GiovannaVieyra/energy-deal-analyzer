import pandas as pd
import os

RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "data-raw")
os.makedirs(RAW_DIR, exist_ok=True)

def load_wholesale_prices() -> pd.DataFrame:
    data = {
        "hub":                        ["ERCOT", "PJM", "MISO", "CAISO", "ISO-NE", "NYISO"],
        "region":                     ["Texas", "Mid-Atlantic", "Midwest", "California", "New England", "New York"],
        "price_2022":                 [57.8, 72.4, 59.1, 91.3, 80.2, 71.4],
        "price_2023":                 [43.2, 55.8, 43.7, 68.9, 62.1, 54.3],
        "price_2024":                 [31.5, 44.2, 33.8, 53.1, 56.4, 47.8],
        "price_2025_forecast":        [33.0, 47.0, 36.0, 58.0, 61.0, 51.0],
        "interconnection_wait_years": [2.5,   7.0,  5.5,  6.0,  4.0,  4.5],
        "renewable_pct_2024":         [32,    22,   18,   61,   38,   34],
    }
    df = pd.DataFrame(data)
    path = os.path.join(RAW_DIR, "wholesale_prices.csv")
    df.to_csv(path, index=False)
    print(f"[ETL] Bloque 1 OK -> {path}")
    return df
    
def load_renewable_capacity() -> pd.DataFrame:
    data = {
        "state":        ["CA","TX","FL","AZ","NV","NC","GA","NJ","VA","NY",
                        "TX","IA","OK","KS","CA","IL","MN","CO","ND","OR"],
        "technology":   (["Solar PV"] * 10) + (["Wind"] * 10),
        "capacity_gw":  [42.1,25.8,16.4,12.7,9.8,9.2,7.1,6.8,6.4,5.9,
                        43.2,12.8,12.1,9.3,7.2,7.0,6.9,5.8,4.9,4.2],
        "lcoe_min":     [24,27,28,22,23,29,30,35,31,36,
                        26,25,24,24,30,27,26,27,24,28],
        "lcoe_max":     [38,42,41,35,36,44,45,52,47,53,
                        35,34,33,33,42,38,37,38,34,39],
    }  
    df = pd.DataFrame(data)
    path = os.path.join(RAW_DIR, "renewable_capacity.csv")
    df.to_csv(path, index=False)
    print(F"[ETL] Bloque 2 OK -> {path}")
    return df

def load_deals_benchmark() ->  pd.DataFrame:
    data = {
        "year":         [2023, 2024, 2024, 2025, 2025, 2026, 2026],
        "buyer":        ["Microsoft", "Microsoft", "Amazon", "Meta", "Google", "Google", "Meta"],
        "technology":   ["Nuclear", "Wind/Solar", "Nuclear", "Nuclear", "Nuclear (SMR)", "Solar", "Nuclear"],
        "capacity_mw":  [835, 10500, 960, 2600, 1155, 1000, 2600],
        "deal_type":    ["PPA", "PPA", "PPA", "PPA", "PPA", "PPA", "PPA"],
        "term_years":   [20, 15, 20, 20, None, 20, 20],
        "market":       ["PJM", "US+EU", "PJM", "PJM", "Multiple", "ERCOT", "PJM"],
        "notes": [
            "Restart of Three Mile Island Unit 1",
            "Largest corporate renewable PPA at signing",
            "Co-location at Susquehanna nuclear plant PA",
            "Perry Davis-Besse Beaver Valley plants",
            "First SMR corporate PPA",
            "First gigawatt-scale single solar PPA",
            "Zero-carbon baseload for AI workloads",
        ]
    }
    df = pd.DataFrame(data)
    path = os.path.join(RAW_DIR, "deals_benchmark.csv")
    df.to_csv(path, index=False)
    print(F"[ETL] Bloque 3 OK -> {path}")
    return df

def load_dc_economics() -> pd.DataFrame:
    data = {
        "metric": [
            "Revenue per MW per year - AI datacenter",
            "Revenue per MW per year - standard datacenter",
            "Energy cost as % of opex",
            "Typical PPA term",
            "Interconnection wait - PJM/MISO",
            "Interconnection wait - ERCOT",
            "Average corporate PPA price 2024",
            "Average utility rate large industrial 2024",
            "Solar LCOE 2024",
            "Wind LCOE 2024",
            "Nuclear LCOE 2024",
        ],
        "value": [11.0, 4.5, 30, 15, 8.5, 2.5, 52, 68, 31, 30, 89],
        "unit": [
            "M USD/MW/yr", "M USD/MW/yr", "%", "years",
            "years", "years",
            "USD/MWh", "USD/MWh", "USD/MWh", "USD/MWh", "USD/MWh",
        ],
        "source": [
            "EIA / industry reports 2025",
            "EIA 2024",
            "BloombergNEF 2025",
            "BNEF Corporate PPA Market 2024",
            "FERC/PJM queue data 2025",
            "ERCOT 2025",
            "LevelTen Energy Q4 2024",
            "EIA Electric Power Monthly 2024",
            "NREL ATB 2024",
            "NREL ATB 2024",
            "NREL ATB 2024",
        ]
    }
    df = pd.DataFrame(data)
    path = os.path.join(RAW_DIR, "dc_economics.csv")
    df.to_csv(path, index=False)
    print(f"[ETL] Bloque 4 OK -> {path}")
    return df

if __name__ == "__main__":
    load_wholesale_prices()
    load_renewable_capacity()
    load_deals_benchmark()
    load_dc_economics()