from sorted_print.SortedPrint import OrderedResponse
from sorted_print.configs.DatasiftAnalyze import analyze_config
import json

op = OrderedResponse()

raw_json = '{"unique_authors": 15700, "analysis": {"analysis_type": "freqDist", "redacted": false, "results": [{"child": {"analysis_type": "freqDist", "redacted": false, "results": [{"unique_authors": 9200, "key": "female", "interactions": 9600}, {"unique_authors": 3300, "key": "male", "interactions": 3500}], "parameters": {"threshold": 2, "target": "fb.author.gender"}}, "unique_authors": 12700, "key": "like", "interactions": 13300}, {"child": {"analysis_type": "freqDist", "redacted": false, "results": [{"unique_authors": 1200, "key": "female", "interactions": 1500}, {"unique_authors": 500, "key": "male", "interactions": 700}], "parameters": {"threshold": 2, "target": "fb.author.gender"}}, "unique_authors": 1800, "key": "comment", "interactions": 2300}], "parameters": {"threshold": 2, "target": "fb.type"}}, "interactions": 18300}'

data = json.loads(raw_json)

op.ordered_print(data, analyze_config)
