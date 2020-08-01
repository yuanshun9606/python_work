# 创建一个列表，其中包含要覆盖的州
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]) # 传入一个数组，被转换为集合

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set() # 使用一个集合来存储最终选择的广播台

while states_needed:
  best_station = None # 将覆盖了最多的未覆盖州的广播台存储进去
  states_covered = set() # 一个集合，包含该广播台覆盖的所有未覆盖的州
  for station, states in stations.items(): # 循环迭代每个广播台并确定它是否是最佳的广播台
    covered = states_needed & states # 计算交集
    if len(covered) > len(states_covered): # 检查该广播台的州是否比best_station多
      best_station = station # 如果多，就将best_station设置为当前广播台
      states_covered = covered

  states_needed -= states_covered # 更新states_needed
  final_stations.add(best_station) # 在for循环结束后将best_station添加到最终的广播台列表中

print(final_stations) # 打印final_stations