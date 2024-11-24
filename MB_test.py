import subprocess

Test_Info = "=" * 15+ " Test_Info " +"=" * 15
Test_Info_Data = {
    "MES_Status" : "",
    "CM_SN" : "",
    "Owner_SN" : "",
    "Model" : "",
    "OPID" : "",
    "MAC" : "How to get",
    "SAS" : "NA",
    "IPMI" : "How to get",
    "IB" : "NA",
    "1394" : "NA",
    "ServerTime" : "ServerTime_Data",
    "Work_Order" : "Work Order_Data",
    "PCB" : "How to get",
    "ECO" : "NA",
    "Work_State" : "How to get",
    "IntelSN" : "NA",
    "OP Request" : "NA",
    "PBA" : "NA",
    "TA" : "NA",
    "Fix Number" : "How to get",
    "OS detail" : "",
}

#設定檔案名稱
output_file = "test_log.txt"

#輸入Test_Info的資料
Test_Info_Data["MES_Status"] = input("請輸入目前MES的狀態:")
Test_Info_Data["CM_SN"] = input("請輸入代工廠的SN:")
Test_Info_Data["Owner_SN"] = input("請輸入原廠的SN:")
Test_Info_Data["Model"] = input("請輸入專案名稱:")
Test_Info_Data["OPID"] = input("請輸入作業員員工編號:")
Test_Info_Data["Work_Order"] = Test_Info_Data["CM_SN"][0:12+1]

#設定command的指令，並做
command = "date +'%Y%m%d%H%M%S'"

#shell=True:使其可以直接執行字串形式的指令
#capture_output=True:需要處理指令的輸出
#text=True:將資料的type轉為str
command_result = subprocess.run(command, shell=True, capture_output=True, text=True)
# 取得指令的資料，".stdout"代表指令的資料
Test_Info_Data["ServerTime"] = command_result.stdout.strip("\n")

# 使用 subprocess 執行指令並將結果存入 txt 檔，w：覆蓋檔案內的資訊
with open(output_file, "w", encoding="utf-8") as file:
    file.write(f"{Test_Info}\n")
    #存入Test_Info_Data的資料
    for key, value in Test_Info_Data.items():
        file.write(f"{key}: {value}\n")

# 執行 'cat /etc/os-release' 命令，並捕獲其標準輸出
command = "cat /etc/os-release"
#shell=True:使其可以直接執行字串形式的指令
#capture_output=True:需要處理指令的輸出
#text=True:將資料的type轉為str
command_result = subprocess.run(command, shell=True, capture_output=True, text=True)
# 取得命令的標準輸出
os_release_data = command_result.stdout

# 解析資料，並轉換為字典型態
os_info = {}
for line in os_release_data.splitlines():
    if "=" in line:
        key, value = line.split("=", 1)
        os_info[key.strip()] = value.strip('"')  # 去除雙引號

# 進行後續分析（範例: 確認操作系統名稱）
os_name = os_info.get("NAME")
os_version = os_info.get("VERSION")

#新增ubuntu資訊;a:新增檔案內的資訊
with open(output_file, "a", encoding="utf-8") as file:
    file.write(f"{os_name}\n{os_version}\n")
    file.write("=" * 45)
    file.write("\n")
    #取得Test_Info_Data["OPID"]的value
    file.write(f"{Test_Info_Data["OPID"]};\n")
    #先把Test_Info_Data.keys()轉成list，再取出對應索引值的key
    file.write(f"{list(Test_Info_Data.keys())[4]} Use Manual mode: spent {0} seconds\n\n")
    file.write(f"{Test_Info_Data["Fix Number"]};\n")
    file.write(f"{list(Test_Info_Data.keys())[19]} Use Manual mode: spent {0} seconds\n\n")
    file.write(f"{Test_Info_Data["CM_SN"]};\n")
    file.write(f"{list(Test_Info_Data.keys())[1]} Use Manual mode: spent {0} seconds\n\n")

#做版本變更用