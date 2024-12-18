def kirill_gardener():
  # Reading input
  N = int(input())  
  arr = list(map(int, input().split()))
      
  # Check if the length of the list matches N
  if len(arr) != N:
    raise ValueError(f"Expected {N} flowers, but got {len(arr)}")

  v = []
  for i in range(N):
    v.append((arr[i], i))
    
    # Sort by the flower type
  v.sort()
    
    # Arrays to hold unique values and ranges for each type
  u = []
  rl = []
  u.append(v[0][0])
  rl.append((v[0][1], v[0][1]))
    
  for i in range(1, N):
    if v[i][0] != u[-1]:
      u.append(v[i][0])
      rl.append((v[i][1], v[i][1]))
    else:
      rl[-1] = (rl[-1][0], v[i][1])

    # Variables for dynamic programming to hold previous and current states
  Ln, Rn = 0, 0
  Cr, Cl = 0, 0

  for i in range(len(u)):
    Crp, Clp = Cr, Cl
    Lp, Rp = Ln, Rn
    Rn = rl[i][1]
    Ln = rl[i][0]
    Cr = Rn - Ln + min(Crp + abs(Rp - Ln), Clp + abs(Lp - Ln))
    Cl = Rn - Ln + min(Crp + abs(Rp - Rn), Clp + abs(Lp - Rn))
    
  print(N + min(Cr, Cl))

if __name__ == "__main__":
  kirill_gardener()