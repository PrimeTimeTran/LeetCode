from collections import deque


class Solution:
  def minMoves(self, classroom: List[str], energy: int) -> int:
    rows = len(classroom)
    cols = len(classroom[0])
    start = None
    litter = {}

    for r in range(rows):
      for c in range(cols):
        cell = classroom[r][c]

        if cell == "S":
          start = (r, c)
        elif cell == "L":
          litter[(r, c)] = len(litter)

    # Bitmask representing all litter collected.
    target = (1 << len(litter)) - 1

    # (row, col, remaining_energy, litter_mask, moves)
    queue = deque([(start[0], start[1], energy, 0, 0)])

    # For each (row, col, mask), remember the most energy
    # we've had when reaching that state.
    best_energy = {(start[0], start[1], 0): energy}

    directions = (
      (1, 0),
      (-1, 0),
      (0, 1),
      (0, -1),
    )

    while queue:
      r, c, current_energy, mask, moves = queue.popleft()

      if mask == target:
        return moves

      if current_energy == 0:
        continue

      for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if not (0 <= nr < rows and 0 <= nc < cols):
          continue

        cell = classroom[nr][nc]

        if cell == "X":
          continue

        new_energy = current_energy - 1
        new_mask = mask

        # Collect litter.
        if (nr, nc) in litter:
          new_mask |= 1 << litter[(nr, nc)]

        # Reset energy after entering R.
        if cell == "R":
          new_energy = energy

        state = (nr, nc, new_mask)

        # If we've already reached this position with the
        # same litter collected and >= energy, this state
        # can never be better.
        if new_energy <= best_energy.get(state, -1):
          continue

        best_energy[state] = new_energy

        queue.append(
          (
            nr,
            nc,
            new_energy,
            new_mask,
            moves + 1,
          )
        )
    return -1