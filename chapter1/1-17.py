# 从字典中提取子集

prices = {
  'ACME': 45.23,
  'AAPL': 612.78,
  'IBM': 205.55,
  'HPQ': 37.20,
  'FB': 10.75
}

sub_prices = {key: value for key, value in prices.items() if value > 100}

print('prices sub: ', sub_prices)

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
# 将tech_names中包含的prices中的键提取成prices的子字典
sub_tech_names = { key: value for key, value in prices.items() if key in tech_names }
print('sub_tech_names: ', sub_tech_names)