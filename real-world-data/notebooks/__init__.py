# File Paths 
data_filepath = '../data/'

# Computed data
computed_data_filepath = data_filepath + 'computed/'

# Merged data (data over multiple days or FIC combined with FED and AMA)
merged_data_filepath = computed_data_filepath + 'merged/'

# Minute granularity data
FIC_1minute_filepath = lambda index : data_filepath + 'raw/invocations_per_function_md.anon.d0%s.csv'    % index if index < 10 else data_filepath + 'raw/invocations_per_function_md.anon.d%s.csv'    % index
FED_1minute_filepath = lambda index : computed_data_filepath + 'FED_1min_granularity/function_durations_d%s.pkl' % index
AMA_1minute_filepath = lambda index : computed_data_filepath + 'AMA_1min_granularity/app_memory_d%s.pkl' % index 

# FIC, FED and AMA 10 minute granualrity
FIC_10minute_filepath = lambda index : computed_data_filepath + 'FIC_10min_granularity/invocations_per_function_d%s.pkl' % index
FED_10minute_filepath = lambda index : computed_data_filepath + 'FED_10min_granularity/function_durations_d%s.pkl' % index
AMA_10minute_filepath = lambda index : computed_data_filepath + 'AMA_10min_granularity/app_memory_d%s.pkl' % index

# FIC, FED and AMA 60 minute granualrity
FIC_60minute_filepath = lambda index : computed_data_filepath + 'FIC_60min_granularity/invocations_per_function_d%s.pkl' % index
FED_60minute_filepath = lambda index : computed_data_filepath + 'FED_60min_granularity/function_durations_d%s.pkl' % index
AMA_60minute_filepath = lambda index : computed_data_filepath + 'AMA_60min_granularity/app_memory_d%s.pkl' % index

FIC_1minute_12days_filepath = merged_data_filepath + 'FIC_1minute_12days.pkl'
FED_1minute_12days_filepath = merged_data_filepath + 'FED_1minute_12days.pkl'
AMA_1minute_12days_filepath = merged_data_filepath + 'AMA_1minute_12days.pkl'
FIC_FED_AMA_1minute_12days_filepath = merged_data_filepath + 'FIC_FED_AMA_1minute_12days.pkl'

FIC_10minute_12days_filepath = merged_data_filepath + 'FIC_10minute_12days.pkl'
FED_10minute_12days_filepath = merged_data_filepath + 'FED_10minute_12days.pkl'
AMA_10minute_12days_filepath = merged_data_filepath + 'AMA_10minute_12days.pkl'
FIC_FED_AMA_10minute_12days_filepath = merged_data_filepath + 'FIC_FED_AMA_10minute_12days.pkl'

FIC_60minute_12days_filepath = merged_data_filepath + 'FIC_60minute_12days.pkl'
FED_60minute_12days_filepath = merged_data_filepath + 'FED_60minute_12days.pkl'
AMA_60minute_12days_filepath = merged_data_filepath + 'AMA_60minute_12days.pkl'
FIC_FED_AMA_60minute_12days_filepath = merged_data_filepath + 'FIC_FED_AMA_60minute_12days.pkl'

FIC_10minute_7days_filepath = merged_data_filepath + 'FIC_10minute_7days.pkl'
FED_10minute_7days_filepath = merged_data_filepath + 'FED_10minute_7days.pkl'
AMA_10minute_7days_filepath = merged_data_filepath + 'AMA_10minute_7days.pkl'

FIC_60minute_7days_filepath = merged_data_filepath + 'FIC_60minute_7days.pkl'

FIC_FED_AMA_10minute_7days_filepath = merged_data_filepath + 'FIC_FED_AMA_10minute_7days.pkl'
FIC_FED_AMA_60minute_7days_filepath = merged_data_filepath + 'FIC_FED_AMA_60minute_7days.pkl'

FIC_1minute_7days_9clusters_filepath  = computed_data_filepath + 'FIC_10minute_7days_9clusters.pkl'
FIC_10minute_7days_9clusters_filepath = computed_data_filepath + 'FIC_10minute_7days_9clusters.pkl'
FIC_60minute_7days_9clusters_filepath = computed_data_filepath + 'FIC_60minute_7days_9clusters.pkl'

FIC_150minute_filepath = lambda index : computed_data_filepath + 'FIC_150min_granularity/invocations_per_function_d%s.pkl' % index
FIC_150minute_7days_filepath = merged_data_filepath + 'FIC_150minute_7days.pkl'
