# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
import json
from pprint import pprint


def main():
    # In python dicts are analogous to json as they are the only mapping types
    some_dict = {
                    "String_key": "String_value",
                    1: [1, 2, 3, 4],
                    1.2: {
                        "some_nested_json_key": "some_nested_json_values"
                    }
                }
    dumped_json = json.dumps(some_dict)
    # Dumping JSON means converting it into the string format
    print('The Dumped JSON is')
    print(dumped_json)
    loaded_json = json.loads(dumped_json)
    print('The Loaded JSON is')
    pprint(loaded_json)
    # We can access key values in this loaded_json as we do normally in dicts


if __name__ == "__main__":
    main()
