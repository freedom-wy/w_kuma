from w_kuma.libs.handle_request_http import HTTP
from w_kuma.config import zoomeye_api
from w_kuma.libs.handle_thread import ThreadRequest


class ZoomeyeApi(object):
    def __init__(self):
        self.total = 0
        self.datas = []

    def __fill_single(self, data):
        """
        一条数据
        :param data:
        :return:
        """
        if data:
            self.total = 1
            self.datas.append(data)

    def __fill_collection(self, data, query):
        """
        多条数据,免费账号数据量有限
        :param data:
        :return:
        """
        if data.get("total") > 30:
            self.datas.extend(data.get("list"))
            # total_page = data.get("total") // 30
            # url_list = [zoomeye_api.format(query, page) for page in range(2, total_page+1)]
            # per_page_response = ThreadRequest().thread_request_zoomeye_api(url_list)
            # temp = [item.get("list") for item in per_page_response.data_list]
            # self.datas.extend(temp)
            self.total = len(self.datas)
        else:
            self.total = data.get("total")
            self.datas = data.get("list")

    def search_by_zoomeye(self, query, page=1):
        url = zoomeye_api.format(query, page)
        response = HTTP.get(url)
        if response and response.get("total") == 1:
            self.__fill_single(data=response)
        elif response and response.get("total") > 1:
            self.__fill_collection(data=response, query=query)


if __name__ == '__main__':
    ZoomeyeApi().search_by_zoomeye(query="360.cn")
