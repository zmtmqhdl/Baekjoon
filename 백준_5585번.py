n = 1000 - int(input()) # �� ���� -> ������ ���� 1000�� �����̹Ƿ� 1000 - int(input())
count = 0 # ������ ������ ������ count���� �ʱ�ȭ
coin = [500, 100, 50, 10, 5, 1] # ������ ������ ���ҷ� ���� coin�̶�� list����
for i in coin : # �ݺ��� for -> coin�� ���Ҹ� i�� ���ʴ�� �����ϸ� �ݺ�
    count += n // i # count = count + (n // i)
    n %= i # n = n % i
print(count) # ���