

def count_batteries_by_health(present_capacities):
    cnt={"healthy":0,"exchange":0,"failed":0}
    for capC in present_capacities:
        soh=(capC/120)*100
        if soh > 80:
            cnt["healthy"]+=1
        elif 62 <= soh <=80:
            cnt["exchange"]+=1
        else:
            cnt["failed"]+=1
      
    return cnt


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
