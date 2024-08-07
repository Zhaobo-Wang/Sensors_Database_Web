    from queries import insert_sensor, delete_sensor, update_sensor_location, get_sensors
    
    def main():
        # 插入新传感器
        print("插入新传感器...")
        insert_sensor(1, 'sensor_001', 'Location_A')
    
        # 查询传感器
        print("查询传感器...")
        sensors = get_sensors()
        for sensor in sensors:
            print(sensor)
    
        # 更新传感器位置
        print("更新传感器位置...")
        update_sensor_location(1, 'Location_B')
    
        # 查询传感器
        print("查询传感器...")
        sensors = get_sensors()
        for sensor in sensors:
            print(sensor)
    
        # 删除传感器
        print("删除传感器...")
        delete_sensor(1)
    
        # 查询传感器
        print("查询传感器...")
        sensors = get_sensors()
        for sensor in sensors:
            print(sensor)
    
    if __name__ == '__main__':
        main()