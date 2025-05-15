import concurrent.futures
import requests
import time
import logging
from typing import List, Dict, Any

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class IdempotencyTester:
    def __init__(self, url: str, method: str = "POST",
                 headers: Dict[str, str] = None,
                 payload: Dict[str, Any] = None,
                 timeout: int = 10,
                 concurrent_requests: int = 10):
        """
        初始化幂等性测试器

        Args:
            url: 测试接口的URL
            method: HTTP方法，默认为"POST"
            headers: 请求头
            payload: 请求体
            timeout: 请求超时时间（秒）
            concurrent_requests: 并发请求次数
        """
        self.url = url
        self.method = method.upper()
        self.headers = headers or {}
        self.payload = payload or {}
        self.timeout = timeout
        self.concurrent_requests = concurrent_requests
        self.session = requests.Session()

    def send_request(self) -> Dict[str, Any]:
        """发送单个请求并返回结果"""
        try:
            start_time = time.time()

            if self.method == "GET":
                response = self.session.get(
                    self.url,
                    headers=self.headers,
                    timeout=self.timeout
                )
            elif self.method == "POST":
                response = self.session.post(
                    self.url,
                    headers=self.headers,
                    json=self.payload,
                    timeout=self.timeout
                )
            else:
                raise ValueError(f"不支持的HTTP方法: {self.method}")

            end_time = time.time()

            return {
                "success": response.ok,
                "status_code": response.status_code,
                "response_time": end_time - start_time,
                "content": response.text,
                "headers": dict(response.headers)
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    def run_concurrent_tests(self) -> List[Dict[str, Any]]:
        """并发执行多次请求测试"""
        results = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.concurrent_requests) as executor:
            # 提交所有请求
            future_to_index = {
                executor.submit(self.send_request): i
                for i in range(self.concurrent_requests)
            }

            # 收集结果
            for future in concurrent.futures.as_completed(future_to_index):
                index = future_to_index[future]
                try:
                    result = future.result()
                    results.append((index, result))
                except Exception as e:
                    results.append((index, {"success": False, "error": str(e)}))

        # 按索引排序结果
        results.sort(key=lambda x: x[0])
        return [result for _, result in results]

    def print_results(self, results: List[Dict[str, Any]]) -> None:
        """打印所有请求结果"""
        for i, result in enumerate(results):
            print(f"\n===== 请求 {i + 1} 的结果 =====")

            if not result["success"]:
                print(f"失败: {result.get('error', '未知错误')}")
                continue

            print(f"状态码: {result['status_code']}")
            print(f"响应时间: {result['response_time']:.3f}s")
            print(f"响应内容: {result['content']}")


def main():
    # 配置测试参数（请根据实际情况修改）
    test_config = {
        "url": "https://fat-manage.svfactory.com:6143/miai/brainstorm/threedim/sampleproductsyncmanage/addSampleToTask",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJQaW13SEZ5Wk1jdlNRRklJWUdFWW1fdGZNTFBldEU0ck5aMlphd3lVRXB3In0.eyJleHAiOjE3NDcxNDkwNDgsImlhdCI6MTc0NzEyMzg0OCwiYXV0aF90aW1lIjoxNzQ3MTIyMTU0LCJqdGkiOiIzYmRjYmYzMS00YjA0LTQ2ZjEtYmQxZC1jODZiZGEyZDNmNDkiLCJpc3MiOiJodHRwczovL2ZhdC1zc28uc3ZmYWN0b3J5LmNvbTo2MTQzL2F1dGgvcmVhbG1zL3V1YW0iLCJzdWIiOiJmOjExMTQ0YmJjLWFkN2UtNDJkYS05ZTEyLWI3Y2Q5OWE5NWRiYzoxNzQwMjk5Nzg1OTY2OTgxMTIxIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYnJhaW5zdG9ybS1mZSIsIm5vbmNlIjoiYzNhMDFiY2UtN2MyZi00YWIyLThiMmQtYmZlOTQyODYyMjMxIiwic2Vzc2lvbl9zdGF0ZSI6ImY5ZWRjYWRmLTlmYjAtNGQwYS1hMDk3LTkyOGRkZmU0ZjU2MiIsImFjciI6IjAiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInNpZCI6ImY5ZWRjYWRmLTlmYjAtNGQwYS1hMDk3LTkyOGRkZmU0ZjU2MiIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwibmFtZSI6Iuael-emueaIkOa1i-ivleS9v-eUqCIsInByZWZlcnJlZF91c2VybmFtZSI6Imxpbnl1Y2hlbmciLCJnaXZlbl9uYW1lIjoi5p6X56a55oiQ5rWL6K-V5L2_55SoIiwiZW1haWwiOiI4NDkyMzYwMDBAcXEuY29tIn0.AOQST7ksV9rfVqgEkxcDRmx0Fa5RlRVTqsBoUGDBG0YJCf8IspKEaiGq14KZuF6ogpIySSo01PZVzpDv4PRN77h4jiPA4gBG0Dnt5bL00w7gC9wsTcj8FfxoJE0wF0c9UEDUudbuS7wydYr9wPojnOTSunm_o1mFBMD40OV0Kyz-fXhlfV27HMKM6HVIjys0WJMonI7ozhqx6Kh4kiV0fzOiCmZ9L_A0tAuMnOKro826F8bUJ7XSiYTOgzADFhpfz76gTJxWGGKgWcvj4XfyUIoHF4leOUjDyexKJBGpzixqE9gwSLiRCTvhxG1w9yjFY2-5Ufa4IdHlWgsNVRrYPQ",
            "miai-product-code": "JHOCT001",
            "miaispacemanageid": "1873905652887785473"
        },
        "payload": {
            "taskName": "JHOCT001-20250513175453",
            "dimensionTaskList": [
                {
                    "labelUsers": [
                        {
                            "labelUserId": "1740299785966981121",
                            "labelUserName": "林禹成测试使用"
                        }
                    ],
                    "taskName": "JHOCT001-20250513175453-E-1"
                }
            ],
            "subTaskNum": 1,
            "subTaskSampleNum": 100,
            "date": [
                "2025-05-11T16:00:00.000Z",
                "2025-05-13T15:59:59.999Z"
            ],
            "dataSyncIds": [
                "1922195761664741378"
            ],
            "sampleSource": "2",
            "taskId": "",
            "workpieceId": "",
            "deviceId": "",
            "sortingSampleType": "ng",
            "statusList": [],
            "startDateTime": "2025-05-11T16:00:00.000Z",
            "endDateTime": "2025-05-13T15:59:59.999Z",
            "productInfoId": "1873905708948852738",
            "isUse": False,
            "status": 2,
            "excludeDataSyncIds": []
        },
        "concurrent_requests": 10
    }

    # 创建并运行测试
    tester = IdempotencyTester(**test_config)
    results = tester.run_concurrent_tests()
    tester.print_results(results)


if __name__ == "__main__":
    main()