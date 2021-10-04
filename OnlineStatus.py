statuses = {
"Alice": "online",
"Bob": "offline",
"Eve": "online",
}

amount = 0

for t in statuses:
  if statuses[t] == "online":
    amount = amount + 1
print("Online", amount)
