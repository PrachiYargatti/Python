# 7.ATM Cash Dispencing Machine

def dispense_cash(amount):
  if amount % 500 != 0:
    print("Amount should be multiple of 500.")
    return

  notes_2000 = amount // 2000 # max Rs.2000 notes
  remaining = amount % 2000 # remaining amount after Rs.2000 notes
  notes_500 = remaining // 500 # Rs.500 notes for remaining amount

  print(f"Rs.2000 notes: {notes_2000}")
  print(f"Rs.500 notes: {notes_500}")

amount = int(input("Enter the amount: "))
dispense_cash(amount)
