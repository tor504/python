# 필요한 라이브러리 불러오기
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 예제 데이터 생성
np.random.seed(0)
X = 2 * np.random.rand(100, 1)  # 0~2 사이의 난수 생성
y = 4 + 3 * X + np.random.randn(100, 1)  # y = 4 + 3x + 노이즈

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 선형 회귀 모델 생성
lin_reg = LinearRegression()

# 모델 학습
lin_reg.fit(X_train, y_train)

# 학습 결과 출력
print("회귀 계수 (기울기):", lin_reg.coef_)
print("절편:", lin_reg.intercept_)

# 테스트 데이터에 대한 예측
y_pred = lin_reg.predict(X_test)

# 성능 평가
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("평균 제곱 오차(MSE):", mse)
print("결정 계수(R^2):", r2)
