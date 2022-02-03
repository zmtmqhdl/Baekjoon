n, m = map(int, input().split()) # �� ����
start_B = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']] # �� ���� �� ĭ�� B�� ���� ���� �Ǵ� ��츦 ǥ���� start_B��� list����
start_W = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']] # �� ���� �� ĭ�� W�� ���� ���� �Ǵ� ��츦 ǥ���� start_W��� list����
data = [] # data��� list����
for _ in range(n) : # �ݺ��� for -> n�� �ݺ�
    line = list(input()) # ���Ե� ���� ���ҷ� ���� line�̶�� list����
    data.append(line) # append�� ����Ͽ� data�� line�� ���ҷ� ����
result = 64 # 8 * 8�� ũ�⸦ ���� ü�����̹Ƿ� ��� ĭ�� �����Ѵٰ� ������ ���� �ִ밪�� ���� result���� ����
for i in range(n - 7) : # �ݺ��� for -> 0���� n - 8���� i�� ���ʴ�� �����ϸ� �ݺ�
                        # 8ĭ�� �߶� ����ϹǷ� n - 7
    for j in range(m - 7) : # �ݺ��� for -> 0���� n - 8���� j�� ���ʴ�� �����ϸ� �ݺ�
                            # 8ĭ�� �߶� ����ϹǷ� m - 7
        start_B_count = 0 # �� ���� �� ĭ�� B�� �������� �� �����ؾ��ϴ� ĭ�� ����ϴ� start_B_count���� ����
        start_W_count = 0 # �� ���� �� ĭ�� W�� �������� �� �����ؾ��ϴ� ĭ�� ����ϴ� start_W_count���� ����
        for a in range(8) : # �ݺ��� for -> 0���� 7���� a�� ������� �����ϸ� �ݺ�
                            # 8 * 8 ũ���� ü������ �����ϴ� ����
            for b in range(8) : # �ݺ��� for -> 0���� 7���� b�� ���ʴ�� �����ϸ� �ݺ� 
                                # 8 * 8 ũ���� ü������ �����ϴ� ����
                if data[i + a][j + b] != start_B[a][b] : # ���ǹ� if -> �� ���� �� ĭ�� B�� �������� ���� ����
                    start_B_count += 1 # start_B_count = start_B_count + 1
                if data[i + a][j + b] != start_W[a][b] : # ���ǹ� if -> �� ���� �� ĭ�� W�� �������� ���� ����
                    start_W_count += 1 # start_W_count = start_W_count + 1
        result = min(result, start_B_count, start_W_count) # min�� ����Ͽ� result, start_B_count, start_W_count�߿��� ���� ���� ���� result�� ����
print(result) # ���