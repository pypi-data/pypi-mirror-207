import requests
import getpass
import json
import sys
import pandas as pd 

from datetime import datetime, timezone, timedelta

class SDTcloud():
    def __init__(self):
        print("Please enter your config information.")
        print("You have to use config function.")

    def exceptionHandle(self, responseData, subtype):
        resp_dict = json.loads(responseData.content)
        if subtype == "500":
            errFormat = {
                "timestamp": resp_dict['timestamp'],
                "code": responseData.status_code,
                "error": resp_dict['error'],
                "message": resp_dict['error']
            }
        else:
            errFormat = {
                "timestamp": resp_dict['timestamp'],
                "code": resp_dict['code'],
                "error": resp_dict['error'],
                "message": resp_dict['message']
            }
        
        raise Exception(f"Failed!!!\n {errFormat}")
    

    def checkStatusCode(self, status_code):
        """ Check status code and return 0 or 1. 
            0 is fail.
            1 is 200(OK).
            2 is 201(Created).
            3 is 204(No Content).

        Args:
            data (Dict): Response of api
            status_code (Int): Status code of resource
        """
        if status_code == 500:
            return 0, "500"
        elif status_code == 200:
            return 1, f"Ok!!!, Status: {status_code}"
        elif status_code == 201:
            return 2, f"Created!!!, Status: {status_code}"
        elif status_code == 204:
            return 3, f"No Content!!!, Status: {status_code}"
        else:
            return 0, ""
           
    def config(self, address, port):
        """ Setting config information.

        Args:
            address (Str): API Address
            port (Str): API Port
        """
        self.url = f"http://{address}:{port}"
        print("Ok!!!")

    # 로그인
    def login(self):
        """ login of stackbase. 

        Raises:
            Exception: _description_
        """
        
        userId = input("ID: ")
        userPassword = getpass.getpass("PW: ")

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        bodys = {
            "grantType": "password",
            "email": userId,
            "password": userPassword
        }
        
        response = requests.request('post',f"{self.url}/oauth/token", headers=headers, data=bodys)
        respStatus, returnMessage = self.checkStatusCode(response.status_code)

        if respStatus == 0:
            self.exceptionHandle(response, returnMessage)
        
        result = json.loads(response.content)

        self.userToken = f"Bearer {result['accessToken']}"

        print(returnMessage)

    # 스토리지 등록
    def create_storage(self, name, tag):
        """ Create storage in stackbase.

        Args:
            name (Str): Name's storage
            tag (Str): Tag's storage

        Raises:
            Exception: _description_

        Returns:
            _type_: _description_
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.userToken
        }

        bodys = json.dumps({
            "name": name,
            "tag": tag
        })

        response = requests.request('post',f"{self.url}/stackbase/v1/storages", headers=headers, data=bodys)
        respStatus, returnMessage = self.checkStatusCode(response.status_code)

        if respStatus == 0:
            self.exceptionHandle(response, returnMessage)

        result = json.loads(response.content)
        result['createdAt'] = datetime.fromtimestamp(int(result['createdAt']/1000), timezone(timedelta(hours=9)))
        result['updatedAt'] = datetime.fromtimestamp(int(result['updatedAt']/1000), timezone(timedelta(hours=9)))
        
        print(returnMessage)
    
    # 스토리지 단건 정보 조회
    def get_storage(self):
        print("single get")
    
    # 유저의 스토리지 리스트 조회
    def list_storage(self):
        """ Print list of storage in stackbase

        Raises:
            Exception: _description_

        Returns:
            _type_: _description_
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.userToken
        }

        response = requests.request('get',f"{self.url}/stackbase/v1/storages", headers=headers)
        respStatus, returnMessage = self.checkStatusCode(response.status_code)

        if respStatus == 0:
            self.exceptionHandle(response, returnMessage)
        elif respStatus == 3:
            print(returnMessage)
            return 0

        result = json.loads(response.content)
        df = pd.DataFrame(result)
        for n in range(len(df)):
            df.loc[n, 'createdAt'] = datetime.fromtimestamp(int(df.loc[n, 'createdAt']/1000), timezone(timedelta(hours=9)))
            df.loc[n, 'updatedAt'] = datetime.fromtimestamp(int(df.loc[n, 'updatedAt']/1000), timezone(timedelta(hours=9)))

        print(returnMessage)
        return df

    # 스토리지 정보 수정
    def update_storage(self):
        print("update")
    
    # 스토리지 삭제
    def delete_storage(self):
        print("delete")

    # 폴더 등록
    def create_folder(self, storageId, parentId, dirName):
        """ Create folder in stackbase's storage

        Args:
            storageId (Str): Storage ID that create folder.
            parentId (Str): Folder ID that create folder. If you want to set root path, you have to enter "".
            dirName (Str): Folder name.

        Raises:
            Exception: _description_

        Returns:
            _type_: _description_
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.userToken
        }

        bodys = json.dumps({
            "parentId": parentId,
            "name": dirName,
            "storageId": storageId
        })

        response = requests.request('post',f"{self.url}/stackbase/v1/folder", headers=headers, data=bodys)
        respStatus, returnMessage = self.checkStatusCode(response.status_code)

        if respStatus == 0:
            self.exceptionHandle(response, returnMessage)

        result = json.loads(response.content)
        result['createdAt'] = datetime.fromtimestamp(int(result['createdAt']/1000), timezone(timedelta(hours=9)))
        
        print(returnMessage)
    
    # 트리 검색
    def get_tree(self, storageId, parentId):
        """ Print list of tree in stackbase.

        Args:
            storageId (Str): Storage ID
            parentId (Str): Folder ID. If you want to set root path, you have to enter "".

        Raises:
            Exception: _description_

        Returns:
            _type_: _description_
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.userToken
        }

        param = {
            "storageId": storageId,
            "parentId": parentId
        }

        response = requests.request('get',f"{self.url}/stackbase/v1/trees", headers=headers, params=param)
        respStatus, returnMessage = self.checkStatusCode(response.status_code)

        if respStatus == 0:
            self.exceptionHandle(response, returnMessage)
        elif respStatus == 3:
            print(returnMessage)
            return 0
            
        result = json.loads(response.content)
        df1 = pd.DataFrame(result)
        df2 = pd.DataFrame(result['trees'])
        
        df = pd.concat([df1.drop(['trees'], axis=1), df2], axis=1)
        for n in range(len(df)):
            df.loc[n, 'modifiedAt'] = datetime.fromtimestamp(int(df.loc[n, 'modifiedAt']/1000), timezone(timedelta(hours=9)))
        
        print(returnMessage)
        return df

    # 폴더 수정
    def update_folder(self):
        print("update")

    # 폴더 삭제
    def delete_folder(self):
        print("delete")

    # 컨텐츠 조회
    def get_content(self):
        print("get")

    # 컨텐츠 수정
    def update_content(self):
        print("test")
    
    # 컨텐츠 삭제
    def delete_content(self):
        print("test")

    # 컨텐츠 다운로드
    def fget_content(self, fileId, getPath):
        """ Download content(file) from stackbase.

        Args:
            fileId (Str): File ID
            getPath (Str): File save path.

        Raises:
            Exception: _description_
        """
        headers = {
            "Authorization": self.userToken
        }

        response = requests.request('get',f"{self.url}/stackbase/v1/contents/download/{fileId}", headers=headers)
        respStatus, returnMessage = self.checkStatusCode(response.status_code)

        if respStatus == 0:
            self.exceptionHandle(response, returnMessage)
        
        with open(getPath, "wb") as f:
            f.write(response.content)
        
        print(returnMessage)
    
    # 컨텐츠 등록
    def fput_content(self, storageId, folderId, filePath, fileVersion, fileFormat, fileTag):
        """ Upload content(file) in stackbase

        Args:
            storageId (Str): Storage ID
            folderId (Str): Folder ID
            filePath (Str): Path of upload file
            fileVersion (Str): Version of file
            fileFormat (Str): Format of file
            fileTag (Str): Tag of file

        Raises:
            Exception: _description_

        Returns:
            _type_: _description_
        """
        headers = {
            "Authorization": self.userToken
        }

        bodys = json.dumps({
            "storageId": storageId,
            "folderId": folderId,
            "version": fileVersion,
            "format": fileFormat,
            "tag": fileTag
        })

        file_open = open(filePath, 'rb')

        files={
            'request': (None, bodys, 'application/json'),
            "content": (filePath.split("/")[-1], file_open, 'application/octet-stream')
        }

        response = requests.request("POST", f"{self.url}/stackbase/v1/contents", headers=headers, files=files)
        respStatus, returnMessage = self.checkStatusCode(response.status_code)

        if respStatus == 0:
            self.exceptionHandle(response, returnMessage)

        result = json.loads(response.content)
        result['createdAt'] = datetime.fromtimestamp(int(result['createdAt']/1000), timezone(timedelta(hours=9)))
        result['modifiedAt'] = datetime.fromtimestamp(int(result['modifiedAt']/1000), timezone(timedelta(hours=9)))
        
        print(returnMessage)