import pandas as pd


def data_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function defined to return details
    about the number of rows and columns and the column data type
    frequency of the passed pandas DataFrame

    Parameters
    ----------
    df - the data frame to get the details of

    Returns
    -------
    Specified details of input data frame
    """

    def _shape(_df: pd.DataFrame) -> pd.DataFrame:
        """
        Function defined to return a dataframe with details about
        the number of row and columns
        """
        row, col = _df.shape
        return pd.DataFrame(data=[[row], [col]], columns=['Values'], index=['Number of rows', 'Number of columns'])

    def _dtypes_freq(_df: pd.DataFrame) -> pd.DataFrame:
        """
        Function defined to return a dataframe with details about
        the pandas dtypes frequency
        """
        counter, types = {}, _df.dtypes
        for data_type in types:
            tmp = str(data_type)
            if tmp in counter.keys():
                counter[tmp] += 1
            else:
                counter[tmp] = 1

        values = [[value] for value in counter.values()]
        return pd.DataFrame(data=values, columns=['Values'], index=list(counter.keys()))

    result_df = pd.concat([_shape(df), _dtypes_freq(df)])
    return result_df


def display_summary(_df: pd.DataFrame) -> None:
    """
    Function define to print out the result of the data summary

    Parameters
    ----------
    _df

    Returns
    -------

    """
    result_df = data_summary(_df)
    message = "---- Data summary ----"
    print(message, result_df, sep='\n')
    return
