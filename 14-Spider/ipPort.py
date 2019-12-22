import json
import http.client
import urllib.parse


def http_client():
    params = {"a": "123"}
    headers = {"Content-type": "application/json"}
    conn = http.client.HTTPConnection(
        "www.baidu.com", 5005, source_address=("1.2.3.4", 0))
    conn.request("GET", "/test/nihao", json.dumps(params), headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read().decode()
    print(data)
    conn.close()


def main():
    http_client()


if __name__ == '__main__':
    main()