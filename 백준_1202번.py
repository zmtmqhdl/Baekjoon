import heapq # ���̺귯�� ȣ��
import sys # ���̺귯�� ȣ��
n, k = map(int, sys.stdin.readline().split()) # �� ����
gem = [] # ���� ������ ������ gem�̶�� list����
bag = [] # ���� ������ ������ bag�̶�� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    m, v = map(int, sys.stdin.readline().split()) # �� ����
    heapq.heappush(gem, [m, v]) # heappush�� ����Ͽ� gem�̶�� list�� [m, v]�� ���ҷ� �����ϰ� ����
for _ in range(k) : # �ݺ��� for -> k��ŭ �ݺ�
    c = int(sys.stdin.readline()) # �� ����
    heapq.heappush(bag, c) # heappush�� ����Ͽ� bag�̶�� list�� c�� ���ҷ� �����ϰ� ����
result = 0 # ������� ������ result���� �ʱ�ȭ
select_gem = [] # ������ ���Ժ��� ���� �������� ������ ������ select_gem�̶�� list����
for _ in range(k) : # �ݺ��� for -> k��ŭ �ݺ�
    select_bag = heapq.heappop(bag) # heappop�� �̿��Ͽ� bag�̶�� list���� ���� ���� ���� ���� �� �� ���� select_bag�� ����
    while gem and select_bag >= gem[0][0] : # �ݺ��� while -> gem�̶�� list�� ���Ұ� 1�� �̻� �ְ� select_bag�� ���� gem�� ���Ժ��� ���ų� ū ��� �ݺ�
        [m, v] = heapq.heappop(gem) # heappop�� �̿��Ͽ� gem�̶�� list���� ���� ���� ���� ���� �� �� ���� [m, v]�� ����
        heapq.heappush(select_gem, -v) # heappush�� �̿��Ͽ� select_gem�̶�� list�� -v���� ���� -> max heap
    if select_gem : # ���ǹ� if, elif -> select_gem�̶�� list�� ���Ұ� 1�� �̻��� ���
        result -= heapq.heappop(select_gem) # result = result - (select_gem�̶�� list���� ���� ū �� -> ���� ����)
    elif not gem : # gem�̶�� list�� ���Ұ� ���� ���
        break # ����
print(result) # ���