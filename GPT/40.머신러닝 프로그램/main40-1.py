# 필요한 라이브러리 불러오기
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 데이터 불러오기
iris = load_iris()
X = iris.data
y = iris.target

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 랜덤 포레스트 분류기 생성
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# 모델 학습
rf_classifier.fit(X_train, y_train)

# 테스트 데이터로 예측
y_pred = rf_classifier.predict(X_test)

# 정확도 출력
print("정확도:", accuracy_score(y_test, y_pred))
