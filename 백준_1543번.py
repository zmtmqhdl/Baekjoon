a = str(input()) # �� ����
b = str(input()) # �� ����
count = 0 # ������� ������ count���� �ʱ�ȭ
n = 0 # index���� ������ n���� �ʱ�ȭ
while n <= len(a) - len(b) : # �ݺ��� while
    if a[n:n + len(b)] == b : # ���ǹ� if, else -> n��° ���ں��� n + len(b)������ ���ڰ� b�� ���� ���
        count += 1 # count = count + 1
        n += len(b) # n = n + len(b)
    else :
        n += 1 # n = n + 1 -> ���� index���� �ٽ� ����
print(count) # ���