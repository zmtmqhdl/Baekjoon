n, m = map(int,input().split()) # �� ����
arr1 = set() # arr1��� ���� ����
arr2 = set() # arr2��� ���� ����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ� 
    arr1.add(input()) # add�� ����Ͽ� arr1��� ���տ� ���Ե� ���� ���ҷ� ����
for _ in range(m) : # �ݺ��� for -> m��ŭ �ݺ�
    arr2.add(input()) # add�� ����Ͽ� arr2��� ���տ� ���Ե� ���� ���ҷ� ����
arr = sorted(list(arr1 & arr2)) # arr1, arr2��� ������ ���� �߿��� ��ġ�� ���Ҹ� ������������ �����ϰ� �� ���ҵ��� arr��� ������ ����� ���ҷ� ����
print(len(arr)) # len�� ����Ͽ� arr��� ������ ���� ���� ���
for i in arr : # �ݺ��� for -> arr��� ������ ���Ҹ� i�� ���ʴ�� �����ϸ� �ݺ�
    print(i) # ���