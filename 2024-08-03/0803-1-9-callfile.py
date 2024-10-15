
#呼叫file.py檔案的主程式，並執行函式
# -*- coding: utf-8 -*-

from datetime import datetime

import file

def main():
    now=datetime.now()
    current_file_name=now.strftime("%Y-%m-%d.log") #取得現在時間
    log_path=file.created_log_file(current_file_name)  #呼叫函式   
    file.record_info(log_path) #呼叫函式

    
if __name__ == '__main__':


    main()
    
