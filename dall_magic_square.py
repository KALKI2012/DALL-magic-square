def generate_dall_magic_square(D):
    """
    生成 D×D 的 DALL 幻方（D 为奇数）
    返回二维列表
    """
    if D % 2 == 0:
        raise ValueError("D 必须是奇数")

    # 对于 D=3，直接返回洛书的标准排列
    if D == 3:
        return [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

    # 初始化全零矩阵
    square = [[0] * D for _ in range(D)]

    # 起始位置：第一行中间（与您提供的代码一致）
    row, col = 0, D // 2
    num = 1
    square[row][col] = num

    # 定义 φ(k) 跳跃值表
    phi_table = {
        1: [D + 1],
        2: [D + 2, 2 * D + 2],
        3: [D + 3, 2 * D + 3, 3 * D + 3]
    }

    # 记录每个 k 层级当前使用的跳跃索引
    phi_index = {1: 0, 2: 0, 3: 0}

    for num in range(1, D * D):
        # 决定步长
        if num % D != 0:
            step = 1
        else:
            k = num // D
            key = 3 if k >= 4 else k
            seq = phi_table[key]
            idx = phi_index[key] % len(seq)
            step = seq[idx]
            phi_index[key] = (phi_index[key] + 1) % len(seq)

        # 方向：右上（行减，列加）
        new_row = (row - step) % D
        new_col = (col + step) % D

        # 如果目标位置已被占用，改为向下移动一格
        if square[new_row][new_col] != 0:
            new_row = (row + 1) % D
            new_col = col

        row, col = new_row, new_col
        num += 1
        square[row][col] = num

    return square

def verify_magic_square(square):
    D = len(square)
    expected_sum = D * (D*D + 1) // 2
    
    print("幻方矩阵：")
    for row in square:
        print(row)
    
    print(f"\n预期和值: {expected_sum}")
    
    # 检查每行
    print("\n行和：")
    for i, row in enumerate(square):
        row_sum = sum(row)
        print(f"第 {i+1} 行: {row_sum} {'✓' if row_sum == expected_sum else '✗'}")
    
    # 检查每列
    print("\n列和：")
    for j in range(D):
        col_sum = sum(row[j] for row in square)
        print(f"第 {j+1} 列: {col_sum} {'✓' if col_sum == expected_sum else '✗'}")
    
    # 检查主对角线
    main_diag_sum = sum(square[i][i] for i in range(D))
    print(f"\n主对角线和: {main_diag_sum} {'✓' if main_diag_sum == expected_sum else '✗'}")
    
    # 检查副对角线
    anti_diag_sum = sum(square[i][D-1-i] for i in range(D))
    print(f"副对角线和: {anti_diag_sum} {'✓' if anti_diag_sum == expected_sum else '✗'}")

# 测试示例
if __name__ == "__main__":
    # 测试 D=3
    print("=== D=3 ===")
    magic_square_3 = generate_dall_magic_square(3)
    verify_magic_square(magic_square_3)
    
    # 测试 D=5
    print("\n=== D=5 ===")
    magic_square_5 = generate_dall_magic_square(5)
    verify_magic_square(magic_square_5)
    
    # 测试 D=7
    print("\n=== D=7 ===")
    magic_square_7 = generate_dall_magic_square(7)
    verify_magic_square(magic_square_7)