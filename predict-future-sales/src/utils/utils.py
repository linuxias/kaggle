import pandas as pd

def downcast(df: pd.DataFrame, verbose = True):
    start_mem = df.memory_usage().sum() / 1024**2
    for col in df.columns:
        dtype_name = df[col].dtype.name
        if dtype_name == 'object':
            pass
        elif dtype_name == 'bool':
            df[col] = df[col].astype('int8')
        elif dtype_name.startswith('int') or (df[col].round() == df[col]).all():
            df[col] = pd.to_numeric(df[col], downcast = 'integer')
        else:
            df[col] = pd.to_numeric(df[col], downcast = 'float')
    end_mem = df.memory_usage().sum() / 1024**2
    if verbose:
        print('Memory usage decreased {:5.2f}Mb to {:5.2f} Mb ({:.1f}% reduction)'.format(start_mem, end_mem, 100 * (start_mem - end_mem) / start_mem))
        
    return df