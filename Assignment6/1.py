import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# 假定你已经有一个包含过去10年GDP数据的CSV文件
# 格式: 第一列为日期 (年份), 第二列为GDP值
# 例如:
# Year,GDP
# 2001,130000
# 2002,140000
# ...
# 2010,220000

# 读取数据
df = pd.read_csv('gdp.csv', index_col='Year', parse_dates=True)

# 使用ARIMA模型进行拟合。参数(p,d,q)需要根据数据来确定
# 这里，我们为了演示目的随意选取了(1,1,1)
# 在实际操作中，应该使用ACF和PACF图来帮助确定这些参数
model = ARIMA(df['GDP'], order=(1, 1, 0))  # 这里的参数可能需要调整
model_fit = model.fit()

# 一旦模型拟合完成，我们就可以预测接下来一年的GDP
forecast = model_fit.forecast(steps=1)  # steps=1 代表预测未来1个时间步长，即1年
print(forecast)

# 可视化结果
df['GDP'].plot(label='Actual GDP')
forecast.plot(label='Forecasted GDP', style='--')
plt.legend()
plt.title('China Annual GDP Forecast')
plt.xlabel('Year')
plt.ylabel('GDP')
plt.show()