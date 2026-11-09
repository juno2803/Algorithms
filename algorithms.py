from collections import deque

def shortestPathAllKeys(grid):
    m, n = len(grid), len(grid[0])

    start = None
    total_keys = 0

    # 시작점과 열쇠 개수 확인
    for r in range(m):
        for c in range(n):
            if grid[r][c] == '@':
                start = (r, c)

            if 'a' <= grid[r][c] <= 'f':
                total_keys += 1

    # 모든 열쇠를 획득한 상태
    target = (1 << total_keys) - 1

    # BFS 초기화
    queue = deque([(start[0], start[1], 0, 0)])
    visited = set()
    visited.add((start[0], start[1], 0))

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        r, c, mask, dist = queue.popleft()

        # 모든 열쇠를 획득하고 목표 지점에 도착
        if mask == target and grid[r][c] == 'G':
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # 격자 범위 확인
            if not (0 <= nr < m and 0 <= nc < n):
                continue

            cell = grid[nr][nc]

            # 벽 확인
            if cell == '#':
                continue

            # 자물쇠 확인
            if 'A' <= cell <= 'F':
                bit = 1 << (ord(cell) - ord('A'))

                if not (mask & bit):
                    continue

            # 열쇠 획득
            new_mask = mask

            if 'a' <= cell <= 'f':
                bit = 1 << (ord(cell) - ord('a'))
                new_mask |= bit

            # 방문 여부 확인
            state = (nr, nc, new_mask)

            if state in visited:
                continue

            visited.add(state)
            queue.append((nr, nc, new_mask, dist + 1))

    return -1