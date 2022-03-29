import heapq # ���̺귯�� ȣ��
n = int(input()) # �� ����
data = [] # data��� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    heapq.heappush(data, int(input())) # heappush�� ����Ͽ� data��� list�� ���Ե� ���� ���ҷ� �߰��ϸ鼭 ����
if len(data) == 1 : # ���ǹ� if, else -> ī�� ������ 1���� ���
    print(0) # ���
else : # ī�� ������ ���� ���� ���
    result = 0 # ������� ������ result���� �ʱ�ȭ
    while len(data) > 1 : # �ݺ��� while -> ī�� ������ 2�� �̻��� ���
        min1 = heapq.heappop(data) # heappop�� �̿��Ͽ� data��� list���� ���� ���� ���� min1���� �����ϰ� ����
        min2 = heapq.heappop(data) # heappop�� �̿��Ͽ� data��� list���� ���� ���� ���� min2���� �����ϰ� ����
        result += min1 + min2 # result = result + (min1 + min2)
        heapq.heappush(data, min1 + min2) # heappush�� �̿��Ͽ� data��� list�� min1 + min2�� ���� ���ҷ� �߰��ϸ鼭 ���Ĥ�
    print(result) # ���