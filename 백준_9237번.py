n = int(input()) # �� ����
tree = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� tree��� list����
tree.sort(reverse = True) # sort(reverse = True)�� ����Ͽ� tree��� list�� ���Ҹ� ������������ ����
for i in range(len(tree)) : # �ݺ��� for -> 0���� len(tree) - 1���� i�� ���ʴ�� �����ϸ� �ݺ�
    tree[i] = tree[i] + i + 1 # ������ �� �ڶ�µ� �ɸ��� �ð� ����
print(max(tree) + 1) # ������� ������ ���� ������ max(tree) + 1�� �����Ͽ� ���