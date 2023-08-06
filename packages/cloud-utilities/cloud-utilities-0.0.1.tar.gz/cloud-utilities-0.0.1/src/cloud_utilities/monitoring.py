import requests


class ManagedPrometheus:
    def __init__(self, credentials) -> None:
        self.__credentials = credentials

    def fetch_aggregated_metrics(self, promql_queries, project):
        url = f"https://monitoring.googleapis.com/v1/projects/{project}/location/global/prometheus/api/v1/query"
        aggregated_metrics = []
        for query in promql_queries:
            aggregated_metric = []
            request_body = {
                "query": query
            }
            response = requests.post(url, json=request_body, headers=self.__credentials.get_auth_header()[0])
            if response.status_code == 200:
                for result in response.json().get('data', {}).get('result', []):
                    aggregated_metric.append(result)
            aggregated_metrics.append(aggregated_metric)
        return aggregated_metrics, response.status_code
