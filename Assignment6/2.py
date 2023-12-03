import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor

# 示例GDP数据（通常需要更详细的数据集）
data = {
    'Year': [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017],
    'GDP': [137422, 161840.2, 187318.9, 219438.5, 270092.3, 319244.6, 348517.7, 412119.3, 487940.2, 538580, 592963.2, 643563.1, 688858.2, 746395.1, 832035.9]
}
df = pd.DataFrame(data)

# 特征和标签
X = df[['Year']]
y = df['GDP']

# 因为数据量小，这里就不划分训练集和测试集了，但在实际操作中建议划分。
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 初始化模型
xgb_model = XGBRegressor(objective='reg:squarederror', n_estimators=100)

# 训练模型
xgb_model.fit(X, y)

# 进行评估
y_pred = xgb_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"The mean squared error (MSE) on test set: {mse}")

# 预测未来GDP
future_years = np.array([2018, 2019, 2020, 2021, 2022]).reshape(-1,1)
future_GDP = xgb_model.predict(future_years)

print("Predictions for GDP from 2023 to 2027:")
for year, gdp in zip(future_years.ravel(), future_GDP):
    print(f"Year {year}: {gdp:.2f}")