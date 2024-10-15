# Description: 呼叫tools.file模組的函式
# tools目錄為一個package，裡面有一個file.py模組，提供了兩個函式，
# created_log_file()和record_info()，用空的__init__.py檔案來標示這是
# 一個package。

from datetime import datetime

import tools.file

def main():
    now=datetime.now()
    current_file_name=now.strftime("%Y-%m-%d.log") #取得現在時間
    log_path=tools.file.created_log_file(current_file_name)  #呼叫函式   
    tools.file.record_info(log_path) #呼叫函式

    
if __name__ == '__main__':


    main()
    
