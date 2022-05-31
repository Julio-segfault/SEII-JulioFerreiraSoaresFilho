
try:
    f = open('test_file1.txt')
    #var = bad_var
    if f.name == 'corrupt_file.txt':
        raise Exception
except FileNotFoundError:
    print('ごめんなさい!ファイルが見つかりません')
# except Exception as e:
#     print(e)
except Exception:
    print('ごめんなさい!なにかが悪いした')
else:
    print(f.read())
    f.close()
finally:
    print('Executing Finally...')


