n = int(input()) # �� ����
score = 0 # ������ ������ score���� �ʱ�ȭ
slime = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� slime�̶�� list����
slime.sort(reverse = True) # sort(reverse = True)�� ����Ͽ� slime�̶�� list�� ���Ҹ� ������������ ����
while len(slime) != 1 : # �ݺ��� while -> len�� ����Ͽ� ���� slime�̶�� list�� ������ ������ 1���� �ƴ� ��� �ݺ�
    slime.insert(0, slime[0] + slime[1]) # insert�� ����Ͽ� 0��° index�� slime[0] + slime[1]�� ���� ���� 
    score += (slime[1] * slime[2]) # score = score + (slime[1] + slime[2])
    del slime[1] # del�� ����Ͽ� slime�̶�� list���� 1��° index���� ����
    del slime[1] # del�� ����Ͽ� slime�̶�� list���� 1��° index���� ����
print(score) # ���