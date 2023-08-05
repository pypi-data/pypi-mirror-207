"""This module create report using CLI of Monaco 2018 racers and print report
that shows the top 15 racers and the rest after underline."""

import argparse
from .report_builder import build_report, print_report, build_df
from typing import Any


def parse_arguments() -> argparse.Namespace:
    """ This function help to get attributes using CLI
    :return: arguments from command-line interface such as --files : folder_path,
    [--asc | --desc]  shows list of drivers and optional order (default order is asc)
    --driver shows statistic about driver
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('--files', help='folder_path')
    parser.add_argument('--asc', default=True, type=bool,
                        help='shows list of drivers and optional order (default order is asc)')
    parser.add_argument('--desc', default=False, type=bool,
                        help='shows list of drivers and optional order (default order is asc)')
    parser.add_argument('--driver', help='shows statistic about driver')

    args = parser.parse_args()

    return args


def cli_report_builder() -> Any:
    """This function create report using CLI of Monaco 2018 racers and print report
    that shows the top 15 racers and the rest after underline.
    :return: print report that shows the top 15 racers and the rest after underline,
    order racers by time or print statistic about one driver wich you choose using cli
    """

    try:
        args = parse_arguments()
    except:
        raise AttributeError('Check your arguments!')


    if not args.files:
        raise FileNotFoundError('Need folder path!')
    elif args.files:

        try:
            if args.driver:
                df = build_report(build_df(args.files, False if args.desc else True))
                driver_df = df[df.driver == args.driver]
                if len(driver_df):
                    return print_report(df[df.driver == args.driver])
                else:
                    raise AttributeError('Check driver name!')
            else:
                return print_report(build_report(build_df(args.files, False if args.desc else True)))
        except FileNotFoundError:
            raise FileNotFoundError('Check your folder path!')

