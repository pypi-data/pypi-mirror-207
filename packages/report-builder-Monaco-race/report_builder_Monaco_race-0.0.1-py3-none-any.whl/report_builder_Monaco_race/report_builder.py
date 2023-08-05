"""This module create and print report using pandas of Monaco 2018 racers and print report
that shows the top 15 racers and the rest after underline."""

import pandas as pd


def build_df(folder_path: str, ascending_bool: bool = True) -> pd.DataFrame:

    """This function create pandas df  of Monaco 2018 racers.
    :folder_path: str
    :return: read data from 3 files, join them in one pandas dataframe and return it
    """

    abbreviations_df = pd.read_csv(folder_path + '/abbreviations.txt', sep='_', header=None, index_col=0,
                                   names=['abbreviation', 'driver', 'car'])
    startlog_df = pd.read_fwf(folder_path + '/start.log', widths=[3, 23], header=None, index_col=0,
                              names=['abbreviation', 'start_time'])
    endlog_df = pd.read_fwf(folder_path + '/end.log', widths=[3, 23], header=None, index_col=0,
                            names=['abbreviation', 'end_time'])

    df = abbreviations_df.join(startlog_df).join(endlog_df)


    df[['start_time', 'end_time']] = df[['start_time', 'end_time']] \
        .apply(pd.to_datetime, format='%Y-%m-%d_%H:%M:%S.%f')

    df['race_time'] = (abs(df['end_time'] - df['start_time']))

    df['race_time'] = df['race_time'].astype(str).str[10:-3]
    df = df.sort_values(by=['race_time'], ascending=ascending_bool).reset_index()

    return df

def build_report(df: pd.DataFrame) -> pd.DataFrame:

    """This function create report  of Monaco 2018 racers.
    :df: pd.DataFrame
    :ascending_bool: bool = True
    :return: order pandas dataframe and return it with select columns
    """

    final_df = df[['driver', 'car', 'race_time']]
    final_df.index = final_df.index + 1
    return final_df


def print_report(df: pd.DataFrame) -> None:

    """This function print report pandas df of Monaco 2018 racers and print report
    that shows the top 15 racers and the rest after underline.
    :df: take pd.DataFrame
    :return: print report that shows the top 15 racers and the rest after underline,
    order racers by time or print statistic about one driver wich you choose"""

    if len(df) == 1:
        print(df[['driver', 'car', 'race_time']])
    else:
        print(df[['driver', 'car', 'race_time']].head(15))
        print('---------------------------------------------------------------')
        print(df[['driver', 'car', 'race_time']].tail(4).to_string(header=False))

    return None



