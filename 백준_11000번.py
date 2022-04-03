import heapq # ���̺귯�� ȣ��
import sys
n = int(sys.stdin.readline()) # �� ����
data = [] # data��� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    s, t = map(int, sys.stdin.readline().split()) # �� ����
    data.append([s, t]) # append�� ����Ͽ� data��� list�� [s, t]�� ���ҷ� ����
data.sort() # sort�� ����Ͽ� data��� list�� ���Ҹ� ������������ ����
room = [] # room�̶�� list����
heapq.heappush(room, data[0][1]) # heqppush�� ����Ͽ� room�̶�� list�� data[0][1]�� ���ҷ� ����
for i in range(1, n) : # �ݺ��� for -> 1���� n - 1���� i�� ���ʴ�� ����
    if data[i][0] < room[0] : # ���ǹ� if, else -> ���� ȸ�ǽ� ������ �ð����� ���� ȸ�� ���۽ð��� ���� ���
        heapq.heappush(room, data[i][1]) # heappush�� ����Ͽ� data[i][1]�� ���� room�̶�� list�� ���� -> ���ο� ȸ�ǽ� ����
    else : # ���� ȸ�ǰ� ������ �̾ ȸ�ǰ� ���� ������ ���
        heapq.heappop(room) # heappop�� ����Ͽ� room�̶�� list���� ���� ���� ���Ұ� ����
        heapq.heappush(room, data[i][1]) # heappush�� ����Ͽ� data[i][1]�� ���Ҹ� room�̶�� list�� ����
print(len(room)) # room�̶�� list�� ���� ���� ���