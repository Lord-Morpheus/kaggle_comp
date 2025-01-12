from autogluon.tabular import TabularDataset, TabularPredictor
#subsample_size = 500  # subsample subset of data for faster demo, try setting this to much larger values
train_data = TabularDataset("train_extended_32col.csv")
train_data=train_data.dropna()
train_data = train_data.drop(['id'], axis = 1)
#train_data = train_data.sample(n=subsample_size, random_state=0)
#print(train_data.head())
label = 'num_sold'
predictor = TabularPredictor(label=label, eval_metric="mean_absolute_percentage_error").fit(train_data, presets='best_quality')
print("-"*100)
print("AutoGluon infers problem type is: ", predictor.problem_type)
print("Meta Data of the features:",predictor.feature_metadata)
print("-"*100)
print(predictor.leaderboard())
print("-"*100)
print("The importance of features",predictor.feature_importance(train_data))
test_data = TabularDataset('test_extended_32col.csv')
test_data = test_data.drop(['id'], axis=1)
y_pred = predictor.predict(test_data)
import pandas as pd
# Prepare submission file
test= pd.read_csv("test.csv")
submission = pd.DataFrame({
    'id': test['id'],  # Use 'id' column from test data
    'num_sold': y_pred # Flatten predictions array to 1D
})
submission.to_csv('submision3.csv', index=False)