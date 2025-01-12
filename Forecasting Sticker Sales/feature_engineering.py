import pandas as pd

df = pd.read_csv('train.csv')

# Step 1: Create pair columns
df['country_product'] = df['country'] + '_' + df['product']
df['store_product'] = df['store'] + '_' + df['product']
df['country_store'] = df['country'] + '_' + df['store']


# Step 2: Calculate target statistics for each category
# For (country, product)
country_product_stats = df.groupby('country_product')['num_sold'].agg(['mean', 'median', 'min', 'max']).rename(
    columns={'mean': 'TE_mean', 'median': 'TE_median', 'min': 'TE_min', 'max': 'TE_max'}
)
# For (store, product)
store_product_stats = df.groupby('store_product')['num_sold'].agg(['mean', 'median', 'min', 'max']).rename(
    columns={'mean': 'TE_mean', 'median': 'TE_median', 'min': 'TE_min', 'max': 'TE_max'}
)
# For (country)
country_stats = df.groupby('country')['num_sold'].agg(['mean', 'median', 'min', 'max']).rename(
    columns={'mean': 'TE_mean', 'median': 'TE_median', 'min': 'TE_min', 'max': 'TE_max'}
)
# For (country,store)
country_store_stats = df.groupby('country_store')['num_sold'].agg(['mean', 'median', 'min', 'max']).rename(
    columns={'mean': 'TE_mean', 'median': 'TE_median', 'min': 'TE_min', 'max': 'TE_max'}
)
#for (product)
product_stats = df.groupby('product')['num_sold'].agg(['mean', 'median', 'min', 'max']).rename(
    columns={'mean': 'TE_mean', 'median': 'TE_median', 'min': 'TE_min', 'max': 'TE_max'}
)
#for (store)
store_stats = df.groupby('store')['num_sold'].agg(['mean', 'median', 'min', 'max']).rename(
    columns={'mean': 'TE_mean', 'median': 'TE_median', 'min': 'TE_min', 'max': 'TE_max'}
)


# Step 3: Map the statistics back to the DataFrame
df['country_product_TE_mean'] = df['country_product'].map(country_product_stats['TE_mean'])
df['country_product_TE_median'] = df['country_product'].map(country_product_stats['TE_median'])
df['country_product_TE_min'] = df['country_product'].map(country_product_stats['TE_min'])
df['country_product_TE_max'] = df['country_product'].map(country_product_stats['TE_max'])

df['store_product_TE_mean'] = df['store_product'].map(store_product_stats['TE_mean'])
df['store_product_TE_median'] = df['store_product'].map(store_product_stats['TE_median'])
df['store_product_TE_min'] = df['store_product'].map(store_product_stats['TE_min'])
df['store_product_TE_max'] = df['store_product'].map(store_product_stats['TE_max'])

df['country_TE_mean'] = df['country'].map(country_stats['TE_mean'])
df['country_TE_median'] = df['country'].map(country_stats['TE_median'])
df['country_TE_min'] = df['country'].map(country_stats['TE_min'])
df['country_TE_max'] = df['country'].map(country_stats['TE_max'])

df['country_store_TE_mean'] = df['country_store'].map(country_store_stats['TE_mean'])
df['country_store_TE_median'] = df['country_store'].map(country_store_stats['TE_median'])
df['country_store_TE_min'] = df['country_store'].map(country_store_stats['TE_min'])
df['country_store_TE_max'] = df['country_store'].map(country_store_stats['TE_max'])

df['product_TE_mean'] = df['product'].map(product_stats['TE_mean'])
df['product_TE_median'] = df['product'].map(product_stats['TE_median'])
df['product_TE_min'] = df['product'].map(product_stats['TE_min'])
df['product_TE_max'] = df['product'].map(product_stats['TE_max'])

df['store_TE_mean'] = df['store'].map(store_stats['TE_mean'])
df['store_TE_median'] = df['store'].map(store_stats['TE_median'])
df['store_TE_min'] = df['store'].map(store_stats['TE_min'])
df['store_TE_max'] = df['store'].map(store_stats['TE_max'])


### NOW SAME THING FOR THE TEST FILE
test = pd.read_csv('test.csv')

test['country_product'] = test['country'] + '_' + test['product']
test['store_product'] = test['store'] + '_' + test['product']
test['country_store'] = test['country'] + '_' + test['store']

test['country_product_TE_mean'] = test['country_product'].map(country_product_stats['TE_mean'])
test['country_product_TE_median'] = test['country_product'].map(country_product_stats['TE_median'])
test['country_product_TE_min'] = test['country_product'].map(country_product_stats['TE_min'])
test['country_product_TE_max'] = test['country_product'].map(country_product_stats['TE_max'])

test['store_product_TE_mean'] = test['store_product'].map(store_product_stats['TE_mean'])
test['store_product_TE_median'] = test['store_product'].map(store_product_stats['TE_median'])
test['store_product_TE_min'] = test['store_product'].map(store_product_stats['TE_min'])
test['store_product_TE_max'] = test['store_product'].map(store_product_stats['TE_max'])

test['country_TE_mean'] = test['country'].map(country_stats['TE_mean'])
test['country_TE_median'] = test['country'].map(country_stats['TE_median'])
test['country_TE_min'] = test['country'].map(country_stats['TE_min'])
test['country_TE_max'] = test['country'].map(country_stats['TE_max'])

test['country_store_TE_mean'] = test['country_store'].map(country_store_stats['TE_mean'])
test['country_store_TE_median'] = test['country_store'].map(country_store_stats['TE_median'])
test['country_store_TE_min'] = test['country_store'].map(country_store_stats['TE_min'])
test['country_store_TE_max'] = test['country_store'].map(country_store_stats['TE_max'])

test['product_TE_mean'] = test['product'].map(product_stats['TE_mean'])
test['product_TE_median'] = test['product'].map(product_stats['TE_median'])
test['product_TE_min'] = test['product'].map(product_stats['TE_min'])
test['product_TE_max'] = test['product'].map(product_stats['TE_max'])

test['store_TE_mean'] = test['store'].map(store_stats['TE_mean'])
test['store_TE_median'] = test['store'].map(store_stats['TE_median'])
test['store_TE_min'] = test['store'].map(store_stats['TE_min'])
test['store_TE_max'] = test['store'].map(store_stats['TE_max'])


df.to_csv("train_extended_32col.csv", index=False)
test.to_csv("test_extended_32col.csv", index = False)