analyze_config = {
  "1": {"key": "interactions", "type": "int"},
  "2": {"key": "unique_authors", "type": "int"},
  "3": {
    "key": "analysis",
    "type": "obj",
    "value": {
      "1": {"key": "analysis_type", "type": "str"},
      "2": {
        "key": "parameters",
        "type": "obj",
        "value": {
          "1": {"key": "target", "type": "str"},
          "2": {"key": "threshold", "type": "int"}
        }
      },
      "3": {
        "key": "results",
        "type": "list",
        "value": {
          "1": {"key": "key", "type": "str"},
          "2": {"key": "interactions", "type": "int"},
          "3": {"key": "unique_authors", "type": "int"},
          "4": {
            "key": "child",
            "type": "obj",
            "value": {
              "1": {"key": "analysis_type", "type": "str"},
              "2": {
                "key": "parameters",
                "type": "int",
                "value": {
                  "1": {"key": "target", "type": "str"},
                  "2": {"key": "threshold", "type": "int"}
                }
              },
              "3": {
                "key": "results",
                "type": "list",
                "value": {
                  "1": {"key": "key", "type": "str"},
                  "2": {"key": "interactions", "type": "int"},
                  "3": {"key": "unique_authors", "type": "int"}
                }
              },
              "4": {"key": "redacted", "type": "bool"}
            }
          }
        }
      }
    }
  }
}