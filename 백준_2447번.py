n = int(input()) # �� ����
data = [] # data��� list����
          # �� ����� ������ list
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ� :
    data.append(["*" for _ in range(n)]) # append�� ����Ͽ� *�� n��ŭ data��� list�� ����
                                         # n * n ���·� *�� ���� 2���� �迭
divide = n # divide���� n���� �ʱ�ȭ 
count = 0 # n�� 3�� �� �ŵ��������� �ľ��ϱ� ���� count���� ����
while divide != 1 : # �ݺ��� while -> n�� 3�� �� �ŵ��������� ����
    divide /= 3 # divde = divide / 3
    count += 1 # count = count + 1
for n in range(count) : # �ݺ��� for -> 0���� count - 1���� n�� ���ʴ�� �����ϸ� �ݺ�
    blank = [i for i in range(n) if (i // (3 ** n)) % 3 == 1] # blank��� list���� -> ������ ��ǥ�� ���ϴ� ����
    for i in blank : # �ݺ��� for -> blank��� list�� ���Ҹ� ���ʴ�� i�� �����ϸ� �ݺ�
        for j in blank : # �ݺ��� for -> blank��� list�� ���Ҹ� ���ʴ�� j�� �����ϸ� �ݺ�
            data[i][j] = " " # data[i][j]�� ���Ҹ� �������� �ٲ�
for i in data : # �ݺ��� for -> data��� list�� ���Ҹ� ���ʴ�� i�� �����ϸ� �ݺ�
    print("".join(i)) # join�� ����Ͽ� i�� ���ļ� �ϳ��� ���ڿ��� �ٲ㼭 ���
                      # '������'.join(list) -> �����ڿ� _�� ������ list�� ���Ҹ� ����ϵ� ���� ���̿� _�� �߰��Ͽ� ���