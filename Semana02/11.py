
f = open('test.txt', 'r')

print(f.name)
print(f.mode)
f.close()

with open('test.txt', 'r') as g:

    # for line in g:
    #     print(line, end='')
    # g_cont1 = g.readline()
    # print(g_cont1, end='')
    # g_cont1 = g.readline()
    # print(g_cont1, end='')
    # g_contents = g.read(50)
    # print(g_contents)
    # g_contents = g.read(50)
    # print(g_contents)
    # g_cont = g.readlines()
    # print(g_cont)
    size_to_read = 10
    g_cont2 = g.read(size_to_read)
    print(g_cont2, end='*')

    g.seek(0)
    g_cont2 = g.read(size_to_read)
    print(g_cont2, end='*\n')

    print(g.tell())

    # while len(g_cont2) > 0:
    #     print(g_cont2, end='*')
    #     g_cont2 = g.read(size_to_read)
    #f.write('Test')

print(g.closed)
#print(g.read())

with open('test2.txt', 'w') as h:
    h.write('Test')
    h.seek(0)
    h.write('R')

with open('test2.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# with open('test2.jpg', 'rb') as rf:
#     with open('test_copy.jpg', 'wb') as wf:
#         for line in rf:
#             wf.write(line)

# with open('test2.jpg', 'rb') as rf:
#     with open('test_copy.jpg', 'wb') as wf:
#        chunk_size = 4096
#        rf_chunk = rf.read(chunk_size)
#        while len(rf_chunk) > 0:
#            wf.write(rf_chunk)
#            rf_chunk = rf.read(chunk_size)
