import codecs

fo = codecs.open('../data/tmp_file/output.txt','w','utf8')
with codecs.open('../data/tmp_file/untitled.txt','r','utf8') as fi:
    for i in fi:
        line = i.strip().split('\t')
        order_1 = line[0].replace('\n','  ')
        order_1 = order_1.replace('   ',' ')
        order_1 = order_1.replace('  ', ' ')
        order_1 = order_1.replace('{', '')
        order_1 = order_1.replace('}', '')
        order_1 = order_1.replace('\'', '')
        order_1 = order_1.replace(', ', ',')
        order_1 = order_1.replace(' ,', ',')
        order_1 = order_1.replace(' ,', ',')
        order_1 = order_1.replace(' 》', '》')
        order_1 = order_1.replace('《 ', '《')
        order_1 = order_1.replace('【 ', '【')
        order_1 = order_1.replace(' 】', '】')
        order_1 = order_1.replace(' )', ')')
        order_1 = order_1.replace('( ', '(')
        order_1 = order_1.replace('（ ', '（')
        order_1 = order_1.replace(' ）', '）')
        order_1 = order_1.replace('   ', '')
        order_1 = order_1.replace('  ', '')
        # order_1 = order_1.replace('')
        # print(type(line[0]))
        fo.write(order_1+'\t'+line[1])