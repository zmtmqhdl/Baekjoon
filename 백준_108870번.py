n = int(input()) # �׽�Ʈ Ƚ�� ����
data = list(map(int, input().split())) # ���Ե� ���� ���� data��� list����
sort_data = sorted(list(set(data))) # data�� set������ �ٲپ� �ߺ��� ���� �����ϰ� ������������ ���ĵ� sort_data��� list����
result = {sort_data[i] : i for i in range(len(sort_data))} # sort_data���� i���� ���� ���Ұ� �� ��° index�� ��ġ�ϰ� �ִ��� Ȯ���ϱ� ���� result��� dictionary����
                                                           # data�� �� : ���ĵǾ��� ���� index��
for i in data : # �ݺ��� for -> i�� data�� ���Ҹ� ���ʴ�� ����
    print(result[i], end = ' ') # end�� ����Ͽ� ������� ������ �ΰ� ���