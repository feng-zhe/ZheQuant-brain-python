import json
from zq_db.mongodb import get_single_stock_data

def inc_pct(json_str):
    '''Calculate the increasement by percentage

    Args:
        json_str:   The json of stock composition
                    e.g.
                    {
                        "test_code1": 200,
                        "test_code2": 300,
                        ...
                    }

    Returns:
        A number indicating the increasement percentage
            e.g. return 1 means 1%

    Raises:
       N/A 
    '''
    compo = json.loads(json_str)
    begin_value = 0                                     # begin value
    for key, val in compo:
        get_single_stock_data(#TODO
        begin_value += 

    curr_value = 0                                      # current value
    for key, val in compo:
        pass                                            #TODO

    if begin_value:
        return curr_value/begin_value*100
