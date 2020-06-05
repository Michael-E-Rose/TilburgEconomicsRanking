#!/usr/bin/env python3
# Author:   Michael E. Rose <michael.ernst.rose@gmail.com>
"""Combines yearly Tilburg Economics Schools rankings for the same
weighting factor.
"""

import os
from glob import glob

import pandas as pd

SOURCE_FOLDER = "./raw_data/"
TARGET_FOLDER = "./combined/"


def interpolate(df, key):
    """Interpolate subset of MulitIndex df."""
    subset = df.xs(key, level=0, drop_level=False, axis=1)
    return (subset.interpolate(axis=1)
                  .where(subset.fillna(method='bfill', axis=1).notnull()))


def read_dataframes(files):
    """Read all Tilburg Economics Ranking files and return wide DataFrame."""
    print(">>> Dropping duplicates:")
    for file in files:
        year = os.path.splitext(os.path.basename(file))[0][-4:]
        df = pd.read_csv(file, index_col=1)
        df.columns = pd.MultiIndex.from_product([list(df.columns), [year]],
                                                names=['type', 'year'])
        dups = df.index.duplicated()
        if dups.sum():
            print(f"... {dups.sum()} from {year}")
            print('; '.join(df[dups].reset_index()['University'].tolist()))
        df = df[~dups]
        try:
            out = out.merge(df, "outer", left_index=True, right_index=True)
        except NameError:
            out = df.copy()
    return out


def save_melted(df, fname):
    """Melt df and save."""
    df = (df.reset_index()
            .melt(id_vars='University', value_vars=['Rank', 'Score'])
            .dropna()
            .sort_values(['University', 'year'])
            .set_index(['University', 'year', 'type'])
            .unstack()
            .reset_index())
    df.columns = [' '.join(col).strip().split()[-1] for col in df.columns.values]
    df['year'] = df['year'].astype(int)
    df.to_csv(fname, index=False)


def main():
    for folder in list(os.walk(SOURCE_FOLDER))[0][1]:
        files = sorted(glob(f"{SOURCE_FOLDER}{folder}/*.csv"))

        df = read_dataframes(files)

        # Non-interpolated version
        save_melted(df, fname=f"{TARGET_FOLDER}{folder}.csv")

        # Interpolated version
        df = pd.concat([interpolate(df, 'Rank'), interpolate(df, 'Score')],
                       axis=1)
        save_melted(df, fname=f"{TARGET_FOLDER}{folder}_interpolated.csv")

        print(f">>> Saving ranks for {df.shape[0]:,} Economics Schools for "
              f"weighting according to {folder.replace('_', ' ')}")


if __name__ == '__main__':
    main()
