import pandas as pd

def print_test():
    print('hello world!')

class DataLoader():
    
    def __init__(self, 
                 time_index_col,
                 keep_cols, 
                 join_dfs= True):
        
        self.keep_cols = keep_cols
        self.time_index_col = time_index_col

    def guess_format(self, path_file):
        return path_file.split('.')[-1].lower()
        
    def load_dataset(self,path_files):

        self.tablefreq = pd.DataFrame()

        dataset = pd.DataFrame()
        assert isinstance(path_files, dict),'path_file must be dictionary which keys are tags and values are file paths'

        for i, (tag, path) in enumerate(path_files.items()):
            if i ==0:
                df_ = self.file_read(path,self.guess_format(path))
                df_ = df_[self.keep_cols]
                self.tablefreq = self.raw_database_tablefreq(df_).add_prefix(tag+ '_')
                df_ = df_.add_prefix(tag+ '_')
                dataset = df_.copy()
            else:
                df_ = self.file_read(path,self.guess_format(path))
                df_ = df_[self.keep_cols]
                self.tablefreq = pd.merge(self.tablefreq,
                                          self.raw_database_tablefreq(df_).add_prefix(tag+ '_'),
                                          left_index= True,
                                          right_index=True,
                                          how='outer')
                df_ = df_.add_prefix(tag+ '_')
                dataset = dataset.merge(df_, right_index=True, left_index=True,)
                
        return dataset

    def file_read(self, path_file, format) -> pd.DataFrame:
        assert format in ['parquet', 'csv', 'excel'], 'Format must be "parquet", "csv", "xlsx"'

        if format =='parquet':
            df = pd.read_parquet(path_file, engine='pyarrow')
            df[self.time_index_col] = pd.to_datetime(df[self.time_index_col])
            df.set_index(self.time_index_col, inplace=True)
        return df

    def raw_database_tablefreq(self, df):
        tablefreq = df.copy()
        tablefreq['date'] = tablefreq.index.date
        tablefreq['time'] = tablefreq.index.time
        tablefreq = tablefreq.groupby('date').agg({'time':['min', 'max','count']})
        return tablefreq



        
