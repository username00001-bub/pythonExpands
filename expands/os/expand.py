import os

def delete(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            file_path = os.path.join(root, name)
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except:
                    pass
        
        for dir in dirs:
            delete(os.path.join(root, dir))

        if os.path.exists(path):
            try:
                os.rmdir(path)
            except:
                pass