import pyupbit

access = "HWhgcJ7zH8LP2ONoUHyaBNK3bZH1i0IPOpQoFMx3"          # 본인 값으로 변경
secret = "ktHyiOu7j5hABWBWofwTBnOosxyFjzyb9hEcxBdx"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

#test
