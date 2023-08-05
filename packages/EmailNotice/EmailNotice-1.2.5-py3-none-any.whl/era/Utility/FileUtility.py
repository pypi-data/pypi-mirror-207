import pandas as pd
from typing import Any, Callable

class _FileUtilitySingletion():
    _default_Header_list = 5
    _fileInstance = None
    _emailHeader = "Email"
    _attachmentHeader = "AttachmentPath"
    _ccListHeader = "CC"
    _bccListHeader = "BCC"
    _subjectHeader = "Subject"

    def __init__(self) -> None:
        pass


    def ReadEmailList(self,path):
        try:
            recipient_no_col = pd.read_excel(path,usecols='A:E',header=0,dtype=str)
            policy_no_list = recipient_no_col.values.tolist()
            return policy_no_list
        except:
            return None
        
    def ReadAttachmentList(self,path:str,callBack:Callable[[list], Any]):
        try:
            recipient_no_col = pd.read_excel(path,dtype=str)
            policy_no_list = [recipient_no_col.columns.ravel().tolist()]
            policy_no_list += recipient_no_col.values.tolist()
            callBack(policy_no_list)
            return
        except:
            callBack(None)
            return
    
    def CheckAttachmentFormat(self, data :list) -> bool:
        header = data[0]
        if len(header) < self._default_Header_list:
            return False
        elif header[0] == self._emailHeader and header[1] == self._attachmentHeader and header[2] == self._ccListHeader and header[3] == self._bccListHeader and header[4] == self._subjectHeader:
            return True
        else:
            return False


def GetFileUtilitySingletion():
    if _FileUtilitySingletion._fileInstance is None:
        _FileUtilitySingletion._fileInstance = _FileUtilitySingletion()
    return _FileUtilitySingletion._fileInstance