import pandas as pd
from numpy import save
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

from load_movies import load_movies

# df = pd.read_parquet(get_tidy_data_path() / 'current_race.parquet')

# numerical_columns = [
#     'number',
#     'position',
#     'points',
#     'grid',
#     'laps',
#     'Time.millis',
#     'FastestLap.rank',
#     'FastestLap.lap',
#     'FastestLap.AverageSpeed.speed'
# ]

# categorical_columns = [
#     'status',
#     'Driver.code',
#     'Driver.nationality',
#     'Constructor.constructorId',
# ]

# df = df[
#     numerical_columns + categorical_columns
# ]


# full_pipeline = ColumnTransformer(
#     [
#         ('num', StandardScaler(), numerical_columns),
#         ('cat', OneHotEncoder(), categorical_columns)
#     ]
# )

# current_prepared_array = full_pipeline.fit_transform(df)
# save(
#     get_tidy_data_path() / 'current_race_prepared.npy',
#     current_prepared_array
# )
