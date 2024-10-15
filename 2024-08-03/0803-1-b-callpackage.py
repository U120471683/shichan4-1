from datetime import datetime
from  tools.file import created_log_file,record_info

def main():
    now=datetime.now()
    current_file_name=now.strftime("%Y-%m-%d.log") #取得現在時間
    log_path=created_log_file(current_file_name)  #呼叫函式   
    record_info(log_path) #呼叫函式

    
if __name__ == '__main__':


    main()
    
