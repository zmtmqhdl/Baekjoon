n = int(input()) # �ݺ� Ƚ�� ����
for _ in range(n) : # �ݺ��� for
    data = input() # �� ����
    for i in range(len(data) - 1) : # �ݺ��� for -> i��° ���ڿ� i + 1��° ���ڸ� ���� ���̹Ƿ� ������ ���ڴ� Ƚ���� �� �ʿ䰡 ���⿡ �ݺ� Ƚ���� data�� ���� - 1
        if data[i] != data[i + 1] : # ���ǹ� if -> ���� i��° ���ڿ� i + 1��° ���ڰ� ���� �ʴٸ�
            new_data = data[i + 1:] # new_data��� ������ data�� i + 1��°���� ������ ���ڱ��� ����
            if new_data.count(data[i]) > 0 : # ���ǹ� if - > ���� new_data�� data[i]�� �����Ѵٸ�
                n -= 1 # n = n - 1
                break # ����
print(n) # ���