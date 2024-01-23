import pyupbit
import numpy as np

#  ohlcv (open, high, low, close, volume)로 당일 시가, 고가, 저가, 종가, 거래에 대한 데이터
df = pyupbit.get_ohlcv("KRW-BTC",count=30)

# 변동성 돌파 기준 범위 계산, (고가 - 저가) * k값
df['range'] = (df['high'] - df['low']) * 0.5

# range 컬럼을 한칸식 밑으로 내림 (.shift(1))
df['target'] = df['open'] + df['range'].shift(1)

# np.where (조건문, 참일때 값, 거짓일때 값)
fee = 0.0032
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)

# 누적 곱 계산(cumprod) => 누적 수익률
df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")