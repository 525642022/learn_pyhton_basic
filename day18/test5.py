# 作者 ljc

# 作者 ljc
import requests
import threadpool


def get_stock(code):
    url = 'http://hq.sinajs.cn/list=' + code
    resq = requests.get(url).text
    print("%s----\n" % resq)


codes = ['sz000878',
         'sh600993', 'sz000002', 'sh600153', 'sz002230', 'sh600658']
# threads = [threading.Thread(target=get_stock,args=(code,))
#            for code in codes]
#
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()
pool = threadpool.ThreadPool(2)
tasks = threadpool.makeRequests(get_stock, codes)
[pool.putRequest(task) for task in tasks]
pool.wait()
