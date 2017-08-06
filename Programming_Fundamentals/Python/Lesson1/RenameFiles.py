
import os;

def rename_files():
        
    dirpath = "/Users/khaled/Downloads/alphabet/";
    
    if(os.path.exists(dirpath)) :
      myfiles = os.listdir(dirpath);
      for file_name in myfiles:
          newname = file_name.translate(None , '0123456789');
          print(dirpath+file_name)
          os.rename(dirpath+file_name , dirpath+newname);
 #         os.rename(actualpath , newname);

rename_files();
