data = input() # �� ����
ucpc = ['U', 'C', 'P', 'C'] # UCPC���ڸ� �����ϰ� �ִ� ucpc��� list����
check = True # UCPC�� ����������� Ȯ���ϱ� ���� True���� �����ϰ� �ִ� check���� ����
for i in range(len(ucpc)) : # �ݺ��� for -> 0���� len(ucpc) - 1���� i�� ���ʴ�� �����ϸ� �ݺ�
    if ucpc[i] in data : # ���ǹ� if, else -> ucpc[i]�� ���� data�� �����ϴ� ���
        idx = data.find(ucpc[i]) # find�� ����Ͽ� data�� ucpc[i]���� �����ϴ� index���� idx������ ���� 
        data = data[idx + 1:] # data���� idx + 1��° index���� ������ ���Ӱ� ���� 
    else : # ucpc[i]�� ���� data�� ���� ���
        check = False # UCPC�� ��������� �ʴ� ���� Ȯ���ϱ� ���� check���� False�� ����
        break # ����
if check == True : # ���ǹ� if, else -> UCPC�� ��������� ���
    print('I love UCPC') # ���
else : # UCPC�� ��������� �ʴ� ���
    print('I hate UCPC') # ���