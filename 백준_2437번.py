n = int(input()) # �� ����
data = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� data��� list����
data.sort() # sort�� ����Ͽ� data��� list�� ���Ҹ� ������������ ����
kg = 1 # ������ �ּڰ��� ������ kg���� ���� -> �� ���Ը� ���ذ��� i�� �տ� �ִ� �� ������ �պ��� i�� ���԰� ũ�� �� ������ ������ ǥ���� ���� ����
for i in data : # �ݺ��� for -> data��� ���Ҹ� i�� ���ʴ�� �����ϸ� �ݺ�
    if kg < i : # ���ǹ� if -> 
        break # ����
    kg += i # kg = kg + i
print(kg) # ���