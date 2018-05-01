# TilburgEconomicsRanking
Compiled data of the Tilburg University Top Worldwide Economics Schools Research Ranking.

## What is this?
To ease the use of Economics Departments rankings in my research, I have compiled a panel dataset using the yearly Tilburg University Economics School Research Rankings.  These data originate from https://econtop.uvt.nl/rankingsandbox.php.  In May 2018 I made the data public so that everyone can use them freely.  Please report mistakes in the data to them.

## How do I use this?

In folder [combined/](./combined/) you find six files: Two files for each of their weighting method, of which one is the original data and one includes liner interpolation for inner missings.  They report both the rank and their computed scores.  The files are in long format to ease merging.

Usage in your scripts is easy:

* In python (with pandas):
```python
import pandas as pd
url = 'https://raw.githubusercontent.com/Michael-E-Rose/TilburgEconomicsRanking/master/combined/Article_Influence_Score.csv'
df = pd.read_csv(url)
```

* In R:
```R
url = 'https://raw.githubusercontent.com/Michael-E-Rose/TilburgEconomicsRanking/master/combined/Article_Influence_Score.csv'
df <- read.csv(url)
```

* In Stata:
```Stata
insheet using "https://raw.githubusercontent.com/Michael-E-Rose/TilburgEconomicsRanking/master/combined/Article_Influence_Score.csv"
```

## What's the benefit?
- Central and continuously updated online storage for seamless inclusion in local scripts.
- Longitudinal collection of the Ranks and Scores according to their three different methods.
- Interpolated version without inner missings as alternative.
