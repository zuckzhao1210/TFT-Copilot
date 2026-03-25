import json
from Keyboard_op import *
from Mouse_op import *
from Action_op import *
def parse_operation(ops_json_PATH,action):
    with open(ops_json_PATH,'r',encoding='utf-8') as ops_json:
        ops = json.load(ops_json)
    game_round = ops.get("game_round")
    operations = ops.get("operations", {})
    
    # 检查并执行每个操作
    if operations.get("choose_HEX") is not None:
        index = operations["choose_HEX"]["index"]
        #with operations["choose_HEX"] as 
        # action.choose_HEX(index)
        print(f'DO:1.choose_HEX{index}!\n')

    if operations.get("rise_population") is not None:
        num = operations["rise_population"]["click_num"]
        # action.rise_population(num)
        print(f'DO:2.rise_population{num} times!\n')

    if operations.get("move_legend") is not None:
        target_position = operations["move_legend"]["target_position"]
        path = operations["move_legend"]["path"]
        # action.move_legend(target_position,path)
        print(f'DO:3.move_legend!\n')

    if operations.get("refresh_shop") is not None:
        # action.refresh_shop()
        print(f'DO:4.refresh_shop!\n')

    if operations.get("buy_units"):
        for buy in operations["buy_units"]:
            shop_idx = buy["shop_index"]
            # action.buy_unit(shop_idx)
            print(f'DO:5.buy_units at idx={shop_idx}!\n')

    if operations.get("sell_units"):
        for sell in operations["sell_units"]:
            location = sell["location"]
            idx = sell["index"]
            # action.sell_unit(location,idx)
            print(f'DO:6.sell_units at {location} idx={idx}!\n')

    if operations.get("field_units"):
        for unit in operations["field_units"]:
            from_bench_index = unit["from_bench_index"]
            to_field_position = unit["to_field_position"]
            # action.field_unit(from_bench_index,to_field_position)
            print(f'DO:7.field_units frmo {from_bench_index}to{to_field_position}!\n')
    
    if operations.get("bench_units"):
        for unit in operations["bench_units"]:
            from_field_position = unit["from_field_position"]
            to_bench_index = unit["to_bench_index"]
            # action.bench_unit(from_field_position,to_bench_index)
            print(f'DO:8.bench_units frmo {from_field_position} to {to_bench_index}!\n')

    if operations.get("position_adjustments"):
        for unit in operations["position_adjustments"]:
            unit_field_position = unit["unit_field_position"]
            target_field_position = unit["target_field_position"]
            # action.adjust_position(unit_field_position,target_field_position)
            print(f'DO:9.position_adjustments frmo {unit_field_position} to {target_field_position}!\n')

    if operations.get("combine_items"):
        for item in operations["combine_items"]:
            item1_id = item["item1_id"]
            item2_id = item["item2_id"]
            target_unit = item["target_unit"]
            # action.combine_items(item1_id,item2_id,target_unit)
            print(f'DO:10.combine_items {item1_id} and {item2_id}!\n')

    if operations.get("assign_items"):
        for item in operations["assign_items"]:
            item_id = item["item_id"]
            target_unit = item["target_unit"]
            #action.assign_item(item_id,target_unit)
            print(f'DO:11.assign_items {item_id}!\n')
    return True

def main():
    PATH = 'operation_protocol/game_op.json'
    keyboard = KeyboardController()
    mouse = MouseController()
    action = GameAction(mouse,keyboard)
    STATE = parse_operation(PATH,action)

if __name__ == "__main__":
    main()