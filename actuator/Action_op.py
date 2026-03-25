from Keyboard_op import *
from Mouse_op import *
from typing import List
class GameAction:
    """
    游戏动作类，封装《云顶之弈》的常用操作，基于鼠标和键盘控制器。
    """

    def __init__(self, mouse: MouseController, keyboard: KeyboardController):
        self.mouse = mouse
        self.keyboard = keyboard
        # 可在此加载坐标配置，例如：
        # self.coords = load_coords()  # 假设一个坐标映射字典

    def choose_HEX(self, HEX_index: int):
        """
        选择海克斯
        :param HEX_index: 海克斯格子索引 (0~2)
        """
        # 需要将 HEX_index 映射到屏幕坐标
        # 假设有一个方法 _get_HEX_coord(HEX_index) 返回 (x, y)
        x, y = self._get_HEX_coord(HEX_index)
        self.mouse.click(x=x, y=y)

    def rise_population(self, click_num: int):
        """升人口：按 F 键"""
        for i in range(click_num):
            self.keyboard.press('f')

    def refresh_shop(self):
        """刷新商店：按 D 键"""
        self.keyboard.press('d')

    def buy_unit(self, shop_index: int):
        """
        购买棋子
        :param shop_index: 商店格子索引 (0~4)
        """
        # 需要将 shop_index 映射到屏幕坐标
        # 假设有一个方法 _get_shop_coord(shop_index) 返回 (x, y)
        x, y = self._get_shop_coord(shop_index)
        self.mouse.click(x=x, y=y)

    def sell_unit(self, location: str, index: int):
        """
        出售棋子
        :param location: 'field' 或 'bench'
        :param index: 场上或备战区的位置索引
        """
        x, y = self._get_unit_coord(location, index)
        self.mouse.move_to(x=x, y=y)   
        self.mouse.wait(random_range=(0.2, 0.4))
        self.keyboard.press('e')#鼠标移动到目标棋子后快捷键E

    def field_unit(self, from_bench_index: int, to_field_position: int):
        """
        棋子上场：从备战区拖到场上指定位置
        :param from_bench_index: 备战区索引
        :param to_field_position: 场上目标位置索引
        """
        start = self._get_bench_coord(from_bench_index)
        end = self._get_field_coord(to_field_position)
        self.mouse.drag(start_x=start[0], start_y=start[1], end_x=end[0], end_y=end[1], duration=0.4)

    def bench_unit(self, from_field_position: int, to_bench_index: int):
        """
        棋子下场：从场上拖回备战区
        """
        start = self._get_field_coord(from_field_position)
        end = self._get_bench_coord(to_bench_index)
        self.mouse.drag(start_x=start[0], start_y=start[1], end_x=end[0], end_y=end[1], duration=0.4)

    def adjust_position(self, from_field_position: int, to_field_position: int):
        """
        调整场上棋子位置
        """
        start = self._get_field_coord(from_field_position)
        end = self._get_field_coord(to_field_position)
        self.mouse.drag(start_x=start[0], start_y=start[1], end_x=end[0], end_y=end[1], duration=0.4)

    def combine_items(self, item1_slot: int, item2_slot: int, target_unit: Optional[dict] = None):
        """
        装备合成：将两个基础装备合成为新装备
        :param item1_slot: 装备栏中第一个装备的槽位索引
        :param item2_slot: 装备栏中第二个装备的槽位索引
        :param target_unit: 可选，合成后直接装备的目标棋子，格式如 {'location': 'field', 'index': 3}
        """
        # 点击第一个装备
        x1, y1 = self._get_item_slot_coord(item1_slot)
        self.mouse.click(x=x1, y=y1)
        self.mouse.wait(random_range=(0.1, 0.2))
        # 点击第二个装备（触发合成）
        x2, y2 = self._get_item_slot_coord(item2_slot)
        self.mouse.click(x=x2, y=y2)
        self.mouse.wait(random_range=(0.3, 0.5))
        # 如果指定了目标，则将合成后的装备授予目标棋子
        if target_unit:
            # 假设合成后装备出现在装备栏第一个空位或固定位置，再点击拖拽到棋子
            # 此处简化：直接获取合成后装备的位置并拖拽
            equip_x, equip_y = self._get_equipment_coord()  # 合成后装备位置
            target_x, target_y = self._get_unit_coord(target_unit['location'], target_unit['index'])
            self.mouse.drag(start_x=equip_x, start_y=equip_y, end_x=target_x, end_y=target_y, duration=0.3)

    def assign_item(self, item_slot: int, target_unit: dict):
        """
        装备分配：将已有装备装备给指定棋子
        :param item_slot: 装备栏槽位索引
        :param target_unit: 目标棋子，如 {'location': 'field', 'index': 5}
        """
        # 拖拽装备到棋子
        start_x, start_y = self._get_item_slot_coord(item_slot)
        target_x, target_y = self._get_unit_coord(target_unit['location'], target_unit['index'])
        self.mouse.drag(start_x=start_x, start_y=start_y, end_x=target_x, end_y=target_y, duration=0.3)

    def move_legend(self, target_position: int, path: Optional[List[int]] = None):
        """
        小小英雄移动（通常选秀阶段）
        :param target_position: 目标格子编号
        :param path: 可选，移动路径格子编号列表，若不提供则直接移动到目标
        """
        # 如果提供了路径，依次移动；否则直接点击目标
        if path:
            for pos in path:
                x, y = self._get_legend_grid_coord(pos)
                self.mouse.click(x=x, y=y)
                self.mouse.wait(random_range=(0.1, 0.2))
        else:
            x, y = self._get_legend_grid_coord(target_position)
            self.mouse.click(x=x, y=y)

    # 以下为坐标映射方法，需要根据实际游戏界面标定
    def _get_HEX_coord(self, index: int) -> Tuple[int, int]:
        """返回海克斯格子坐标"""
        # 示例坐标，实际需测量
        HEX_coords = [(100, 400), (200, 400), (300, 400)]
        return HEX_coords[index]
    
    def _get_shop_coord(self, index: int) -> Tuple[int, int]:
        """返回商店格子坐标"""
        # 示例坐标，实际需测量
        shop_coords = [(100, 400), (200, 400), (300, 400), (400, 400), (500, 400)]
        return shop_coords[index]

    def _get_bench_coord(self, index: int) -> Tuple[int, int]:
        """返回备战区格子坐标"""
        # 示例
        bench_coords = [(100, 600), (200, 600), (300, 600), (400, 600), (500, 600)]
        return bench_coords[index]

    def _get_field_coord(self, position: int) -> Tuple[int, int]:
        """返回场上棋子位置坐标"""
        # 场上格子通常有多个位置，需要映射
        field_coords = {}  # 实际需要定义
        # 假设位置编号0-27
        return field_coords.get(position, (0,0))

    def _get_sell_button_coord(self) -> Tuple[int, int]:
        """返回出售按钮坐标"""
        return (200, 500)  # 示例

    def _get_item_slot_coord(self, slot: int) -> Tuple[int, int]:
        """返回装备栏槽位坐标"""
        item_coords = [(50, 100), (100, 100), (150, 100)]  # 示例
        return item_coords[slot]

    def _get_equipment_coord(self) -> Tuple[int, int]:
        """返回合成后装备所在位置（可能临时在装备栏或中央）"""
        return (250, 250)  # 示例

    def _get_unit_coord(self, location: str, index: int) -> Tuple[int, int]:
        """根据位置类型和索引返回棋子坐标"""
        if location == 'field':
            return self._get_field_coord(index)
        elif location == 'bench':
            return self._get_bench_coord(index)
        else:
            raise ValueError(f"Invalid location: {location}")

    def _get_legend_grid_coord(self, grid_index: int) -> Tuple[int, int]:
        """返回小小英雄移动的格子坐标"""
        # 选秀阶段格子坐标
        legend_coords = {}  # 需要标定
        return legend_coords.get(grid_index, (0,0))